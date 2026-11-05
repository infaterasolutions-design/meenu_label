with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="productDetailView"')
end = html.find('<!-- END PRODUCT DETAIL VIEW -->', start)
if end == -1:
    end = html.find('</div>\n  </div>\n\n  <!-- QUICK VIEW MODAL', start)

pdp_section = html[start:end]
print("PDP section length:", len(pdp_section))
with open('scratch/pdp_exact_template.html', 'w', encoding='utf-8') as out:
    out.write(pdp_section)
print("Saved to scratch/pdp_exact_template.html")
