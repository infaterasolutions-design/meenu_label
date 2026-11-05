collection_liquid = '''{% comment %}
  Meenu Label Dedicated Atelier Collection Page Section
{% endcomment %}

<section class="catalog-section" id="collection-grid" style="margin-top: 30px;">
  <div class="sticky-catalog-header" id="stickyCatalogHeader">
    <div class="sticky-header-info">
      <div style="display: flex; align-items: center; gap: 10px;">
        <h1 class="section-title" style="margin: 0; font-size: 22px; letter-spacing: 0.02em;">
          {{ collection.title | default: 'Signature Silhouettes' }}
        </h1>
        <span class="sticky-count-pill" id="activeCategoryCount">
          {{ collection.products_count | default: 0 }} SILHOUETTES
        </span>
      </div>
      <p class="section-sub" style="margin: 4px 0 0 0; font-size: 12px;">
        {{ collection.description | default: 'Limited Atelier Run • Handcrafted in Chandigarh' }}
      </p>
    </div>

    <div class="filter-tabs">
      <a href="/collections/all" class="filter-tab {% if collection.handle == 'all' or collection.handle == blank %}active{% endif %}">All Silhouettes</a>
      <a href="/collections/co-ord-sets" class="filter-tab {% if collection.handle == 'co-ord-sets' %}active{% endif %}">Co-ord Sets</a>
      <a href="/collections/festive-suits" class="filter-tab {% if collection.handle == 'festive-suits' %}active{% endif %}">Festive Suits</a>
      <a href="/collections/dresses" class="filter-tab {% if collection.handle == 'dresses' %}active{% endif %}">Midi Dresses</a>
      <a href="/collections/tops" class="filter-tab {% if collection.handle == 'tops' or collection.handle == 'tops-blouses' %}active{% endif %}">Casual Tops</a>
    </div>
  </div>

  {% paginate collection.products by 24 %}
    <div class="product-grid" id="productGrid">
      {% if collection.products_count > 0 %}
        {% for product in collection.products %}
          {% render 'product-card', product: product %}
        {% endfor %}
      {% else %}
        <div style="grid-column: 1 / -1; text-align: center; padding: 70px 20px; background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 8px;">
          <div style="font-size: 38px; margin-bottom: 12px; opacity: 0.7;">✨</div>
          <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; margin: 0 0 8px; color: #1E1C19;">Editions Arriving Soon</h2>
          <p style="font-size: 13px; color: var(--text-muted); max-width: 420px; margin: 0 auto 20px; line-height: 1.6;">
            We craft our pieces in strictly limited small batches. Explore our full Drop 01 catalog to discover currently available pieces.
          </p>
          <a href="/collections/all" class="modal-btn-primary" style="display: inline-block; width: auto; padding: 11px 26px; text-decoration: none;">
            VIEW ALL AVAILABLE SILHOUETTES &rarr;
          </a>
        </div>
      {% endif %}
    </div>

    {% if paginate.pages > 1 %}
      <div style="display: flex; justify-content: center; gap: 8px; margin-top: 40px;">
        {{ paginate | default_pagination }}
      </div>
    {% endif %}
  {% endpaginate %}
</section>

{% schema %}
{
  "name": "Main Collection",
  "settings": []
}
{% endschema %}
'''

import os
paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\sections\main-collection.liquid',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\main-collection.liquid'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(collection_liquid)
    print(f"Created {p}")
