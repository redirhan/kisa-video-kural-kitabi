# Short-Form Rulebook, Turkish edition (free Claude Code skill pack)

**Measured** rules for Reels, Shorts and TikTok editing, written in Turkish. The numbers come from
measuring 52 viral short videos (Turkish and English) and from what 12 editing tutorials agree on.
Once installed, Claude Code uses them whenever it plans, builds or reviews a short-form edit.

Made by Redirhan Labs. Free, MIT licence.

## What's inside

| Folder | What it does |
|---|---|
| `skills/kisa-video-kurallari/` | The editing rulebook: take selection, cuts on word boundaries, caption size and height, emphasis, zooms, SFX and music levels, the first 3 seconds, endings, banned moves, 4 style kits |
| `skills/referanstan-konsepte/` | "Make something like this" protocol: download the reference, measure it, break it down shot by shot on 5 aspects, offer 2–3 concepts, build a 10–15 s sample first, "slideshow risk" check |
| `bonus/tts-okunus-sozlugu/` | Turkish TTS pronunciation glossary, 181 terms (DNA → "de ne a", Watson → "vatsın", 5 mg → "5 miligram") + `respell.py` |

A few of the numbers:
- Turkish talking-head captions sit at ~0.67 of the frame height (English: 0.56).
- In Turkish videos the median first cut is at 3.6 s: a title box, not cutting, carries the hook.
- Half of the top talking heads have no music bed; where there is one it sits ~16 LU under the voice.
- 8 of 14 top talking heads put no sound effect on any cut.

## Install

```bash
mkdir -p ~/.claude/skills
cp -R skills/kisa-video-kurallari skills/referanstan-konsepte ~/.claude/skills/
cp -R bonus/tts-okunus-sozlugu ~/.claude/skills/        # optional
```

Restart Claude Code and ask, for example, *"Plan a 45 s reel from this talking-head video"* or
*"Look at this reel and let's make one like it for my café: <link>"*. The skills load by themselves
(they are written in Turkish; Claude reads them fine in any language).

Requirements: the rulebook is plain text. The reference protocol's measurements suggest `yt-dlp`,
`ffmpeg` and optionally whisper (e.g. whisper.cpp). The glossary helper needs only Python 3.

## Want more? Panel TR

Test your edit through Turkish viewers' eyes before you post: **Panel TR** is a synthetic focus group
of evidence-based Turkish personas split by age, city size and Instagram use. It answers "how many
stop, how many scroll past, how many would DM?" with counts. → free Lite edition: https://github.com/redirhan/panel-tr-lite

## Licence

MIT, see `LICENSE`. The reference protocol's workflow idea is inspired by OpenMontage (AGPL-3.0); no
code was taken from it.
