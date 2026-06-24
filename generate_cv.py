"""
Clean professional CV — Bannaga Altieb Abdul Muhsin
Standard ATS-friendly single-column format, light background.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether

W, H = A4

# ── Colours ───────────────────────────────────────────────────────────────────
ACCENT  = colors.HexColor("#1e40af")   # professional navy blue
DARK    = colors.HexColor("#111827")
MID     = colors.HexColor("#374151")
GREY    = colors.HexColor("#6b7280")
LIGHT   = colors.HexColor("#f3f4f6")
WHITE   = colors.white
LINE    = colors.HexColor("#d1d5db")

# ── Styles ────────────────────────────────────────────────────────────────────
NAME    = ParagraphStyle("name",    fontName="Helvetica-Bold",    fontSize=22, textColor=DARK,   leading=26, alignment=TA_CENTER)
TITLE   = ParagraphStyle("title",   fontName="Helvetica",         fontSize=11, textColor=ACCENT, leading=14, alignment=TA_CENTER)
CRED    = ParagraphStyle("cred",    fontName="Helvetica",         fontSize=8.5,textColor=GREY,   leading=12, alignment=TA_CENTER)
CONTACT = ParagraphStyle("contact", fontName="Helvetica",         fontSize=8,  textColor=MID,    leading=12, alignment=TA_CENTER)
SECHDR  = ParagraphStyle("sechdr",  fontName="Helvetica-Bold",    fontSize=11, textColor=ACCENT, leading=15, spaceAfter=2)
BODY    = ParagraphStyle("body",    fontName="Helvetica",         fontSize=9.5,textColor=MID,    leading=14, alignment=TA_JUSTIFY)
BULLET  = ParagraphStyle("bullet",  fontName="Helvetica",         fontSize=9.5,textColor=MID,    leading=14, leftIndent=12, firstLineIndent=-6)
JOB_T   = ParagraphStyle("jobt",   fontName="Helvetica-Bold",    fontSize=10.5,textColor=DARK,  leading=14)
JOB_C   = ParagraphStyle("jobc",   fontName="Helvetica-Bold",    fontSize=9.5,textColor=ACCENT, leading=13)
JOB_D   = ParagraphStyle("jobd",   fontName="Helvetica-Oblique", fontSize=9,  textColor=GREY,   leading=12)
SMALL   = ParagraphStyle("small",  fontName="Helvetica",         fontSize=9,  textColor=MID,    leading=13)
BOLD    = ParagraphStyle("bold",   fontName="Helvetica-Bold",    fontSize=9.5,textColor=DARK,   leading=14)
QUOTE   = ParagraphStyle("quote",  fontName="Helvetica-Oblique", fontSize=8,  textColor=GREY,   leading=12, alignment=TA_CENTER)
SKILL_L = ParagraphStyle("skl",    fontName="Helvetica-Bold",    fontSize=9,  textColor=DARK,   leading=13)
SKILL_V = ParagraphStyle("skv",    fontName="Helvetica",         fontSize=9,  textColor=MID,    leading=13)

def sp(h=4): return Spacer(1, h)
def hr(): return HRFlowable(width="100%", thickness=0.5, color=LINE, spaceAfter=5, spaceBefore=5)
def section(title):
    return [
        Paragraph(title.upper(), SECHDR),
        HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=6, spaceBefore=0),
    ]

# ── Build ─────────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        "assets/Bannaga_CV.pdf",
        pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=15*mm, bottomMargin=15*mm,
    )

    story = []

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION BUILDERS (assembled in old-CV order at the end)
    # ══════════════════════════════════════════════════════════════════════════
    header = []
    summary = []
    overview = []
    ai_dev = []
    accomplish = []
    experience_sec = []
    projects_sec = []
    education_sec = []
    skills_sec = []
    certs_sec = []
    mla_sec = []
    hobbies_sec = []
    footer = []

    # ── NAME & CONTACT ────────────────────────────────────────────────────────
    header.append(Paragraph("Bannaga Altieb Abdul Muhsin", NAME))
    header.append(sp(4))
    header.append(Paragraph("Electrical Project Engineer  —  Riyadh, Saudi Arabia", TITLE))
    header.append(sp(3))
    header.append(Paragraph(
        "Telecom &amp; industrial passive infrastructure  ·  Energy optimization  ·  O&amp;M excellence", CRED))
    header.append(sp(5))
    header.append(Paragraph("CEM®  ·  CMVP®  ·  LEED Green Associate", CRED))
    header.append(sp(6))
    header.append(Paragraph(
        "+966 54 296 6343  |  eng.altieb@gmail.com  |  linkedin.com/in/bannaga-abdalmuhsin  |  "
        "x.com/AltiebBannaga  |  instagram.com/bannga.altieb  |  tiktok.com/@bannagaaltieb94  |  "
        "facebook.com/bannga.altieb",
        CONTACT))
    header.append(sp(8))
    header.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=10, spaceBefore=0))

    # ── PROFESSIONAL SUMMARY ──────────────────────────────────────────────────
    summary += section("Professional Summary")
    summary.append(Paragraph(
        "Certified Energy Manager (CEM®) and Certified Measurement &amp; Verification Professional (CMVP®) with "
        "14+ years of experience in electrical and energy engineering. Specializes in project management, telecom "
        "power systems, energy-efficient solutions, and technical operations across diverse infrastructure. "
        "Expertise spans data collection, energy analysis, facilities management, AI-driven dashboards, and "
        "structured reporting. Delivered innovative, reliable, and performance-driven engineering solutions across "
        "telecom, power generation, and industrial sectors. Holds a B.Sc. in Electronic Control Engineering with "
        "additional certifications in LEED Green Associate and SCADA systems. Fluent in English and Arabic.",
        BODY))
    summary.append(sp(10))

    # ── OVERVIEW / KEY METRICS ────────────────────────────────────────────────
    overview += section("Overview")
    metrics_data = [[
        Paragraph("14+\nYears Experience", ParagraphStyle("m", fontName="Helvetica-Bold", fontSize=10,
            textColor=ACCENT, leading=14, alignment=TA_CENTER)),
        Paragraph("15+\nCertifications &amp; Training", ParagraphStyle("m", fontName="Helvetica-Bold", fontSize=10,
            textColor=ACCENT, leading=14, alignment=TA_CENTER)),
        Paragraph("60+\nMV/LV Assets Commissioned", ParagraphStyle("m", fontName="Helvetica-Bold", fontSize=10,
            textColor=ACCENT, leading=14, alignment=TA_CENTER)),
        Paragraph("18%\nUtility Cost Reduction", ParagraphStyle("m", fontName="Helvetica-Bold", fontSize=10,
            textColor=ACCENT, leading=14, alignment=TA_CENTER)),
    ]]
    metrics = Table(metrics_data, colWidths=[(W - 36*mm) / 4] * 4)
    metrics.setStyle(TableStyle([
        ("ALIGN",        (0,0), (-1,-1), "CENTER"),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("BACKGROUND",   (0,0), (-1,-1), LIGHT),
        ("TOPPADDING",   (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0), (-1,-1), 6),
        ("GRID",         (0,0), (-1,-1), 0.5, LINE),
        ("ROUNDEDCORNERS",(0,0),(-1,-1), [4,4,4,4]),
    ]))
    overview.append(metrics)
    overview.append(sp(10))

    # ── EXPERIENCE ────────────────────────────────────────────────────────────
    experience_sec += section("Experience")

    experience = [
        ("2019 – Present", "Electrical Project Engineer", "ACES  |  Riyadh, Saudi Arabia", [
            "Serve as Energy Manager and efficiency designer across STC COW and Mobily ENM managed networks.",
            "O&amp;M Engineer for Mobily ENM Managed Services — full facility operations, CAFM/BMS integration, and KPI reporting.",
            "O&amp;M Engineer for STC COW Managed Services — operations and maintenance across 600+ nationwide telecom sites.",
            "Designed and delivered multi-phase energy optimization programs achieving up to 18% reduction in utility costs.",
            "Developed Python-based automation for energy performance reporting and ML-based anomaly detection alerts.",
            "Built AI-driven Energy &amp; Environmental Dashboard for CO2 footprint monitoring across all STC COW sites.",
            "Authored comprehensive technical troubleshooting and preventive maintenance documentation.",
            "Mentored junior engineers and standardized field engineering practices across all sites.",
        ]),
        ("2018 – 2019", "Electrical Project Engineer", "Absar  |  Riyadh, Saudi Arabia", [
            "Executed SEC unified-contract builds for 60+ MV/LV electrical assets including RMUs, transformers, and LV switchgear.",
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
            "Developed operational procedures, safety documentation, and switching routines.",
        ]),
    ]

    for date, title, company, bullets in experience:
        job_header = Table([[
            Paragraph(title, JOB_T),
            Paragraph(date, ParagraphStyle("dr", fontName="Helvetica-Oblique", fontSize=8.5,
                textColor=GREY, leading=12, alignment=TA_RIGHT)),
        ]], colWidths=[(W - 36*mm) * 0.68, (W - 36*mm) * 0.32])
        job_header.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ]))
        experience_sec.append(KeepTogether([
            job_header,
            Paragraph(company, JOB_C),
            sp(3),
            *[Paragraph(f"• {b}", BULLET) for b in bullets],
            sp(8),
        ]))

    # ── KEY PROJECTS ──────────────────────────────────────────────────────────
    projects_sec += section("Key Projects")

    projects = [
        ("STC COW Network — O&amp;M &amp; Energy Optimization",
         "End-to-end operations and maintenance for 600+ telecom sites nationwide. Delivered systematic energy "
         "auditing, SCADA oversight, and multi-phase optimization achieving up to 18% utility cost reduction."),
        ("Mobily ENM Managed Services",
         "Full O&amp;M and facility operations for Mobily's ENM managed services network including CAFM/BMS "
         "integration, outage prevention, and structured performance reporting."),
        ("Mobily Data Center Energy Audit",
         "Comprehensive energy audit of critical data center infrastructure delivering measurable PUE improvements "
         "and quantified energy savings certified under CEM® / CMVP® methodology."),
        ("SEC Unified Contract — MV/LV Commissioning",
         "Complete installation and commissioning of 60+ MV/LV electrical assets (RMUs, transformers, mini-pillars, "
         "LV switchgear) with full SCADA integration and zero-defect SEC handover documentation."),
        ("PP12 Thermal Generation Plant — 200 MW Operations",
         "Day-to-day operations including 11kV switching, safety routines, wastewater treatment management, and "
         "DCS-based environmental monitoring for a 200 MW thermal power station."),
        ("AI CO2 &amp; Energy Dashboard",
         "Built ML-based anomaly detection and CO2 footprint tracking dashboards for nationwide STC COW telecom "
         "deployments using Python, Power BI, SQL Server, and DAX — enabling real-time environmental governance."),
    ]

    for title, desc in projects:
        projects_sec.append(KeepTogether([
            Paragraph(f"<b>{title}</b>", SMALL),
            Paragraph(desc, BODY),
            sp(5),
        ]))
    projects_sec.append(sp(4))

    # ── KEY ACCOMPLISHMENTS ───────────────────────────────────────────────────
    accomplish += section("Key Accomplishments")
    accomplishments = [
        "Reduced nationwide telecom site utility costs by up to <b>18%</b> through multi-phase energy optimization programs.",
        "Delivered uninterrupted O&amp;M coverage for STC COW &amp; Mobily ENM with proactive outage prevention strategies.",
        "Authored troubleshooting guides and automation routines reducing incident resolution time by <b>30%</b>.",
        "Commissioned <b>60+ MV/LV assets</b> under SEC unified contracts with full SCADA integration and zero-defect handover.",
        "Developed an AI-driven Energy &amp; Environmental Dashboard tracking real-time CO2 emissions and power efficiency.",
        "Applied Power BI, Python, and SQL Server to model operational trends across 600+ multi-site telecom networks.",
        "Version-controlled all engineering documentation and templates using Git/GitHub workflows.",
    ]
    for a in accomplishments:
        accomplish.append(Paragraph(f"• {a}", BULLET))
        accomplish.append(sp(2))
    accomplish.append(sp(8))

    # ── AI & DEVELOPMENT ──────────────────────────────────────────────────────
    ai_dev += section("AI & Development")
    ai_dev.append(Paragraph("<b>AI &amp; Automation</b>", BOLD))
    for b in [
        "Designed Python-based automation to streamline energy performance reporting and KPI tracking across sites.",
        "Developed machine-learning-based anomaly detection alerts for telecom site power consumption behavior.",
        "Built governance-ready Energy &amp; Environmental dashboards for real-time CO2 footprint monitoring.",
        "Applied Power BI, SQL Server, and DAX to model and visualize operational trends across multi-site networks.",
    ]:
        ai_dev.append(Paragraph(f"• {b}", BULLET))
    ai_dev.append(sp(4))
    ai_dev.append(Paragraph("<b>Development &amp; Tools</b>", BOLD))
    for b in [
        "Created reusable troubleshooting guides and diagnostic scripts for SCADA / PLC / DCS systems.",
        "Documented API-style checklists to standardize field data capture and site integrations.",
        "Version-controlled documentation and engineering templates using Git/GitHub workflows.",
    ]:
        ai_dev.append(Paragraph(f"• {b}", BULLET))
    ai_dev.append(sp(10))

    # ── SKILLS ────────────────────────────────────────────────────────────────
    skills_sec += section("Skills")

    skill_groups = [
        ("Power Systems & Electrical",
         "HV/MV/LV Engineering · SCADA / DCS / PLC / RTU · Energy Auditing (CEM®) · "
         "Commissioning & Testing · Power System Protection · 11kV Switching · Transformer & RMU Installation"),
        ("AI, Data & Analytics",
         "Power BI / DAX · Python / Machine Learning · SQL Server · Data Dashboards · "
         "KPI Reporting · CO2 Monitoring · Anomaly Detection"),
        ("Software & Development",
         "React / Next.js · TypeScript · Tailwind CSS · Node.js · PostgreSQL · GraphQL · Git/GitHub"),
        ("Design & Prototyping",
         "Figma (96%) · Power BI Visuals (92%) · UI Systems (94%) · Dashboard Design · Wireframing"),
        ("Energy & Facilities",
         "Energy Management (CEM®/CMVP®) · CAFM · BMS Integration · Facility Operations · "
         "PUE Optimization · Preventive Maintenance · LEED Green Associate"),
        ("Tools & Platforms",
         "Microsoft Office Suite · Power BI · SQL Server · Figma · SCADA Platforms · Git/GitHub · Python"),
    ]

    for label, value in skill_groups:
        row = Table([[
            Paragraph(label, SKILL_L),
            Paragraph(value, SKILL_V),
        ]], colWidths=[(W - 36*mm) * 0.28, (W - 36*mm) * 0.72])
        row.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("LINEBELOW", (0,0), (-1,-1), 0.3, LINE),
        ]))
        skills_sec.append(row)
    skills_sec.append(sp(10))

    # ── EDUCATION ─────────────────────────────────────────────────────────────
    education_sec += section("Education")
    edu = Table([[
        Paragraph("B.Sc. Electronic Engineering (Control)", JOB_T),
        Paragraph("2007 – 2012", ParagraphStyle("dr", fontName="Helvetica-Oblique", fontSize=8.5,
            textColor=GREY, leading=12, alignment=TA_RIGHT)),
    ]], colWidths=[(W - 36*mm) * 0.68, (W - 36*mm) * 0.32])
    edu.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    education_sec.append(edu)
    education_sec.append(Paragraph("El Neelain University — Khartoum, Sudan", JOB_C))
    education_sec.append(sp(10))

    # ── CERTIFICATIONS ────────────────────────────────────────────────────────
    certs_sec += section("Certifications &amp; Training")
    certs = [
        ("CMVP®", "Certified Measurement &amp; Verification Professional"),
        ("CEM®", "Certified Energy Manager"),
        ("ML", "Machine Learning with Python"),
        ("Power BI", "Power BI Essential Training"),
        ("LEED", "LEED Green Associate (Cert Prep)"),
        ("Excel", "Learning Excel: Data Analysis"),
        ("QE", "Quality Engineering"),
        ("SCADA", "SCADA / PLC / DCS / RTU Systems"),
        ("Data Sci", "The Non-Technical Skills of Effective Data Scientists"),
    ]
    cert_rows = []
    for badge, name in certs:
        cert_rows.append([
            Paragraph(badge, SKILL_L),
            Paragraph(name, SKILL_V),
        ])
    cert_table = Table(cert_rows, colWidths=[(W - 36*mm) * 0.15, (W - 36*mm) * 0.85])
    cert_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, LINE),
    ]))
    certs_sec.append(cert_table)
    certs_sec.append(sp(6))

    # ── MEMBERSHIPS, LANGUAGES, AVAILABILITY ──────────────────────────────────
    def mini_hdr(text):
        return [
            Paragraph(text.upper(), SECHDR),
            HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=5, spaceBefore=0),
        ]

    col_members = [
        *mini_hdr("Memberships"),
        Paragraph("Saudi Council of Engineers (SCE)", SMALL),
        Paragraph("Sudanese Engineers Association (SEA)", SMALL),
    ]
    col_langs = [
        *mini_hdr("Languages"),
        Paragraph("Arabic — Native", SMALL),
        Paragraph("English — Professional", SMALL),
    ]
    col_avail = [
        *mini_hdr("Availability"),
        Paragraph("Sun–Thu: 8:00 AM – 6:00 PM", SMALL),
        Paragraph("Weekends: On-call for urgent needs", SMALL),
        Paragraph("Open to short-notice regional travel", SMALL),
    ]

    usable = W - 36*mm
    bottom_table = Table(
        [[col_members, col_langs, col_avail]],
        colWidths=[usable * 0.32, usable * 0.30, usable * 0.38],
    )
    bottom_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (0,-1), 0),
        ("LEFTPADDING", (1,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (-1,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    mla_sec.append(KeepTogether(bottom_table))
    mla_sec.append(sp(6))

    # ── HOBBIES ───────────────────────────────────────────────────────────────
    hobbies_sec += section("Hobbies & Interests")
    hobbies = ["Electrical Power Systems", "Energy Efficiency", "Automation & Control",
               "Data Analysis & Visualization", "Innovation & New Technologies", "AI & Machine Learning"]
    hobbies_sec.append(Paragraph("  ·  ".join(hobbies), BODY))
    hobbies_sec.append(sp(6))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    footer.append(HRFlowable(width="100%", thickness=1, color=LINE, spaceAfter=6, spaceBefore=0))
    footer.append(Paragraph(
        '"You never change things by fighting the existing reality. '
        'To change something, build a new model that makes the old one obsolete."  — R. Buckminster Fuller',
        QUOTE))
    footer.append(sp(2))
    footer.append(Paragraph(
        "© 2025 Eng. Bannaga Altieb Abdul Muhsin  ·  eng.altieb@gmail.com  ·  +966 54 296 6343",
        QUOTE))

    # ══════════════════════════════════════════════════════════════════════════
    # ASSEMBLE in the same order as the old CV
    # ══════════════════════════════════════════════════════════════════════════
    story += header
    story += summary
    story += overview
    story += ai_dev
    story += accomplish
    story += experience_sec
    story += projects_sec
    story += education_sec
    story += skills_sec
    story += certs_sec
    story += mla_sec
    story += hobbies_sec
    story += footer

    doc.build(story)
    print("✓ PDF saved: assets/Bannaga_CV.pdf")


if __name__ == "__main__":
    build()
