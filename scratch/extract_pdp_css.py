with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('.pdp-section {')
if start == -1:
    start = html.find('.pdp-section')

end = html.find('</style>', start)
pdp_css = html[start:end]
print("Found PDP CSS, length:", len(pdp_css))

with open('scratch/pdp_css.css', 'w', encoding='utf-8') as out:
    out.write(pdp_css)
print("Saved to scratch/pdp_css.css")
