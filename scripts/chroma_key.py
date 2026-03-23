#!/usr/bin/env python3
"""
Chroma key removal with green spill/despill.
Works on any image with a green (#00FF00) background.
Usage:
  python3 chroma_key.py input.png output.png
  python3 chroma_key.py --all   # process all *-raw.png in public/img/
"""

import sys
from pathlib import Path
import numpy as np
from PIL import Image
from scipy.ndimage import binary_dilation


def chroma_remove(input_path: Path, output_path: Path):
    """Remove green chroma key background with despill."""
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img).astype(np.float64)

    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]

    # 1. Hard removal: obvious green pixels
    hard_green = (g > 150) & (r < 100) & (b < 100)
    data[hard_green] = [0, 0, 0, 0]

    # 2. Soft green spill: pixels where green is dominant
    green_ratio = g / (r + g + b + 1)
    green_spill = (green_ratio > 0.45) & (g > 80) & ~hard_green

    # Despill: reduce green channel to avg of r,b
    avg_rb = (r + b) / 2
    data[green_spill, 1] = avg_rb[green_spill]

    # Reduce opacity on strongly green-tinted edge pixels
    strong_spill = (green_ratio > 0.55) & ~hard_green
    spill_strength = np.clip((green_ratio[strong_spill] - 0.45) / 0.3, 0, 1)
    data[strong_spill, 3] = data[strong_spill, 3] * (1 - spill_strength * 0.5)

    # 3. Fringe: despill and soften 2px around hard green edge
    fringe = binary_dilation(hard_green, iterations=2) & ~hard_green
    data[fringe, 1] = np.minimum(data[fringe, 1], (data[fringe, 0] + data[fringe, 2]) / 2)
    data[fringe, 3] = data[fringe, 3] * 0.85

    result = Image.fromarray(data.astype(np.uint8))
    result.save(str(output_path))
    return hard_green.sum()


def has_green_bg(img_path: Path, threshold=0.05) -> bool:
    """Check if image has significant green chroma key background."""
    img = Image.open(img_path).convert("RGB")
    data = np.array(img)
    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    green_pixels = ((g > 150) & (r < 100) & (b < 100)).sum()
    total = data.shape[0] * data.shape[1]
    return (green_pixels / total) > threshold


def main():
    if len(sys.argv) >= 3 and sys.argv[1] != "--all":
        # Single file mode
        inp, out = Path(sys.argv[1]), Path(sys.argv[2])
        removed = chroma_remove(inp, out)
        print(f"✅ {out.name} — {removed:,} green pixels removed")
        return

    # Batch mode: process all raw images that have green backgrounds
    img_dir = Path(__file__).parent.parent / "public" / "img"
    raw_files = sorted(img_dir.glob("*-raw.png"))

    if not raw_files:
        print("No *-raw.png files found.")
        return

    print(f"Scanning {len(raw_files)} raw images for green backgrounds...\n")

    for raw in raw_files:
        name = raw.name.replace("-raw.png", "")
        output = img_dir / f"{name}.png"

        if has_green_bg(raw):
            removed = chroma_remove(raw, output)
            print(f"  ✅ {name}.png — chroma key ({removed:,} green px removed)")
        else:
            print(f"  ⏭  {name} — no green background, skipping")


if __name__ == "__main__":
    main()
