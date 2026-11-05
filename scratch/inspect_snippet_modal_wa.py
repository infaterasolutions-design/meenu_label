with open('snippets/notify-me-modal.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('notifyConciergeWhatsAppBtn')
print(c[idx:idx+300])
