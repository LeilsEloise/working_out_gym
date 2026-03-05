# Chat GPT Code
import csv
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.core.management.base import BaseCommand

from merchandise.models import Product, ProductVariant


def to_decimal(value) -> Decimal:
    if value is None:
        return Decimal("0.00")
    s = str(value).strip()
    if not s:
        return Decimal("0.00")
    s = re.sub(r"[^\d\.,-]", "", s).replace(",", "")
    try:
        return Decimal(s)
    except (InvalidOperation, ValueError):
        return Decimal("0.00")


def to_int(value) -> int:
    try:
        return int(float(str(value).strip()))
    except Exception:
        return 0


def clean_image_src(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return ""
    # dataset has multiple URLs separated by commas; keep first
    if "," in s:
        s = s.split(",")[0].strip()
    # remove any trailing junk after url
    if " " in s and s.startswith("http"):
        s = s.split()[0].strip()
    return s


class Command(BaseCommand):
    help = "Import Gymshark CSV into Product + ProductVariant (FAST create mode for --clear)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="merchandise/data/gymshark_products.csv",
            help="Path to the CSV file",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing products & variants before import",
        )

    def handle(self, *args, **options):
        csv_path = Path(options["path"])

        if not csv_path.exists():
            self.stderr.write(self.style.ERROR(f"CSV not found: {csv_path}"))
            return

        if options["clear"]:
            ProductVariant.objects.all().delete()
            Product.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing products & variants."))

        # Cache products by handle so we only create once per handle
        product_cache = {}

        # Dedupe variants in-memory to avoid IntegrityErrors
        seen_skus = set()
        seen_variant_keys = set()  # (handle, variant_title) fallback

        created_products = 0
        created_variants = 0
        skipped_rows = 0
        row_num = 0

        with csv_path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            self.stdout.write(self.style.WARNING(f"Detected columns: {reader.fieldnames}"))

            for row in reader:
                row_num += 1

                title = (row.get("title") or "").strip()
                handle = (row.get("handle") or "").strip()

                if not title or not handle:
                    skipped_rows += 1
                    continue

                image_src = clean_image_src(row.get("image_src") or "")
                product_type = (row.get("product_type") or "").strip()
                vendor = (row.get("vendor") or "").strip()
                tags = (row.get("tags") or "").strip()

                product = product_cache.get(handle)
                if product is None:
                    product = Product.objects.create(
                        title=title,
                        handle=handle,
                        product_type=product_type,
                        vendor=vendor,
                        tags=tags,
                        image_src=image_src,
                        is_active=True,
                    )
                    product_cache[handle] = product
                    created_products += 1

                variant_title = (row.get("variant_title") or "").strip()
                sku = (row.get("sku") or "").strip() or None

                # dedupe variants
                if sku:
                    if sku in seen_skus:
                        continue
                    seen_skus.add(sku)
                else:
                    key = (handle, variant_title)
                    if key in seen_variant_keys:
                        continue
                    seen_variant_keys.add(key)

                ProductVariant.objects.create(
                    product=product,
                    variant_title=variant_title,
                    sku=sku,
                    price=to_decimal(row.get("price")),
                    inventory_quantity=to_int(row.get("inventory_quantity")),
                    image_src=image_src,
                    is_active=True,
                )
                created_variants += 1

                if row_num % 250 == 0:
                    self.stdout.write(
                        f"Processed {row_num} rows... products: {created_products}, variants: {created_variants}"
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Import complete.\n"
                f"Products created: {created_products}\n"
                f"Variants created: {created_variants}\n"
                f"Rows skipped: {skipped_rows}"
            )
        )