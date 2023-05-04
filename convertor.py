from PIL import Image
import os

# Set the path of the directory containing the WebP files
webp_super_dir = os.getcwd()
webp_dir = os.path.join(webp_super_dir, "webp")
print(webp_dir)
# Set the path of the directory where the PNG files will be saved

subdir_path = os.path.join(webp_dir, "png-converted")

png_dir = subdir_path

# Create the PNG directory if it doesn't exist
if not os.path.exists(png_dir):
    os.makedirs(png_dir)

# Loop through all the files in the WebP directory
for filename in os.listdir(webp_dir):
    # Check if the file is a WebP file
    if filename.endswith(".webp"):
        # Open the WebP file
        with Image.open(os.path.join(webp_dir, filename)) as im:
            # Save the file as a PNG file in the PNG directory
            im.save(os.path.join(png_dir, os.path.splitext(
                filename)[0] + ".png"), "PNG")
