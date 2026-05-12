import os
from PIL import Image
from caption import generate_caption
from story import generate_story

# Paths
image_folder = "data/images"
output_file = "output/stories.txt"

# Create output folder
os.makedirs("output", exist_ok=True)

# Open file once
with open(output_file, "w", encoding="utf-8") as f:

    for img_name in os.listdir(image_folder):
        img_path = os.path.join(image_folder, img_name)

        try:
            image = Image.open(img_path).convert("RGB")

            caption = generate_caption(image)
            story = generate_story(caption)

            # Write to file
            f.write(f"Image: {img_name}\n")
            f.write(f"Caption: {caption}\n")
            f.write(f"Story: {story}\n")
            f.write("="*50 + "\n")

            print(f"Processed: {img_name}")

        except Exception as e:
            print(f"Error with {img_name}: {e}")

print("✅ All captions and stories saved in output/stories.txt")