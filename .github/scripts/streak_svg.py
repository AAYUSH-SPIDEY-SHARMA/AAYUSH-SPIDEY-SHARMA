#!/usr/bin/env python3
"""Render the caffeine-free day counter as a self-contained SVG.

Writes dist/streak.svg, which the publish step in the workflow pushes to the
`output` branch alongside snake.svg. The README embeds it from there, so the
number refreshes daily without ever committing to main.
"""

import sys
from datetime import date, timezone, datetime, timedelta
from pathlib import Path

QUIT_DATE = date(2025, 9, 24)

CRIMSON = "#E5202B"
CARD = "#0D1117"
SILVER = "#C9D1D9"
BORDER = "#21262D"
MUTED = "#8B949E"

FONT = "'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
MONO = "'Fira Code','SF Mono',Consolas,monospace"


def render(days: int, started: date) -> str:
    since = started.strftime("%d %B %Y").lstrip("0")
    plural = "DAY" if days == 1 else "DAYS"
    # Number width varies with digit count; keep the text block left-aligned
    # against the accent bar so the layout is stable as the count grows.
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="770" height="150" viewBox="0 0 770 150" role="img" aria-label="{days} days without tea or coffee">
  <rect x="1" y="1" width="768" height="148" rx="12" fill="{CARD}" stroke="{BORDER}" stroke-width="2"/>
  <rect x="1" y="1" width="6" height="148" rx="3" fill="{CRIMSON}"/>

  <text x="44" y="86" font-family="{MONO}" font-size="62" font-weight="700" fill="{CRIMSON}">{days}</text>
  <text x="44" y="112" font-family="{FONT}" font-size="15" font-weight="600" fill="{SILVER}" letter-spacing="3">{plural} WITHOUT TEA OR COFFEE</text>

  <line x1="392" y1="38" x2="392" y2="112" stroke="{BORDER}" stroke-width="2"/>

  <text x="428" y="62" font-family="{FONT}" font-size="14" fill="{MUTED}" letter-spacing="2">CLEAN SINCE</text>
  <text x="428" y="88" font-family="{FONT}" font-size="19" font-weight="600" fill="{SILVER}">{since}</text>
  <text x="428" y="112" font-family="{FONT}" font-size="13" fill="{MUTED}">still counting — the cup waits until the goal is met</text>
</svg>
"""


def main() -> int:
    # Use IST so the counter ticks over on Aayush's day, not UTC midnight.
    today = (datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)).date()
    days = (today - QUIT_DATE).days
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "dist/streak.svg")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(days, QUIT_DATE), encoding="utf-8")
    print(f"wrote {out} — {days} days since {QUIT_DATE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
