
# ==================================================
# TRIPT 360 Viewer
# generate_scenes.py
# Version 5.2.0
# ==================================================

import os
import json

# Pillow is required:
# pip install pillow
try:
    from PIL import Image
except ImportError:
    print("\nPillow is not installed.")
    print("Run: pip install pillow")
    input("\nPress Enter to close...")
    raise SystemExit

# =========================================
# WEBP SETTINGS
# =========================================

ENABLE_WEBP_CONVERSION = True
WEBP_QUALITY = 100          # 10 - 100
DELETE_ORIGINAL = True

# =========================================
# PROJECT PATHS
# =========================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

PANORAMA_FOLDER = os.path.join(PROJECT_ROOT, "assets", "panoramas")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "scenes.js")

os.makedirs(PANORAMA_FOLDER, exist_ok=True)

SOURCE_EXTENSIONS = (".jpg", ".jpeg", ".png")
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

converted = 0
deleted = 0
skipped = 0
original_size = 0
webp_size = 0

# =========================================
# WEBP CONVERSION
# =========================================

def convert_to_webp(path):
    global converted, deleted, skipped
    global original_size, webp_size

    base, _ = os.path.splitext(path)
    webp_path = base + ".webp"

    if os.path.exists(webp_path):
        if os.path.getmtime(webp_path) >= os.path.getmtime(path):
            skipped += 1
            return

    try:
        img = Image.open(path)

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")

        img.save(
            webp_path,
            "WEBP",
            quality=WEBP_QUALITY,
            method=6
        )

        if os.path.exists(webp_path):
            converted += 1
            original_size += os.path.getsize(path)
            webp_size += os.path.getsize(webp_path)

            if DELETE_ORIGINAL:
                os.remove(path)
                deleted += 1

    except Exception as e:
        print(f"Failed: {os.path.basename(path)}")
        print(e)

# =========================================
# CONVERT IMAGES
# =========================================

if ENABLE_WEBP_CONVERSION:
    for f in sorted(os.listdir(PANORAMA_FOLDER)):
        if f.lower().endswith(SOURCE_EXTENSIONS):
            convert_to_webp(os.path.join(PANORAMA_FOLDER, f))

# =========================================
# BUILD SCENE LIST
# =========================================

files = sorted([
    f for f in os.listdir(PANORAMA_FOLDER)
    if f.lower().endswith(SUPPORTED_EXTENSIONS)
])

if not files:
    print("\nNo panorama images found.")
    input("\nPress Enter to close...")
    raise SystemExit

scenes = []

for file in files:

    scene_id = os.path.splitext(file)[0]
    title = scene_id

    if "-" in title:
        first = title.split("-", 1)[0]
        if first.isdigit():
            title = title.split("-", 1)[1]

    title = title.replace("-", " ").title()

    scenes.append({
        "id": scene_id,
        "title": title,
        "file": file
    })

# =========================================
# WRITE scenes.js
# =========================================

js = "window.PANORAMA_SCENES = " + json.dumps(scenes, indent=4) + ";"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(js)

# =========================================
# REPORT
# =========================================

print("\n" + "=" * 60)
print("TRIPT 360 VIEWER V5.2.0")
print("=" * 60)

print(f"\nPanorama Folder:\n{PANORAMA_FOLDER}")
print(f"\nScenes Found : {len(scenes)}")
print(f"Converted    : {converted}")
print(f"Skipped      : {skipped}")
print(f"Deleted      : {deleted}")

if converted:
    saved = original_size - webp_size
    percent = (saved / original_size * 100) if original_size else 0
    print("\nStorage Report")
    print(f"Original Size : {original_size / 1024 / 1024:.2f} MB")
    print(f"WebP Size     : {webp_size / 1024 / 1024:.2f} MB")
    print(f"Saved         : {saved / 1024 / 1024:.2f} MB ({percent:.1f}%)")

print(f"\nGenerated:\n{OUTPUT_FILE}")

print("\nScene List:\n")
for i, scene in enumerate(scenes, 1):
    print(f"{i}. {scene['title']} -> {scene['file']}")

print("\n" + "=" * 60)
input("\nPress Enter to close...")
