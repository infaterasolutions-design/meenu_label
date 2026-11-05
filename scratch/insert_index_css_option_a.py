css_to_insert = """
/* =========================================================================
   DIRECT WHATSAPP CONCIERGE RESTOCK ENGINE (OPTION A)
   ========================================================================= */

/* Primary WhatsApp Notify Button on PDP */
.pdp-btn-notify-whatsapp {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  padding: 16px 24px;
  background: #25D366;
  color: #FFFFFF !important;
  border: 1.5px solid #1EBE5D;
  border-radius: 4px;
  font-family: inherit;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none !important;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.28);
}

.pdp-btn-notify-whatsapp:hover {
  background: #1EBE5D;
  border-color: #16A34A;
  color: #FFFFFF !important;
  box-shadow: 0 6px 22px rgba(37, 211, 102, 0.4);
  transform: translateY(-2px);
}

.pdp-btn-notify-whatsapp svg {
  fill: currentColor;
  flex-shrink: 0;
}

/* Secondary Waitlist Trigger Button on PDP */
.pdp-btn-notify-waitlist {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 12px 18px;
  background: #FAF7F2;
  color: #57534E;
  border: 1px dashed #C8A364;
  border-radius: 4px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 6px;
}

.pdp-btn-notify-waitlist:hover {
  background: #F5EBE1;
  color: #1C1917;
  border-color: #A37E3A;
  border-style: solid;
}

/* Grid Card WhatsApp Notify Trigger */
.snitch-notify-trigger.whatsapp-notify-trigger {
  background: #1C1917;
  color: #25D366;
  border-color: rgba(37, 211, 102, 0.5);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
  text-decoration: none !important;
}

.snitch-notify-trigger.whatsapp-notify-trigger:hover {
  background: #25D366;
  color: #FFFFFF;
  border-color: #25D366;
  box-shadow: 0 4px 14px rgba(37, 211, 102, 0.35);
}

.snitch-notify-trigger.whatsapp-notify-trigger svg {
  fill: currentColor;
}
"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = """.notify-title {
    font-size: 23px;
  }
}"""

if target in c:
    c = c.replace(target, target + "\n" + css_to_insert, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("SUCCESS: Option A CSS inserted into index.html")
else:
    print("ERROR: Target not found in index.html")
