import os
from PIL import Image

# Set the root folder where your image albums are stored
ROOT_FOLDER = r"C:\Users\nt23q323\Documents\Race-go.github.io\album\News"

# Thumbnail settings
THUMB_WIDTH = 300  # pixels
THUMB_SUBFOLDER = "thumbs"  # where to save thumbnails

def create_thumbnails(root_folder):
    for root, dirs, files in os.walk(root_folder):
        # Create the thumbs folder inside each image directory
        thumb_dir = os.path.join(root, THUMB_SUBFOLDER)
        os.makedirs(thumb_dir, exist_ok=True)
        
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                img_path = os.path.join(root, file)
                thumb_path = os.path.join(thumb_dir, file)
                
                # Skip if thumbnail already exists
                if os.path.exists(thumb_path):
                    continue
                
                try:
                    with Image.open(img_path) as img:
                        # Maintain aspect ratio
                        ratio = THUMB_WIDTH / img.width
                        height = int(img.height * ratio)
                        img.thumbnail((THUMB_WIDTH, height))
                        
                        # Save thumbnail
                        img.save(thumb_path, optimize=True, quality=85)
                        print(f"Created thumbnail: {thumb_path}")
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    create_thumbnails(ROOT_FOLDER)
    print("All thumbnails created successfully.")
