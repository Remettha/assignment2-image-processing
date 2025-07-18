import cv2
import os

# Folders
folders = ['cat', 'dog']  # These are the subfolders inside Assignment2
output_folder = 'output'

# Make sure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each folder (cat and dog)
for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)

            if img is None:
                print(f"❌ Cannot read image: {img_path}")
                continue

            # Resize image
            resized = cv2.resize(img, (300, 300))

            # Convert to grayscale
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(output_folder, f'gray_{folder}_{filename}'), gray)

            # Apply blur
            blur = cv2.GaussianBlur(resized, (5, 5), 0)
            cv2.imwrite(os.path.join(output_folder, f'blur_{folder}_{filename}'), blur)

            # Edge detection
            edges = cv2.Canny(resized, 100, 200)
            cv2.imwrite(os.path.join(output_folder, f'edges_{folder}_{filename}'), edges)

            # Rotate
            rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(os.path.join(output_folder, f'rotated_{folder}_{filename}'), rotated)

print("✅ All images processed and saved in output folder!")