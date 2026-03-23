#!/usr/bin/env python3
"""
Aura Landing — Image Generation Pipeline v3
With style reference image support for visual consistency.
"""

import os
import sys
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyAonZChFCeqDR2znVCa_vYS4npIpc-Retk")
MODEL = "gemini-3.1-flash-image-preview"
OUTPUT_DIR = Path(__file__).parent.parent / "public" / "img"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Default style reference — the hero image we loved
STYLE_REF = OUTPUT_DIR / "hero-wellness-social-raw.png"

client = genai.Client(api_key=API_KEY)

STYLE = """
CRITICAL STYLE INSTRUCTIONS — match the reference image EXACTLY:
- Flat editorial illustration, warm vector style with subtle texture
- Clean shapes, no outlines, smooth gradients within shapes
- Organic rounded forms, NOT geometric/angular
- Color palette STRICTLY: terracotta rust (#914126), warm brown (#8e5546),
  golden tan (#aa9578), cream (#eae1d0), dark brown (#5a3f36), soft white (#f5f2ec)
- Skin tones warm and natural, matching the reference
- Style feels like premium wellness brand editorial — Goop meets Aesop
- NO photorealism, NO 3D, NO harsh shadows
- Generous negative space, centered compositions
- Same level of detail and rendering as the reference image
"""

