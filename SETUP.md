# Setup — 10 minutes

## 1. Repo structure

Everything goes in your **profile repo**: `AAYUSH-SPIDEY-SHARMA/AAYUSH-SPIDEY-SHARMA`

```
.
├── README.md
├── assets/
│   ├── banner.png        # hero image
│   ├── divider.png       # web section divider
│   ├── spider-mark.png   # crimson spider glyph
│   ├── avatar.png        # about-me portrait
│   ├── card-01.png       # THE BUILDER
│   ├── card-02.png       # THE RESEARCHER
│   ├── card-03.png       # THE COMPETITOR
│   └── straw-hat.png
└── .github/
    └── workflows/
        └── snake.yml
```

```bash
git add .
git commit -m "Redesign profile README"
git push
```

## 2. Placeholders to replace

| Where | Placeholder | Replace with |
|---|---|---|
| Featured Work | `REPO_NAME_2` | your second-best repo name |
| Featured Work | `### Next Project` block | real project name + description |
| Get in Touch | `YOUR_HANDLE`, `YOUR_EMAIL`, `YOUR_ID`, `YOUR_PORTFOLIO` | your actual links |
| Behind the Mask | the YAML block | anything that has changed |

Delete any social badge you don't use — an empty link looks worse than no link.

## 3. Contribution snake

The snake image is blank until the action runs once.

1. Put `snake.yml` in `.github/workflows/`
2. Repo → **Settings → Actions → General → Workflow permissions** → *Read and write permissions*
3. Repo → **Actions** tab → *Generate contribution snake* → **Run workflow**

It regenerates daily after that. If you'd rather not run an action, delete the snake `<img>` line from the Contribution Signal section.

## 4. Theme reference

If you swap colours later, these are the four values used throughout:

| Token | Hex | Used for |
|---|---|---|
| Crimson | `#E5202B` | accents, labels, graph lines |
| Card black | `#0D1117` | every stats card background |
| Web silver | `#C9D1D9` | body text on cards |
| Border | `#21262D` | card borders |

Search-and-replace `E5202B` to reskin the whole page in one pass (e.g. `00E5FF` for a cyber-blue variant, `7C3AED` for violet).

## 5. Optional polish

- Pin 6 repos on your profile — the README points at them, so make them count.
- Add real numbers to project descriptions (latency, accuracy, users). Specifics beat adjectives.
- If a section ever feels like filler, delete it. Short and sharp reads more senior than long.
