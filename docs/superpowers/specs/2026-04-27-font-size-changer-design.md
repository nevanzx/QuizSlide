# Font Size Changer for Quiz Slides

## Overview
Add adjustable font size controls to the quiz interface so users can increase or decrease text size during a quiz session.

## UI Design
- **Controls**: Two circular buttons (`A-` and `A+`) fixed in the bottom-left corner of the viewport
- **Style**: Matches the existing fullscreen button (green, circular, fixed-position, with box shadow)
- **Layout**: `A-` on the left, `A+` on the right, spaced slightly apart

## Behavior
- **Scale range**: 0.6x to 1.8x (default 1.0x)
- **Step size**: 0.1 per click
- **Clamping**: Buttons do nothing at min/max limits
- **Affected elements**: Question text, choice text, answer items, answer headings
- **Persistence**: Resets on page reload (session-only)

## Implementation

### CSS Changes (`templates/quiz.html`)
- Add `--font-scale: 1` CSS variable on `:root`
- Update `.question`, `.choice`, `.answer-item` font sizes to use `calc()` with the variable
- Add responsive breakpoints that also respect the scale variable

### JavaScript Changes (`templates/quiz.html`)
- Add `changeFontSize(delta)` function that adjusts `--font-scale` on `document.documentElement`
- Create two buttons in `window.onload` alongside the existing fullscreen button
- Position buttons at `bottom: 20px, left: 20px`

## Files Modified
- `templates/quiz.html` — CSS variables, button creation, JS function
