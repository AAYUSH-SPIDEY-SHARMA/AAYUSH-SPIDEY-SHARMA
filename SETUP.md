# Setup

## Repo structure

Everything lives in the profile repo `AAYUSH-SPIDEY-SHARMA/AAYUSH-SPIDEY-SHARMA`:

```
.
├── README.md
├── assets/
│   ├── banner.png        # hero image
│   ├── divider.png       # web section divider
│   ├── spider-mark.png   # crimson spider glyph
│   ├── avatar.png        # Quick Intro portrait
│   ├── moment.png        # image for the Unforgettable Moment section
│   ├── card-01.png       # THE GAMER
│   ├── card-02.png       # THE AI ENGINEER
│   ├── card-03.png       # THE BALLER
│   └── straw-hat.png
└── .github/
    ├── scripts/
    │   └── streak_svg.py # renders the caffeine-free counter
    └── workflows/
        └── snake.yml     # builds snake.svg + streak.svg daily
```

## Things still to fill in

| Where | Placeholder | Replace with |
|---|---|---|
| Projects → AimPeak | `live link coming soon` | the deployed URL |
| Projects → DOTCODE | `live link coming soon` | the deployed URL (and a real description) |

Each has an HTML comment next to it showing the exact replacement.
The Get in Touch row is fully filled in.

To swap the Unforgettable Moment image, just overwrite `assets/moment.png`.
No README edit needed.

## The daily workflow

`.github/workflows/snake.yml` runs at 00:00 UTC (and on every push to `main`).
It does two things in one job:

1. `Platane/snk` renders the contribution snake to `dist/snake.svg`
2. `.github/scripts/streak_svg.py` renders the tea/coffee day counter to
   `dist/streak.svg`, counting from `QUIT_DATE` in that script

Both files are then published to the `output` branch, and the README embeds them
from `raw.githubusercontent.com/.../output/`.

**Why one job:** the publish step replaces the whole `output` branch, so a second
workflow writing there would delete the other file. Anything new that needs
publishing must be generated into `dist/` in this same job.

**Why checkout runs first:** `actions/checkout` cleans the workspace, so running
it after the generators would wipe `dist/`.

One-time repo settings, if the workflow ever fails to push:
Settings → Actions → General → Workflow permissions → *Read and write permissions*.

## Theme reference

| Token | Hex | Used for |
|---|---|---|
| Crimson | `#E5202B` | accents, labels, graph lines |
| Card black | `#0D1117` | card backgrounds |
| Web silver | `#C9D1D9` | body text on cards |
| Border | `#21262D` | card borders |
| Muted | `#8B949E` | secondary text |

Search-and-replace `E5202B` to reskin the page in one pass. The counter SVG uses
the same tokens, near the top of `streak_svg.py`.

## Note on third-party card services

`github-readme-stats.vercel.app` was dropped from this README — the public
instance is heavily rate-limited and was returning HTTP 503 for every request,
including for public repos, which is what broke the old pin cards and stats card.
The Projects section is now hand-written HTML with no external dependency.

If you ever want those cards back, deploy your own instance of
github-readme-stats to Vercel and point the URLs at it rather than the shared one.

`streak-stats.demolab.com` was dropped for the same reason. The URL itself
answered 200 to a direct request, but GitHub's image proxy (camo) has a short
fetch timeout and the shared demolab instance is slow enough to blow through it,
so the card kept rendering as a broken-image icon on the live profile. Same fix
if you want it back: self-host it.

Contribution Signal now holds only the activity graph and the snake — the snake
is served from this repo's own `output` branch, so it can't be taken down by
someone else's rate limit.
