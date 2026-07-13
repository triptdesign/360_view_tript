# ==================================================
# V4.1 - Auto Generate scenes.js
# ==================================================

import os
import json

# ==================================================
# PROJECT PATHS
# ==================================================

# ==================================================
# PROJECT PATHS
# ==================================================

SCRIPT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_ROOT = os.path.dirname(
    SCRIPT_DIR
)

ASSETS_FOLDER = os.path.join(
    PROJECT_ROOT,
    "assets"
)

PANORAMA_FOLDER = os.path.join(
    ASSETS_FOLDER,
    "panoramas"
)

OUTPUT_FILE = os.path.join(
    SCRIPT_DIR,
    "scenes.js"
)

# ==================================================
# CREATE REQUIRED FOLDERS
# ==================================================

os.makedirs(
    PANORAMA_FOLDER,
    exist_ok=True
)

# ==================================================
# SUPPORTED FILE TYPES
# ==================================================

SUPPORTED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
)

# ==================================================
# READ PANORAMA FILES
# ==================================================

files = []

for file in os.listdir(PANORAMA_FOLDER):

    if file.lower().endswith(
        SUPPORTED_EXTENSIONS
    ):

        files.append(file)

# ==================================================
# SORT FILES
# ==================================================

files.sort()

# ==================================================
# NO FILES FOUND
# ==================================================

if len(files) == 0:

    print("\n" + "=" * 60)

    print("NO PANORAMA IMAGES FOUND")

    print("\nPlace panorama images inside:")

    print(
        PANORAMA_FOLDER
    )

    print("\nSupported formats:")

    print(
        ".jpg  .jpeg  .png  .webp"
    )

    print("\n" + "=" * 60)

    input(
        "\nPress Enter to close..."
    )

    quit()

# ==================================================
# CREATE SCENE DATA
# ==================================================

scenes = []

for file in files:

    scene_id = os.path.splitext(
        file
    )[0]

    title = scene_id

    # Remove numbering prefix

    if "-" in title:

        first_part = title.split(
            "-",
            1
        )[0]

        if first_part.isdigit():

            title = title.split(
                "-",
                1
            )[1]

    # Replace dash

    title = title.replace(
        "-",
        " "
    )

    # Title Case

    title = title.title()

    scenes.append({

        "id": scene_id,

        "title": title,

        "file": file

    })

# ==================================================
# GENERATE scenes.js
# ==================================================

js_content = (
    "window.PANORAMA_SCENES = "
    + json.dumps(
        scenes,
        indent=4
    )
    + ";"
)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        js_content
    )

# ==================================================
# REPORT
# ==================================================

print("\n" + "=" * 60)

print(
    "SCENE GENERATION COMPLETED"
)

print("=" * 60)

print(
    f"\nPanorama Folder:\n{PANORAMA_FOLDER}"
)

print(
    f"\nScenes Found: {len(scenes)}"
)

print(
    f"\nGenerated:\n{OUTPUT_FILE}"
)

print("\nScene List:\n")

for index, scene in enumerate(
    scenes,
    start=1
):

    print(
        f"{index}. "
        f"{scene['title']} "
        f"-> "
        f"{scene['file']}"
    )

print("\n" + "=" * 60)

input(
    "\nPress Enter to close..."
)