IMAGES = [
    {
        "name": "pain-empty-chair",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: an empty modern clinic reception — a beautiful premium waiting chair, EMPTY.
        A phone on a side table shows unread message notifications piling up (chat bubbles
        with notification badges). A small wilting plant on the counter.
        The feeling: "you're investing in ads but nobody comes." Beautiful space, nobody in it.
        Background: solid cream (#f5f2ec).
        Self-contained composition, same rendering style as reference.
        {STYLE}""",
        "remove_bg": True,
    },
    {
        "name": "patient-journey",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: a latina woman (30s, same skin tone as reference) looking at herself in an
        elegant arched mirror. In the mirror, her reflection looks MORE confident and radiant —
        subtle warm glow around the reflection. On her side (reality), she has a slightly
        uncertain but hopeful expression.
        The story: "I want to feel like THAT version of me."
        Background: solid cream (#f5f2ec).
        Same figure proportions, rendering, and color treatment as reference.
        {STYLE}""",
        "remove_bg": True,
    },
    {
        "name": "mechanism-dashboard",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: a laptop showing a simple dashboard with a line chart going UP week over week.
        Labels on chart: "semana 1", "semana 4", "semana 8". Next to the laptop, a small
        calendar with checkmarks, and a coffee cup. A circular arrow icon suggesting
        optimization/iteration. The feeling: calm, methodical, reliable progress.
        Background: solid dark brown (#3b2a23).
        Same rendering style, color warmth, and detail level as reference.
        {STYLE}""",
        "remove_bg": True,
    },
    {
        "name": "system-complete",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: a horizontal patient journey as a flowing curved path connecting 5 touchpoints:
        1) A phone showing an ad with a woman's face
        2) WhatsApp chat bubbles (conversation)
        3) A calendar with a date circled
        4) A clinic door opening
        5) A happy woman walking out with a small heart above her
        All connected by a smooth flowing terracotta line from left to right.
        Background: solid cream (#f5f2ec).
        Horizontal composition. Same figure style and colors as reference.
        {STYLE}""",
        "remove_bg": True,
    },
    {
        "name": "guarantee-shield",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: a confident latina woman (same style/proportions as reference image, 30-40s,
        business-casual) standing with arms crossed and a warm slight smile. Behind her,
        a large geometric shield with "90" written elegantly inside. Around the shield:
        a handshake icon, a checkmark, and a money-back arrow icon.
        The feeling: "we're so confident, we guarantee it."
        Background: solid dark brown (#3b2a23).
        Same rendering, skin tones, and style as reference.
        {STYLE}""",
        "remove_bg": True,
    },
    {
        "name": "results-full-agenda",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: an open appointment book/agenda that is COMPLETELY FULL — every slot filled
        with names. A pen resting on it. Next to it, a phone showing a notification
        "Nueva cita agendada". A small upward arrow suggesting growth.
        The contrast: THIS is the "after" — your agenda is full.
        Background: solid cream (#f5f2ec).
        Same rendering style and colors as reference.
        {STYLE}""",
        "remove_bg": True,
    },
    {
        "name": "cta-open-door",
        "prompt": f"""Create an illustration IN THE EXACT SAME STYLE as the reference image.
        Scene: an elegant arched doorway, slightly open, with warm golden light coming from
        inside. Through the opening, a hint of a beautiful clinic interior — warm and inviting.
        A small sign next to the door reads "Consulta". A subtle welcome mat.
        The feeling: "the door is open, just step in."
        Background: solid terracotta (#914126) wall with dark brown (#3b2a23) floor.
        Same rendering style as reference.
        {STYLE}""",
        "remove_bg": True,
    },
]


def load_reference_image(ref_path: Path) -> types.Part | None:
    """Load a reference image as a Part for Gemini."""
    if not ref_path.exists():
        print(f"  ⚠️  Reference image not found: {ref_path}")
        return None

    with open(ref_path, "rb") as f:
        image_bytes = f.read()

    return types.Part.from_bytes(data=image_bytes, mime_type="image/png")


def generate_image(image_def: dict, ref_image_part: types.Part | None = None) -> Path | None:
    name = image_def["name"]
    output_path = OUTPUT_DIR / f"{name}-raw.png"

    if output_path.exists():
        print(f"  ⏭  {name}-raw.png exists, skipping")
        return output_path

    print(f"  🎨 Generating: {name}...")

    try:
        # Build contents: reference image + prompt
        contents = []
        if ref_image_part:
            contents.append(ref_image_part)
            contents.append("Use the EXACT SAME illustration style as this reference image. Match the rendering, colors, figure proportions, and overall aesthetic perfectly. Now create this new scene:\n\n" + image_def["prompt"])
        else:
            contents.append(image_def["prompt"])

        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )

        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(output_path))
                print(f"  ✅ Saved: {output_path.name}")
                return output_path

        print(f"  ⚠️  No image in response for {name}")
        for part in response.parts:
            if part.text:
                print(f"      Text: {part.text[:300]}")
        return None

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None


def remove_background(input_path: Path, output_name: str) -> Path | None:
    from rembg import remove

    output_path = OUTPUT_DIR / f"{output_name}.png"

    if output_path.exists():
        print(f"  ⏭  {output_name}.png exists, skipping")
        return output_path

    print(f"  ✂️  Removing background: {output_name}...")

    try:
        with open(input_path, "rb") as f:
            input_data = f.read()

        output_data = remove(input_data)

        with open(output_path, "wb") as f:
            f.write(output_data)

        print(f"  ✅ Saved: {output_path.name}")
        return output_path

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None


def adhoc_generate(name: str, prompt: str, do_remove_bg: bool = True, ref_path: Path | None = None):
    """Generate a single image from a custom prompt."""
    full_prompt = f"{prompt}\n\n{STYLE}"
    img_def = {"name": name, "prompt": full_prompt, "remove_bg": do_remove_bg}

    for f in [OUTPUT_DIR / f"{name}-raw.png", OUTPUT_DIR / f"{name}.png"]:
        f.unlink(missing_ok=True)

    ref_part = load_reference_image(ref_path) if ref_path else None
    raw = generate_image(img_def, ref_part)
    if raw and do_remove_bg:
        remove_background(raw, name)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Aura image generation pipeline")
    parser.add_argument("target", nargs="?", help="Image name filter OR ad-hoc name")
    parser.add_argument("-p", "--prompt", help="Custom prompt for ad-hoc generation")
    parser.add_argument("-r", "--ref", help="Path to style reference image", default=None)
    parser.add_argument("--no-rembg", action="store_true", help="Skip background removal")
    parser.add_argument("--force", action="store_true", help="Force regeneration (delete existing)")
    args = parser.parse_args()

    print("=" * 60)
    print("🌟 Aura Landing — Image Pipeline v3 (style reference)")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Output: {OUTPUT_DIR}")

    # Determine reference image
    ref_path = Path(args.ref) if args.ref else STYLE_REF
    if ref_path.exists():
        print(f"📎 Style ref: {ref_path.name}")
    else:
        print(f"⚠️  No style ref found at {ref_path} — generating without reference")
        ref_path = None

    print()

    # Ad-hoc mode
    if args.prompt and args.target:
        print(f"🎯 Ad-hoc: {args.target}")
        print("-" * 40)
        adhoc_generate(args.target, args.prompt, not args.no_rembg, ref_path)
        print("\n✨ Done!")
        return

    # Batch mode
    images = [img for img in IMAGES if not args.target or args.target in img["name"]]

    if not images:
        print(f"No image matching '{args.target}'")
        return

    ref_part = load_reference_image(ref_path) if ref_path else None

    for i, img in enumerate(images, 1):
        name = img["name"]
        print(f"\n[{i}/{len(images)}] {name}")
        print("-" * 40)

        # Force regeneration if requested
        if args.force:
            for f in [OUTPUT_DIR / f"{name}-raw.png", OUTPUT_DIR / f"{name}.png"]:
                f.unlink(missing_ok=True)

        raw = generate_image(img, ref_part)
        if raw and img.get("remove_bg"):
            remove_background(raw, name)

    print(f"\n{'=' * 60}")
    print(f"✨ Done! Images in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
