import os
import io
import pymupdf
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
)

# 1. Prepare Paths
pdf_in_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
thumb_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\po_thumbs"
os.makedirs(thumb_dir, exist_ok=True)
pdf_out_path = r"C:\Users\sande\Downloads\Meenu_Label_Purchase_Order.pdf"

items = [
    ("JAC26ST03743", 19, "3-Piece Suit (Kurta+Pant+Dupatta)", "Silk Blend (Lavender)", 615, 5),
    ("SET566", 8, "3-Piece Suit (Kurta+Pant+Dupatta)", "Pure Chinon (Mauve)", 715, 5),
    ("SLA26ST03996", 18, "3-Piece Suit (Kurta+Pant+Dupatta)", "Crepe (Sage Grey)", 595, 5),
    ("SET974", 4, "2-Piece Set (Angrakha+Pant)", "Crepe Silk (Mustard)", 555, 5),
    ("SET916", 16, "2-Piece Co-ord (Halter+Palazzo)", "Dobby Chiffon (Lime)", 675, 5),
    ("JAC25CD03428", 17, "2-Piece Co-ord (Tunic+Pant)", "Cotton Blend (Ivory)", 555, 5),
    ("JAA26DR04446", 23, "Flared Midi Dress", "Georgette (Garden Floral)", 675, 5),
    ("JNE4046", 25, "Belted Wrap Dress", "Georgette (Porcelain Blue)", 575, 5),
]

# 2. Extract and crop clean thumbnails
doc = pymupdf.open(pdf_in_path)

thumb_paths = {}
for code, page_num, cat, fabric, rate, pcs in items:
    page = doc[page_num - 1]
    images = doc.get_page_images(page_num - 1)
    if images:
        xref = images[0][0]
        base_img = doc.extract_image(xref)
        pil_img = Image.open(io.BytesIO(base_img["image"]))
        w, h = pil_img.size
        cropped = pil_img.crop((int(w * 0.05), int(h * 0.12), int(w * 0.95), int(h * 0.88)))
        cropped.thumbnail((160, 240))
        t_path = os.path.join(thumb_dir, f"{code}.jpg")
        cropped.save(t_path, "JPEG", quality=85)
        thumb_paths[code] = t_path

# 3. Build 1-Page PDF with ReportLab
doc_pdf = SimpleDocTemplate(
    pdf_out_path,
    pagesize=A4,
    leftMargin=24,
    rightMargin=24,
    topMargin=20,
    bottomMargin=18
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontSize=18,
    leading=22,
    textColor=colors.HexColor("#1A1A1A"),
    spaceAfter=2,
)
subtitle_style = ParagraphStyle(
    "SubTitleStyle",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#555555"),
)
header_label = ParagraphStyle(
    "HeaderLabel",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#222222"),
)
cell_style = ParagraphStyle(
    "CellStyle",
    parent=styles["Normal"],
    fontSize=8,
    leading=10.5,
    textColor=colors.HexColor("#222222"),
)
cell_bold = ParagraphStyle(
    "CellBold",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=11,
    fontName="Helvetica-Bold",
    textColor=colors.HexColor("#111111"),
)
cell_center = ParagraphStyle(
    "CellCenter",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=11,
    alignment=1,
    textColor=colors.HexColor("#222222"),
)

elements = []

# Header Box
header_data = [
    [
        Paragraph("<b>MEENU LABEL</b><br/><font size=8 color='#666'>Infatera Software Solutions OPC Pvt. Ltd.<br/>Chandigarh, India | meenulabel24@gmail.com</font>", title_style),
        Paragraph("<div align='right'><b>PURCHASE ORDER</b><br/><font size=8 color='#555'>PO Date: 17-Oct-2026<br/>Ref: Selected Catalog / Drop 01<br/>Destination: Chandigarh</font></div>", subtitle_style)
    ]
]
header_table = Table(header_data, colWidths=[280, 268])
header_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
]))
elements.append(header_table)

# Divider line
divider = Table([[""]], colWidths=[548], rowHeights=[2])
divider.setStyle(TableStyle([
    ("LINEABOVE", (0, 0), (-1, -1), 1.2, colors.HexColor("#2B2723")),
]))
elements.append(divider)
elements.append(Spacer(1, 4))

