# Beatriz Skin

A custom [Hermes CLI](https://github.com/cocktailpeanut/hermes-mod) skin for **Beatriz Agent** — soft interface, sharp judgement.

## Palette

| Role | Color |
|------|-------|
| Rose | `#E8AEB7` |
| Lavender | `#C7A6D9` |
| Dusty pink | `#F3D9DC` |

## Install

1. Clone or copy `skins/beatriz-skin.yaml` to `~/.hermes/skins/`:

```bash
mkdir -p ~/.hermes/skins
cp skins/beatriz-skin.yaml ~/.hermes/skins/
```

2. Activate the skin:

```bash
# Set in ~/.hermes/config.yaml:
# display:
#   skin: beatriz-skin
```

Or use [Hermes Mod](https://github.com/cocktailpeanut/hermes-mod) for a visual editor:

```bash
npx -y hermes-mod
```

Then open `http://127.0.0.1:3210`, select **beatriz-skin** in Skin Studio, and click Activate.

## Schema

| Section | Description |
|---------|-------------|
| `colors` | 14 color keys for banner, UI, prompt, and session |
| `spinner` | Animated faces, thinking verbs, and wing brackets |
| `branding` | Agent name, welcome/goodbye messages, prompt symbol |
| `tool_prefix` | Prefix character for tool output lines |
| `tool_emojis` | Emoji overrides per tool type |
| `banner_logo` | Figlet ASCII logo with rose-to-mauve gradient |
| `banner_hero` | ASCII art avatar with color gradient |

## CI

[![validate](https://github.com/YampiSLabs/hermes-skin/actions/workflows/validate.yaml/badge.svg)](https://github.com/YampiSLabs/hermes-skin/actions/workflows/validate.yaml)

## License

MIT
