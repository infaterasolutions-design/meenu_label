html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

target = "function closeCartPage() {"
listener_code = """window.addEventListener('hashchange', function() {
      var h = window.location.hash;
      if (h === '#cart') {
        openCartPage();
      } else if (h.indexOf('#product-') === 0) {
        var pId = h.replace('#product-', '');
        openProductPage(pId);
      } else if (!h || h === '#home' || h === '#') {
        var cartView = document.getElementById('cartPageView');
        var pdpView = document.getElementById('productDetailView');
        var homeView = document.getElementById('storefrontHomeView');
        if (cartView) cartView.style.display = 'none';
        if (pdpView) pdpView.style.display = 'none';
        if (homeView) homeView.style.display = 'block';
      }
    });

    // Check hash on load
    if (window.location.hash === '#cart') {
      setTimeout(openCartPage, 100);
    } else if (window.location.hash.indexOf('#product-') === 0) {
      setTimeout(function() {
        openProductPage(window.location.hash.replace('#product-', ''));
      }, 100);
    }

    """ + target

if target in content:
    content = content.replace(target, listener_code, 1)
    print("Added hash navigation listeners!")
else:
    print("ERROR: target not found")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Hash listeners saved!")
