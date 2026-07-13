# TRIPT 360 VIEWER - V5.1.1

## Project Overview

TRIPT 360 Viewer is a lightweight, modular web-based 360° virtual
walkthrough system built using **HTML, CSS, JavaScript, Python, and
Pannellum**.

The project is designed for architectural and interior design
presentations where users can explore multiple 360° panoramas through a
clean, responsive interface.

The viewer automatically detects panorama images, generates scene data,
builds the navigation dynamically, and loads the panoramas without
requiring any manual editing.

------------------------------------------------------------------------

# Current Features

## Panorama Viewer

-   Powered by Pannellum
-   Supports equirectangular panoramas
-   Auto-loads the first scene
-   Smooth scene transitions

## Automatic Scene Generation

Panorama images are read automatically from:

    assets/panoramas/

Supported formats:

-   .jpg
-   .jpeg
-   .png
-   .webp

Running

    python data/generate_scenes.py

creates

    data/scenes.js

automatically.

------------------------------------------------------------------------

## Dynamic Navigation

Navigation buttons are generated automatically from `data/scenes.js`.

Features:

-   Automatic room buttons
-   Horizontal scrolling
-   Left / Right navigation arrows
-   Mouse wheel horizontal scrolling
-   Mobile swipe scrolling
-   Responsive navigation bar

No manual coding is required when new panoramas are added.

------------------------------------------------------------------------

## Scene Title

The current room name is displayed in the glass title bar at the
top-center.

Example:

-   Reception
-   Lobby
-   Cafe

The old "360° Virtual Walkthrough" label and the default Pannellum scene
title have been removed for a cleaner interface.

------------------------------------------------------------------------

## Branding

A floating TRIPT circular logo appears at the top-left.

Branding logic:

    js/branding.js

Logo location:

    assets/logos/

------------------------------------------------------------------------

# Project Structure

    v5_1/

    ├── index.html
    │
    ├── css/
    │   └── styles.css
    │
    ├── js/
    │   ├── app.js
    │   ├── viewer.js
    │   ├── navigation.js
    │   ├── branding.js
    │   └── utils.js
    │
    ├── data/
    │   ├── generate_scenes.py
    │   └── scenes.js
    │
    ├── assets/
    │   ├── panoramas/
    │   └── logos/
    │
    └── essential/
        ├── README.md
        └── CHANGELOG.md (recommended)

------------------------------------------------------------------------

# Project Workflow

    Panorama Images
            │
            ▼
    generate_scenes.py
            │
            ▼
    data/scenes.js
            │
            ▼
    viewer.js
            │
            ▼
    navigation.js
            │
            ▼
    index.html
            │
            ▼
    User Interface

------------------------------------------------------------------------

# File Responsibilities

## index.html

Responsible for:

-   Loading all CSS and JavaScript
-   Panorama container
-   Scene title
-   Navigation wrapper
-   Branding container

------------------------------------------------------------------------

## css/styles.css

Responsible for:

-   Layout
-   Responsive design
-   Navigation appearance
-   Navigation arrows
-   Branding
-   Title bar
-   Pannellum UI customization

------------------------------------------------------------------------

## js/app.js

Application entry point.

Initialization order:

    validateScenes()

    buildScenes()

    createViewer()

    createNavigation()

    initializeBranding()

------------------------------------------------------------------------

## js/viewer.js

Responsible for:

-   Building Pannellum scenes
-   Loading panoramas
-   Switching rooms
-   Viewer configuration

If panorama loading behavior changes, modify this file.

------------------------------------------------------------------------

## js/navigation.js

Responsible for:

-   Building navigation buttons
-   Active button state
-   Scene switching
-   Title updates
-   Horizontal scrolling
-   Arrow navigation

This file controls every navigation-related feature.

------------------------------------------------------------------------

## js/branding.js

Responsible for:

-   Logo
-   Branding interactions

Future branding additions:

-   Website button
-   Contact popup
-   Client branding
-   Social links

------------------------------------------------------------------------

## js/utils.js

Shared helper functions.

Currently:

-   Scene validation

------------------------------------------------------------------------

## data/generate_scenes.py

Reads panorama images and automatically generates:

    data/scenes.js

Also creates required folders if missing.

------------------------------------------------------------------------

## data/scenes.js

Automatically generated.

Do NOT edit manually.

------------------------------------------------------------------------

# Customization Guide

## Add New Panorama

1.  Copy panorama images into

```{=html}
<!-- -->
```
    assets/panoramas/

2.  Run

```{=html}
<!-- -->
```
    python data/generate_scenes.py

3.  Open the website.

Done.

------------------------------------------------------------------------

## Change Logo

Replace:

    assets/logos/tript-logo-circle.png

Logic:

    js/branding.js

Style:

    css/styles.css

------------------------------------------------------------------------

## Change Navigation

Logic:

    js/navigation.js

Style:

    css/styles.css

------------------------------------------------------------------------

## Change Viewer

    js/viewer.js

------------------------------------------------------------------------

## Change Scene Generator

    data/generate_scenes.py

------------------------------------------------------------------------

# Version History

## V1

-   Single panorama viewer

## V2

-   Multi-scene support

## V3

-   Dynamic scene navigation

## V4

-   Automatic scene generation

## V5

-   GitHub deployment workflow

## V5.1

-   Modular architecture
-   Branding module
-   Cleaner UI
-   Responsive design

## V5.1.1

-   Horizontal scrolling navigation
-   Left / Right navigation arrows
-   Mouse wheel scrolling
-   Improved navigation layout

------------------------------------------------------------------------

# Future Roadmap

## V5.2

-   Branding improvements

## V5.3

-   Thumbnail navigation

## V6

Possible additions:

-   Floorplan navigation
-   Hotspots
-   Multi-floor support
-   VR enhancements

------------------------------------------------------------------------

# Design Philosophy

The architecture visualization should always remain the primary focus.

The interface is intentionally minimal, responsive, modular, and easy to
extend.

Every new feature should belong to its own module whenever possible to
keep the project maintainable.

------------------------------------------------------------------------

# Author

**TRIPT**

Designing Spaces That Inspire
