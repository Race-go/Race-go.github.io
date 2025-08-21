from PIL import Image

# Disable decompression bomb warning for trusted large images
Image.MAX_IMAGE_PIXELS = None

img = Image.open("DAG_panorama_cropped.jpg")
#img.save("banner_compressed.jpg", optimize=True, quality=75)

# Target banner resolution (typical full-width banner)
max_width = 1920
max_height = 800

# Calculate scaling factor to fit within banner dimensions while preserving aspect ratio
width_ratio = max_width / img.width
height_ratio = max_height / img.height
scale_factor = min(width_ratio, height_ratio, 1)  # never upscale

new_width = int(img.width * scale_factor)
new_height = int(img.height * scale_factor)
if scale_factor < 1:
    print(f"Resizing from {img.width}x{img.height} to {new_width}x{new_height}")
    img = img.resize((new_width, new_height), Image.LANCZOS)

# Save as WebP with quality (adjustable)
output_path = "DAG_panorama_compressed.webp"
img.save(output_path, format="WEBP", quality=70)  # quality can be 60-80 for web
print(f"Saved compressed WebP banner: {output_path}")
