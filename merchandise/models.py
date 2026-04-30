# Chat GPT Code
from django.db import models
from django.templatetags.static import static
from django.utils.text import slugify


# ChatGPT Code
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)[:130] or "category"
            slug = base
            i = 1
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base[: 130 - (len(str(i)) + 1)]}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    handle = models.SlugField(max_length=255, unique=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products",
    )
    vendor = models.CharField(max_length=120, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    tags = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    image_src = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    # Stripe (optional now, useful later)
    stripe_product_id = models.CharField(max_length=255, blank=True)

    # ChatGPT Code
    def save(self, *args, **kwargs):
        # Generate handle if missing
        if not self.handle:
            base = slugify(self.title)[:240] or "product"
            handle = base
            i = 1
            while Product.objects.filter(handle=handle).exclude(pk=self.pk).exists():
                i += 1
                handle = f"{base[:235]}-{i}"
            self.handle = handle

        # Generate slug if missing
        if not self.slug:
            self.slug = self.handle

        super().save(*args, **kwargs)

    # ChatGPT Code
    def get_display_image(self):
        variant = self.variants.first()

        if variant and variant.image_src:
            return variant.image_src

        if self.image:
            return self.image.url

        if self.image_src:
            return self.image_src

        return static("images/noimage.jpg")


# ChatGPT Code
class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variants"
    )

    variant_title = models.CharField(max_length=255, blank=True)  # e.g. "Small / Black"
    sku = models.CharField(max_length=80, blank=True, null=True, db_index=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size = models.CharField(max_length=50, blank=True, null=True)
    inventory_quantity = models.IntegerField(default=0)

    image_src = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    # Stripe (this is the important one later)
    stripe_price_id = models.CharField(max_length=255, blank=True)

    class Meta:
        constraints = [
            # SKU is the best unique key when present
            models.UniqueConstraint(fields=["sku"], name="uniq_variant_sku"),
            # fallback uniqueness (when SKU missing)
            models.UniqueConstraint(
                fields=["product", "variant_title"],
                name="uniq_variant_per_product_title",
            ),
        ]

    def __str__(self):
        return f"{self.product.title} — {self.variant_title or self.sku or 'Variant'}"


# Claude AI code
class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="badges", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
