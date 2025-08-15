"""
Image Resizer Tool
==================
📌 Objective:
    - Resize and convert images in batch from a given folder.

📄 Features:
    1. Reads all images from an input folder
    2. Resizes images to a given size
    3. Converts images to the desired format
    4. Saves processed images into an output folder
    5. Handles errors gracefully
    6. Auto-generates sample images for testing
    7. Easy to extend to GUI

🛠 Tools:
    - Python
    - Pillow (PIL)
    - OS module
"""

import os
from PIL import Image

# ---------- Step 1: Create Sample Images for Testing ----------
def create_sample_images(folder="sample_images"):
    os.makedirs(folder, exist_ok=True)

    samples = [
        ("sample1.jpg", (500, 300), "skyblue"),
        ("sample2.png", (400, 400), (255, 0, 0, 255)),
        ("sample3.webp", (300, 300), "green"),
        ("large_image.jpg", (4000, 3000), "orange")
    ]

    for name, size, color in samples:
        img = Image.new("RGB" if isinstance(color, str) else "RGBA", size, color)
        img.save(os.path.join(folder, name))

    print(f"✅ Sample images created in: {folder}")


# ---------- Step 2: Batch Resize & Convert ----------
def resize_and_convert_images(input_folder, output_folder, size=(800, 600), output_format="JPEG", quality=90):
    """
    Resizes and converts all images from input_folder to output_folder
    """
    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if not a file
        if not os.path.isfile(file_path):
            continue

        try:
            with Image.open(file_path) as img:
                # Resize
                img_resized = img.resize(size)

                # Prepare new filename
                base_name = os.path.splitext(filename)[0]
                new_filename = f"{base_name}.{output_format.lower()}"
                output_path = os.path.join(output_folder, new_filename)

                # Convert and save
                img_resized.convert("RGB").save(output_path, output_format, quality=quality)

                print(f"✅ {filename} → {new_filename} ({size[0]}x{size[1]})")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")


# ---------- Step 3: Main Program ----------
if __name__ == "__main__":
    print("\n=== 🖼 Image Resizer Tool ===\n")

    # 1. Generate sample images for testing
    create_sample_images()

    # 2. Ask user for input & output folder (can use default)
    input_folder = input("📂 Enter input folder path (default: sample_images): ").strip() or "sample_images"
    output_folder = input("📂 Enter output folder path (default: output_images): ").strip() or "output_images"

    # 3. Ask for resize size
    try:
        width = int(input("📏 Enter width (default: 800): ") or 800)
        height = int(input("📏 Enter height (default: 600): ") or 600)
    except ValueError:
        print("⚠ Invalid size, using default 800x600.")
        width, height = 800, 600

    # 4. Ask for output format
    output_format = input("💾 Enter output format (JPEG/PNG/WebP) [default: JPEG]: ").strip().upper() or "JPEG"

    # 5. Ask for quality
    try:
        quality = int(input("🎯 Enter image quality (1-100) [default: 90]: ") or 90)
    except ValueError:
        print("⚠ Invalid quality, using default 90.")
        quality = 90

    # 6. Process images
    resize_and_convert_images(input_folder, output_folder, size=(width, height), output_format=output_format, quality=quality)

    print(f"\n🎉 All done! Resized images saved in '{output_folder}'\n")
