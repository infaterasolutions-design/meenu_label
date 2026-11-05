related_markup = '''
  <!-- Curated Recommendations (Complete The Look / Product Suggestions) -->
  <div class="pdp-related-section">
    <div style="text-align: center; margin-bottom: 28px;">
      <span style="font-size: 11px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent-gold, #C5A059); display: block; margin-bottom: 6px;">
        Curated Atelier Ensembles
      </span>
      <h3 class="pdp-related-title" style="margin: 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 32px; font-weight: 600; color: var(--text-main, #1A1A1A);">
        Complete The Look &bull; Curated Drop 01 Pieces
      </h3>
      <p class="pdp-related-sub" style="margin-top: 6px; font-size: 12px; color: var(--text-muted, #7A7269); letter-spacing: 0.05em; text-transform: uppercase;">
        Other strictly limited silhouettes from our Autumn/Winter 2026 debut
      </p>
    </div>

    <div class="pdp-related-grid" id="shopifyRelatedGrid">
      {% assign current_id = product.id %}
      {% assign count = 0 %}

      {% comment %} 1. First prioritize same collection or category {% endcomment %}
      {% if collection and collection.products.size > 1 %}
        {% for p in collection.products %}
          {% if p.id != current_id and count < 4 %}
            {% render 'product-card', product: p %}
            {% assign count = count | plus: 1 %}
          {% endif %}
        {% endfor %}
      {% endif %}

      {% comment %} 2. Fill remaining from collections.all if fewer than 4 {% endcomment %}
      {% if count < 4 %}
        {% for p in collections.all.products %}
          {% if p.id != current_id and count < 4 %}
            {% render 'product-card', product: p %}
            {% assign count = count | plus: 1 %}
          {% endif %}
        {% endfor %}
      {% endif %}
    </div>
  </div>
'''

js_fallback = '''
  // Client-side fallback to fetch recommendations if server loop had no items
  window.addEventListener('DOMContentLoaded', function() {
    var grid = document.getElementById('shopifyRelatedGrid');
    if (grid && grid.children.length === 0) {
      fetch('/recommendations/products.json?product_id={{ product.id }}&limit=4')
        .then(function(res) { return res.json(); })
        .then(function(data) {
          if (data && data.products && data.products.length > 0) {
            grid.innerHTML = data.products.map(function(p) {
              var priceFormatted = (p.price / 100).toLocaleString('en-IN');
              var imgUrl = p.featured_image || (p.images && p.images[0]) || '';
              return '<div class="product-card">' +
                '<div class="card-thumb">' +
                  '<a href="' + p.url + '"><img src="' + imgUrl + '" alt="' + p.title + '" loading="lazy"></a>' +
                '</div>' +
                '<div class="card-body">' +
                  '<a href="' + p.url + '"><h3 class="card-title">' + p.title + '</h3></a>' +
                  '<div class="card-price-row"><span class="price-main">&#8377;' + priceFormatted + '</span></div>' +
                '</div>' +
              '</div>';
            }).join('');
          }
        })
        .catch(function(err) {
          console.log('Related products fallback note:', err);
        });
    }
  });
'''

for path in ['sections/main-product.liquid', 'meenu-label-shopify-theme/sections/main-product.liquid']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of .pdp-grid and insert related_markup before closing </div> of .pdp-section
    target_end = '        </div>\n      </div>\n    </div>\n  </div>\n</div>'
    if target_end in content and 'pdp-related-section' not in content:
        replacement = '        </div>\n      </div>\n    </div>\n  </div>\n' + related_markup + '\n</div>'
        content = content.replace(target_end, replacement, 1)
        print(f"Added related_markup to {path}")
    else:
        print(f"Target end not found or already has pdp-related-section in {path}")

    # Add js_fallback before </script>
    if '</script>' in content and 'shopifyRelatedGrid' in content and 'Related products fallback note' not in content:
        content = content.replace('</script>', js_fallback + '\n</script>', 1)
        print(f"Added js_fallback to {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