# Note to dealer
note_p = Paragraph(
    "<b>Order Details:</b> Please supply <b>1 Full Size-Set Bundle (S, M, L, XL, XXL)</b> per design code as listed below. Total 8 designs = 40 pieces. Please share your Proforma Invoice & Bank Details for immediate payment.",
    header_label
)
elements.append(note_p)
elements.append(Spacer(1, 6))

# Table Header
table_data = [
    [
        Paragraph("<b>Photo</b>", cell_center),
        Paragraph("<b>Design Code & Category</b>", cell_bold),
        Paragraph("<b>Fabric</b>", cell_bold),
        Paragraph("<b>Sizes (1 Set)</b>", cell_center),
        Paragraph("<b>Rate (Rs.)</b>", cell_center),
        Paragraph("<b>Qty</b>", cell_center),
        Paragraph("<b>Total (Rs.)</b>", cell_center),
    ]
]

subtotal = 0
total_pcs = 0

for idx, (code, page_num, cat, fabric, rate, pcs) in enumerate(items, 1):
    amount = rate * pcs
    subtotal += amount
    total_pcs += pcs
    
    img_widget = Paragraph("Photo", cell_center)
    if code in thumb_paths and os.path.exists(thumb_paths[code]):
        try:
            # 32w x 48h to fit cleanly on one single A4 page
            img_widget = RLImage(thumb_paths[code], width=32, height=48)
        except:
            pass

    desc_p = Paragraph(f"<b>{code}</b><br/><font size=7 color='#666'>Pg #{page_num} | {cat}</font>", cell_style)
    fabric_p = Paragraph(fabric, cell_style)
    sizes_p = Paragraph("S, M, L, XL, XXL", cell_center)
    rate_p = Paragraph(f"Rs. {rate}", cell_center)
    qty_p = Paragraph(f"<b>{pcs}</b> pcs", cell_center)
    amt_p = Paragraph(f"<b>Rs. {amount:,}</b>", cell_center)

    table_data.append([img_widget, desc_p, fabric_p, sizes_p, rate_p, qty_p, amt_p])

gst_5 = round(subtotal * 0.05, 2)
grand_total = subtotal + gst_5

# Summary Rows
table_data.append(["", "", "", "", Paragraph("<b>Subtotal:</b>", cell_bold), Paragraph(f"<b>{total_pcs} pcs</b>", cell_center), Paragraph(f"<b>Rs. {subtotal:,}</b>", cell_center)])
table_data.append(["", "", "", "", Paragraph("<b>GST (5%):</b>", cell_style), "", Paragraph(f"Rs. {gst_5:,}", cell_center)])
table_data.append(["", "", "", "", Paragraph("<b>GRAND TOTAL:</b>", cell_bold), "", Paragraph(f"<font color='#B22222' size=9.5><b>Rs. {round(grand_total):,}</b></font>", cell_center)])

col_widths = [40, 155, 120, 80, 52, 40, 61]
t = Table(table_data, colWidths=col_widths, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F5F2EB")),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ("TOPPADDING", (0, 0), (-1, -1), 2.5),
    ("GRID", (0, 0), (-1, len(items)), 0.5, colors.HexColor("#E0DCD5")),
    ("LINEBELOW", (0, 0), (-1, 0), 1.2, colors.HexColor("#2B2723")),
    ("LINEABOVE", (4, len(items)+1), (-1, len(items)+1), 1, colors.HexColor("#2B2723")),
    ("BACKGROUND", (4, -1), (-1, -1), colors.HexColor("#FDF9F3")),
    ("SPAN", (4, len(items)+1), (4, len(items)+1)),
]))

elements.append(t)
elements.append(Spacer(1, 8))

# Footer instructions
footer_p = Paragraph(
    "<font size=8 color='#444'><b>Payment & Dispatch:</b> Payment will be processed immediately upon receipt of Bank Details / Invoice. Please pack carefully with individual poly-bags and dispatch to Chandigarh via express transport.</font>",
    subtitle_style
)
elements.append(footer_p)

doc_pdf.build(elements)
print(f"SUCCESS: 1-Page PO PDF generated at {pdf_out_path}")
