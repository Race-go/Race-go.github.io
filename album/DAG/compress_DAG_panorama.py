from PIL import Image

# Disable decompression bomb warning for trusted large images
Image.MAX_IMAGE_PIXELS = None

img = Image.open("DAG_panorama_cropped.jpg")
#img.save("banner_compressed.jpg", optimize=True, quality=75)

# WebP limit: keep total pixels under ~89 million
max_pixels = 89_000_000
current_pixels = img.width * img.height

if current_pixels > max_pixels:
    # Calculate scaling factor
    scale_factor = (max_pixels / current_pixels) ** 0.5
    new_width = int(img.width * scale_factor)
    new_height = int(img.height * scale_factor)
    print(f"Resizing from {img.width}x{img.height} to {new_width}x{new_height}")
    img = img.resize((new_width, new_height), Image.LANCZOS)

# Save as WebP with quality 80
output_path = "DAG_panorama_compressed.webp"
img.save(output_path, format="WEBP", quality=80)
print(f"Saved compressed WebP: {output_path}")
