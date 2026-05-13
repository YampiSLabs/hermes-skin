# Beatriz Skin

A custom [Hermes CLI](https://github.com/cocktailpeanut/hermes-mod) skin for **Beatriz Agent** — purple cyberpunk audit theme.

## Preview

![](https://img.shields.io/badge/theme-purple%20cyberpunk-%23A855F7)

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
| `banner_logo` | Figlet-generated ASCII logo with color tags |
| `banner_hero` | Braille art hero image with color gradient |

## CI

[![validate](https://github.com/YampiSLabs/hermes-skin/actions/workflows/validate.yaml/badge.svg)](https://github.com/YampiSLabs/hermes-skin/actions/workflows/validate.yaml)

## License

MIT
