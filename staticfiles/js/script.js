// Claude AI Code
// Back to Top functionality
$('.btt-link').click(function(e) {
  window.scrollTo(0,0)
});

// Sorting functionality
$('#sort-selector').change(function() {
  var selector = $(this);
  var currentUrl = new URL(window.location);
  var selectedVal = selector.val();
  if (selectedVal != "reset") {
    var sort = selectedVal.split("_")[0];
    var direction = selectedVal.split("_")[1];
    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);
    var newUrl = currentUrl.toString();
    history.pushState({}, null, newUrl);
    // Trigger a page reload or update the products list
    location.reload();
  } else {
    currentUrl.searchParams.delete("sort");
    currentUrl.searchParams.delete("direction");
    var newUrl = currentUrl.toString();
    history.pushState({}, null, newUrl);
    // Trigger a page reload or update the products list
    location.reload();
  }
});