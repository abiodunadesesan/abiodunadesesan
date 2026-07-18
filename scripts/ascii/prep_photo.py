from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

# Project paths
ROOT = Path(__file__).resolve().parents[2]

INPUT_IMAGE = ROOT / "assets" / "images" / "profile.jpg"
OUTPUT_IMAGE = ROOT / "assets" / "output" / "profile-prepped.png"

# Create output directory if it doesn't exist
OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)

# Load image
image = Image.open(INPUT_IMAGE)

# Convert to grayscale
image = ImageOps.grayscale(image)

# Auto contrast
image = ImageOps.autocontrast(image)

# Increase contrast slightly
image = ImageEnhance.Contrast(image).enhance(1.6)

# Slight brightness adjustment
image = ImageEnhance.Brightness(image).enhance(1.05)

# Resize while preserving aspect ratio
TARGET_WIDTH = 120

width, height = image.size
aspect_ratio = height / width

# Characters are taller than they are wide, so compensate
TARGET_HEIGHT = int(TARGET_WIDTH * aspect_ratio * 0.55)

image = image.resize((TARGET_WIDTH, TARGET_HEIGHT))

# Save processed image
image.save(OUTPUT_IMAGE)

print(f"Saved processed image to {OUTPUT_IMAGE}")
