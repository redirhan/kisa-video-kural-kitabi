#!/usr/bin/env python3
"""Türkçe TTS için okunuş düzeltici: metindeki kısaltma, özel ad ve birimleri glossary_tr.tsv'deki
okunuşlarla değiştirir. Ekranda gösterilecek metin değişmez; bu çıktı sadece seslendirme motoruna gider.

    python3 respell.py "DNA'nın yapısını Watson ve Crick 1953'te buldu; 5 mg yeterli."
    echo "metin" | python3 respell.py -
    python3 respell.py --check          # sözlüğün biçimini doğrular

Kurallar: uzun terimler önce; kısaltma (abbr) ve birim (unit) büyük/küçük harfe duyarlı; birim sadece
bir sayıdan sonra; kesme işaretli ekler korunur (DNA'nın -> de ne a'nın). Sadece Python standart kütüphanesi.
"""

import re
import sys
from pathlib import Path

GLOSSARY = Path(__file__).with_name("glossary_tr.tsv")
KINDS = {"abbr", "name", "term", "unit", "translate"}


def load(path: Path = GLOSSARY):
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 4 or not cols[0] or not cols[1] or cols[2] not in KINDS:
            raise ValueError(f"{path.name}:{n}: bozuk satır: {line!r}")
        rows.append({"written": cols[0], "spoken": cols[1], "kind": cols[2], "field": cols[3]})
    return rows


def respell(text: str, rows=None) -> str:
    rows = rows if rows is not None else load()
    for r in sorted(rows, key=lambda r: -len(r["written"])):
        w = re.escape(r["written"])
        flags = 0 if r["kind"] in ("abbr", "unit") else re.IGNORECASE
        if r["kind"] == "unit":
            pat = rf"(?<=\d)(\s?){w}(?![\w])"
            text = re.sub(pat, lambda m: f" {r['spoken']}", text, flags=flags)
        else:
            pat = rf"(?<![\w]){w}(?![\w])"
            text = re.sub(pat, r["spoken"], text, flags=flags)
    return text


def main(argv) -> int:
    if argv and argv[0] == "--check":
        rows = load()
        dup = {r["written"] for r in rows if [x["written"] for x in rows].count(r["written"]) > 1}
        print(f"{len(rows)} terim, tekrar eden: {sorted(dup) or 'yok'}")
        return 1 if dup else 0
    text = sys.stdin.read() if (not argv or argv[0] == "-") else " ".join(argv)
    print(respell(text))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
