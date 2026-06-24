"""
Bannaga Altieb Abdul Muhsin — CV
Style 5: cyan/charcoal sidebar with circular photo, icon section headers,
skill bars. Flows naturally across multiple pages.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, FrameBreak, NextPageTemplate,
    Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether,
)

W, H = A4

# ── Colours ───────────────────────────────────────────────────────────────────
HEADER_BLUE = colors.HexColor("#27b3df")   # cyan header block
SIDEBAR_DK  = colors.HexColor("#2c3035")   # charcoal sidebar
ACCENT      = colors.HexColor("#1ba0cc")   # accent (bars, icons, rules)
DARK        = colors.HexColor("#222629")
MID         = colors.HexColor("#3d444b")
GREY        = colors.HexColor("#6b7280")
TRACK       = colors.HexColor("#dfe3e6")   # empty bar track
SIDE_TXT    = colors.HexColor("#d7dbdf")   # sidebar body text
SIDE_MUTE   = colors.HexColor("#aeb4ba")
WHITE       = colors.white
RULE        = colors.HexColor("#e2e6ea")

# ── Geometry ──────────────────────────────────────────────────────────────────
SIDEBAR_W = 196
HEADER_H  = 250
PHOTO_D   = 118

# ── Styles ────────────────────────────────────────────────────────────────────
# Sidebar
S_HDR  = ParagraphStyle("s_hdr",  fontName="Helvetica-Bold",   fontSize=10, textColor=WHITE,     leading=13, spaceAfter=1, spaceBefore=2)
S_BODY = ParagraphStyle("s_body", fontName="Helvetica",        fontSize=8.3,textColor=SIDE_TXT,  leading=12)
S_BOLD = ParagraphStyle("s_bold", fontName="Helvetica-Bold",   fontSize=8.5,textColor=WHITE,     leading=12)
S_MUTE = ParagraphStyle("s_mute", fontName="Helvetica",        fontSize=7.8,textColor=SIDE_MUTE, leading=11)

# Main
M_HDR  = ParagraphStyle("m_hdr",  fontName="Helvetica-Bold",   fontSize=12, textColor=DARK,   leading=15, spaceAfter=2)
BODY   = ParagraphStyle("body",   fontName="Helvetica",        fontSize=9.5,textColor=MID,    leading=14, alignment=TA_JUSTIFY)
BULLET = ParagraphStyle("bullet", fontName="Helvetica",        fontSize=9.5,textColor=MID,    leading=14, leftIndent=11, firstLineIndent=-6)
JOB_T  = ParagraphStyle("job_t",  fontName="Helvetica-Bold",   fontSize=10.5,textColor=DARK,  leading=14)
JOB_C  = ParagraphStyle("job_c",  fontName="Helvetica-Bold",   fontSize=9.5,textColor=ACCENT, leading=13)
JOB_D  = ParagraphStyle("job_d",  fontName="Helvetica-Oblique",fontSize=8.5,textColor=GREY,   leading=12)
SKILL_L= ParagraphStyle("skill_l",fontName="Helvetica-Bold",   fontSize=9,  textColor=DARK,   leading=12)
SMALL  = ParagraphStyle("small",  fontName="Helvetica",        fontSize=9,  textColor=MID,    leading=13)
BOLD   = ParagraphStyle("bold",   fontName="Helvetica-Bold",   fontSize=9.5,textColor=DARK,   leading=14)
QUOTE  = ParagraphStyle("quote",  fontName="Helvetica-Oblique",fontSize=8,  textColor=GREY,   leading=12)

PHOTO_PATH = "assets/images/profile_circle.png"


def sp(h=4):
    return Spacer(1, h)


# ── Sidebar helpers ───────────────────────────────────────────────────────────
def s_section(title):
    return [
        sp(8),
        Paragraph(title.upper(), S_HDR),
        HRFlowable(width="100%", thickness=1, color=HEADER_BLUE, spaceAfter=5, spaceBefore=2),
    ]


# ── Main helpers ──────────────────────────────────────────────────────────────
def m_section(title):
    """Icon-style header: accent square + uppercase title + rule."""
    head = Table(
        [[" ", Paragraph(title.upper(), M_HDR)]],
        colWidths=[14, None],
    )
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), ACCENT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return [
        sp(6),
        head,
        HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceAfter=7, spaceBefore=4),
    ]


def skill_bar(label, pct, bar_w):
    fill = max(2, bar_w * pct / 100.0)
    rest = max(0.5, bar_w - fill)
    bar = Table([[" ", " "]], colWidths=[fill, rest], rowHeights=[6])
    bar.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), ACCENT),
        ("BACKGROUND", (1, 0), (1, 0), TRACK),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [Paragraph(label, SKILL_L), sp(2), bar, sp(7)]


# ── Page painters ─────────────────────────────────────────────────────────────
def paint_sidebar_bg(canvas):
    canvas.setFillColor(SIDEBAR_DK)
    canvas.rect(0, 0, SIDEBAR_W, H, fill=1, stroke=0)


def on_first(canvas, doc):
    canvas.saveState()
    paint_sidebar_bg(canvas)
    # cyan header block
    canvas.setFillColor(HEADER_BLUE)
    canvas.rect(0, H - HEADER_H, SIDEBAR_W, HEADER_H, fill=1, stroke=0)
    # circular photo
    cx = SIDEBAR_W / 2.0
    px = cx - PHOTO_D / 2.0
    py = H - 34 - PHOTO_D
    drawn = False
    if os.path.exists(PHOTO_PATH):
        try:
            canvas.drawImage(ImageReader(PHOTO_PATH), px, py, PHOTO_D, PHOTO_D, mask="auto")
            drawn = True
        except Exception as exc:
            print(f"⚠ could not draw photo '{PHOTO_PATH}': {exc}")
    else:
        print(f"⚠ photo not found at '{PHOTO_PATH}' — using initials placeholder")
    if not drawn:
        canvas.setFillColor(colors.white)
        canvas.circle(cx, py + PHOTO_D / 2.0, PHOTO_D / 2.0, fill=1, stroke=0)
        canvas.setFillColor(SIDEBAR_DK)
        canvas.setFont("Helvetica-Bold", 44)
        canvas.drawCentredString(cx, py + PHOTO_D / 2.0 - 16, "BA")
    # name + title (on cyan block, dark text)
    canvas.setFillColor(colors.HexColor("#10303a"))
    canvas.setFont("Helvetica-Bold", 15)
    canvas.drawCentredString(cx, py - 26, "BANNAGA ALTIEB")
    canvas.drawCentredString(cx, py - 44, "ABDUL MUHSIN")
    canvas.setFont("Helvetica", 8.7)
    canvas.setFillColor(colors.HexColor("#0c2a32"))
    canvas.drawCentredString(cx, py - 62, "Electrical Project Engineer")
    canvas.restoreState()


def on_later(canvas, doc):
    canvas.saveState()
    paint_sidebar_bg(canvas)
    # slim cyan top strip for continuity
    canvas.setFillColor(HEADER_BLUE)
    canvas.rect(0, H - 14, SIDEBAR_W, 14, fill=1, stroke=0)
    canvas.restoreState()


# ── Build ─────────────────────────────────────────────────────────────────────
def build():
    doc = BaseDocTemplate(
        "assets/Bannaga_CV.pdf",
        pagesize=A4,
        leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0,
        title="Bannaga Altieb Abdul Muhsin — CV",
        author="Bannaga Altieb Abdul Muhsin",
    )

    gap = 24
    # Frames
    sidebar_frame = Frame(
        0, 28, SIDEBAR_W, H - HEADER_H - 28,
        leftPadding=18, rightPadding=15, topPadding=10, bottomPadding=12, id="side",
    )
    main_x = SIDEBAR_W + gap
    main_w = W - main_x - 30
    main_frame_first = Frame(
        main_x, 30, main_w, H - 30 - 38,
        leftPadding=0, rightPadding=0, topPadding=8, bottomPadding=10, id="main1",
    )
    main_frame_later = Frame(
        main_x, 30, main_w, H - 30 - 30,
        leftPadding=0, rightPadding=0, topPadding=22, bottomPadding=10, id="main2",
    )

    doc.addPageTemplates([
        PageTemplate(id="first", frames=[sidebar_frame, main_frame_first], onPage=on_first),
        PageTemplate(id="later", frames=[main_frame_later], onPage=on_later),
    ])

    inner_w = main_w  # main content width for bars

    # ══════════════════════════════════════════════════════════════════════════
    # SIDEBAR CONTENT
    # ══════════════════════════════════════════════════════════════════════════
    side = []
    side += s_section("Contact")
    side.append(Paragraph("Phone", S_BOLD))
    side.append(Paragraph("+966 54 296 6343", S_BODY))
    side.append(sp(3))
    side.append(Paragraph("Email", S_BOLD))
    side.append(Paragraph("eng.altieb@gmail.com", S_BODY))
    side.append(sp(3))
    side.append(Paragraph("Location", S_BOLD))
    side.append(Paragraph("Riyadh, Saudi Arabia", S_BODY))
    side.append(sp(3))
    side.append(Paragraph("Online", S_BOLD))
    side.append(Paragraph("linkedin.com/in/bannaga-abdalmuhsin", S_MUTE))
    side.append(Paragraph("x.com/AltiebBannaga", S_MUTE))
    side.append(Paragraph("instagram.com/bannga.altieb", S_MUTE))

    side += s_section("Education")
    side.append(Paragraph("B.Sc. Electronic Engineering (Control)", S_BOLD))
    side.append(Paragraph("El Neelain University", S_BODY))
    side.append(Paragraph("Khartoum, Sudan · 2007–2012", S_MUTE))

    side += s_section("Certifications")
    for c in ["CEM® — Certified Energy Manager",
              "CMVP® — Measurement & Verification",
              "LEED Green Associate",
              "Machine Learning with Python",
              "Power BI Essential Training",
              "SCADA / PLC / DCS / RTU"]:
        side.append(Paragraph("• " + c, S_BODY))

    side += s_section("Languages")
    side.append(Paragraph("Arabic — Native", S_BODY))
    side.append(Paragraph("English — Professional", S_BODY))

    side += s_section("Memberships")
    side.append(Paragraph("Saudi Council of Engineers (SCE)", S_BODY))
    side.append(Paragraph("Sudanese Engineers Association (SEA)", S_BODY))

    side += s_section("Availability")
    side.append(Paragraph("Sun–Thu: 8:00 AM – 6:00 PM", S_BODY))
    side.append(Paragraph("Weekends: on-call for urgencies", S_BODY))
    side.append(Paragraph("Open to short-notice travel", S_BODY))

    # ══════════════════════════════════════════════════════════════════════════
    # MAIN CONTENT
    # ══════════════════════════════════════════════════════════════════════════
    main = []

    # Profile
    main += m_section("Profile")
    main.append(Paragraph(
        "Certified Energy Manager (CEM®) and Certified Measurement &amp; Verification Professional (CMVP®) with "
        "14+ years of experience in electrical and energy engineering. Specializes in project management, telecom "
        "power systems, energy-efficient solutions, and technical operations across diverse infrastructure. "
        "Expertise spans data collection, energy analysis, facilities management, AI-driven dashboards, and "
        "structured reporting — delivering innovative, reliable, and performance-driven engineering solutions "
        "across telecom, power generation, and industrial sectors. Fluent in English and Arabic.",
        BODY))
    main.append(sp(6))

    # Work Experience
    main += m_section("Work Experience")
    experience = [
        ("2019 – Present", "Electrical Project Engineer", "ACES  |  Riyadh, Saudi Arabia", [
            "Serve as Energy Manager and efficiency designer across STC COW and Mobily ENM managed networks.",
            "O&amp;M Engineer for Mobily ENM Managed Services — full facility operations, CAFM/BMS integration, and KPI reporting.",
            "O&amp;M Engineer for STC COW Managed Services — operations and maintenance across 600+ nationwide telecom sites.",
            "Delivered multi-phase energy optimization programs achieving up to 18% reduction in utility costs.",
            "Developed Python automation for energy reporting and ML-based anomaly detection alerts.",
            "Built an AI-driven Energy &amp; Environmental Dashboard for CO2 footprint monitoring across all STC COW sites.",
            "Mentored junior engineers and standardized field engineering practices.",
        ]),
        ("2018 – 2019", "Electrical Project Engineer", "Absar  |  Riyadh, Saudi Arabia", [
            "Executed SEC unified-contract builds for 60+ MV/LV electrical assets (RMUs, transformers, LV switchgear).",
            "Performed full commissioning, testing, and zero-defect SEC handover documentation.",
            "Installed and configured SCADA monitoring and control system integration.",
        ]),
        ("2017 – 2018", "Electrical Engineer", "BEMCO", [
            "Preventive and corrective maintenance for 11kV distribution networks.",
            "Developed standardized testing, inspection, and commissioning manuals.",
            "Managed NCR resolutions and maintained technical documentation workflows.",
        ]),
        ("2012 – 2017", "Electrical Engineer", "SEC Thermal Generation  |  Sudan", [
            "Day-to-day operations and maintenance for a 200 MW thermal generation block.",
            "Managed wastewater treatment systems using PH meters and OC 4000 DCS controls.",
            "Preventive maintenance and fault management for 11kV distribution systems.",
        ]),
    ]
    for date, title, company, bullets in experience:
        head = Table([[
            Paragraph(title, JOB_T),
            Paragraph(date, ParagraphStyle("dr", parent=JOB_D, alignment=2)),
        ]], colWidths=[inner_w * 0.66, inner_w * 0.34])
        head.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        main.append(KeepTogether([
            head,
            Paragraph(company, JOB_C),
            sp(3),
            *[Paragraph(f"• {b}", BULLET) for b in bullets[:2]],
        ]))
        for b in bullets[2:]:
            main.append(Paragraph(f"• {b}", BULLET))
        main.append(sp(8))

    # Key Projects
    main += m_section("Key Projects")
    projects = [
        ("STC COW Network — O&amp;M &amp; Energy Optimization",
         "End-to-end O&amp;M for 600+ telecom sites nationwide; systematic energy auditing, SCADA oversight, and "
         "multi-phase optimization achieving up to 18% utility cost reduction."),
        ("Mobily ENM Managed Services",
         "Full O&amp;M and facility operations including CAFM/BMS integration, outage prevention, and structured "
         "performance reporting."),
        ("Mobily Data Center Energy Audit",
         "Comprehensive energy audit of critical data center infrastructure delivering measurable PUE improvements, "
         "certified under CEM® / CMVP® methodology."),
        ("SEC Unified Contract — MV/LV Commissioning",
         "Installation and commissioning of 60+ MV/LV assets with full SCADA integration and zero-defect SEC handover."),
        ("PP12 Thermal Generation Plant — 200 MW",
         "Operations including 11kV switching, safety routines, wastewater treatment, and DCS-based environmental monitoring."),
        ("AI CO2 &amp; Energy Dashboard",
         "ML-based anomaly detection and CO2 footprint tracking dashboards built with Python, Power BI, SQL Server, and DAX."),
    ]
    for title, desc in projects:
        main.append(KeepTogether([
            Paragraph(f"<b>{title}</b>", SMALL),
            Paragraph(desc, BODY),
            sp(5),
        ]))
    main.append(sp(2))

    # Skills & Expertise (bars)
    main += m_section("Skills & Expertise")
    skills = [
        ("Energy Management (CEM® / CMVP®)", 95),
        ("Power Systems — HV / MV / LV", 93),
        ("SCADA / DCS / PLC / RTU", 90),
        ("Power BI &amp; Data Analytics", 92),
        ("Python &amp; Automation / ML", 85),
        ("Project &amp; O&amp;M Management", 94),
    ]
    bar_w = inner_w
    rows = []
    for i in range(0, len(skills), 2):
        left = skill_bar(*skills[i], bar_w * 0.46)
        right = skill_bar(*skills[i + 1], bar_w * 0.46) if i + 1 < len(skills) else ""
        rows.append([left, right])
    grid = Table(rows, colWidths=[inner_w * 0.5, inner_w * 0.5])
    grid.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    main.append(grid)
    main.append(sp(4))

    # Key Accomplishments
    main += m_section("Key Accomplishments")
    for a in [
        "Reduced nationwide telecom site utility costs by up to <b>18%</b> through multi-phase energy optimization.",
        "Delivered uninterrupted O&amp;M coverage for STC COW &amp; Mobily ENM with proactive outage prevention.",
        "Cut incident resolution time by <b>30%</b> via troubleshooting guides and automation routines.",
        "Commissioned <b>60+ MV/LV assets</b> under SEC unified contracts with full SCADA integration.",
        "Built an AI-driven Energy &amp; Environmental Dashboard tracking real-time CO2 emissions and efficiency.",
        "Modeled operational trends across 600+ multi-site networks using Power BI, Python, and SQL Server.",
    ]:
        main.append(Paragraph(f"• {a}", BULLET))
        main.append(sp(2))
    main.append(sp(4))

    # AI & Development
    main += m_section("AI & Development")
    main.append(Paragraph("<b>AI &amp; Automation</b>", BOLD))
    for b in [
        "Designed Python automation to streamline energy performance reporting and KPI tracking.",
        "Developed ML-based anomaly detection alerts for telecom site power consumption.",
        "Built governance-ready Energy &amp; Environmental dashboards for CO2 footprint monitoring.",
        "Applied Power BI, SQL Server, and DAX to model operational trends across multi-site networks.",
    ]:
        main.append(Paragraph(f"• {b}", BULLET))
    main.append(sp(4))
    main.append(Paragraph("<b>Development &amp; Tools</b>", BOLD))
    for b in [
        "Created reusable troubleshooting guides and diagnostic scripts for SCADA / PLC / DCS systems.",
        "Documented API-style checklists to standardize field data capture and site integrations.",
        "Version-controlled documentation and engineering templates using Git/GitHub workflows.",
    ]:
        main.append(Paragraph(f"• {b}", BULLET))
    main.append(sp(8))

    # Footer quote
    main.append(HRFlowable(width="100%", thickness=1, color=RULE, spaceAfter=6, spaceBefore=2))
    main.append(Paragraph(
        '"You never change things by fighting the existing reality. To change something, build a new model '
        'that makes the old one obsolete."  — R. Buckminster Fuller', QUOTE))
    main.append(sp(3))
    main.append(Paragraph("© 2025 Eng. Bannaga Altieb Abdul Muhsin", QUOTE))

    # ══════════════════════════════════════════════════════════════════════════
    # ASSEMBLE: sidebar fills first frame, then main flows across pages
    # ══════════════════════════════════════════════════════════════════════════
    story = [NextPageTemplate("later")]
    story += side
    story.append(FrameBreak())
    story += main

    doc.build(story)
    print("✓ PDF saved: assets/Bannaga_CV.pdf")


if __name__ == "__main__":
    build()
