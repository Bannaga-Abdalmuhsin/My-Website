---
name: reportlab multi-page sidebar layout
description: How to build a colored-sidebar resume/CV in reportlab that flows across multiple pages without LayoutError
---

# Multi-page sidebar (two-column) layout in reportlab

**Rule:** Never put a whole sidebar+main as one Table row with two big cells — a single
table row cannot split across pages and raises `LayoutError`.

**Working pattern:** `BaseDocTemplate` with TWO `PageTemplate`s:
- page 1 template = two Frames `[sidebar_frame, main_frame]`; an `onPage` canvas
  callback paints the colored sidebar rectangle + header block + photo/name.
- later template = main-frame-only; its own `onPage` repaints the (empty) colored
  sidebar background for visual continuity.
- Story order: `[NextPageTemplate("later"), *sidebar_flowables, FrameBreak(), *main_flowables]`.
  Sidebar content fills frame 1, `FrameBreak` jumps to main frame, main overflows onto
  "later" pages. Sidebar content must FIT on page 1 (its frame only exists there).

**Why:** reportlab fills frames sequentially; parallel columns across pages aren't native.
Painting the sidebar via `onPage` (not flowables) keeps the band on every page.

**Gotcha:** Do NOT wrap a list containing a `Table` (e.g. a skill bar) in `KeepTogether`
and place it inside another Table cell — height computes as ~16777215 and throws
`LayoutError ... too large`. Instead return a plain list of flowables `[label, spacer,
bar_table, spacer]` directly as the cell content (cells accept flowable lists).

**Skill bar:** a 1-row 2-col Table with `colWidths=[w*pct, w*(1-pct)]`, `rowHeights=[6]`,
backgrounds = accent + light-gray track, zero padding.

**Verify visually:** no pymupdf/fitz here; use `pdftoppm -png -r 90 file.pdf /tmp/out`
then read the PNGs. `pdfinfo` for page count.
