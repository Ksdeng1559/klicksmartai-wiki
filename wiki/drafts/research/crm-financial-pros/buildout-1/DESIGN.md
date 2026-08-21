---
name: clientflow-design
description: Design tokens for ClientFlow — AI Intake Fast Lane landing page and product spec.
---

# Design System — ClientFlow

## Color Palette

| Token | Hex | Use |
|-------|-----|-----|
| `--bg` | `#F8FAFC` | Page background |
| `--surface` | `#FFFFFF` | Cards, panels |
| `--surface-alt` | `#F1F5F9` | Alternate sections |
| `--border` | `#E2E8F0` | Dividers, card borders |
| `--text-primary` | `#0F172A` | Headlines, body |
| `--text-secondary` | `#475569` | Subheadings, supporting text |
| `--text-muted` | `#94A3B8` | Captions, labels |
| `--accent` | `#0D9488` | Teal — CTAs, links, accent marks |
| `--accent-hover` | `#0F766E` | CTA hover state |
| `--accent-light` | `#CCFBF1` | Accent tints, badges |
| `--navy` | `#0F172A` | Hero background, dark sections |
| `--navy-light` | `#1E293B` | Dark surface variants |

## Typography

| Role | Font | Fallback |
|------|------|----------|
| Display | Inter | system-ui, sans-serif |
| Body | Inter | system-ui, sans-serif |

**Scale:**
- Display: 56px / 700 / -0.02em
- H1: 40px / 700 / -0.01em
- H2: 28px / 600 / 0
- H3: 20px / 600 / 0
- Body: 16px / 400 / 0
- Small: 14px / 400 / 0
- Caption: 12px / 500 / 0.02em uppercase

## Layout

- Max width: 1120px
- Section padding: 96px vertical (48px mobile)
- Grid: 12-column, 24px gutter
- Card padding: 32px
- Border radius: 12px (cards), 8px (buttons), 6px (inputs)

## Depth & Elevation

Minimal — border-based separation preferred. Subtle shadow on cards only.
- Card: `box-shadow: 0 1px 3px rgba(0,0,0,0.08)`

## Components

**Button primary:** bg accent, white text, 12px 24px padding, 8px radius, font-weight 600
**Button secondary:** bg white, border `--border`, `--text-primary`
**Card:** white bg, 1px border `--border`, 12px radius, 32px padding
**Badge:** bg accent-light, accent text, 6px radius

## Responsive

- Desktop: 1120px max
- Tablet: 768px
- Mobile: 375px