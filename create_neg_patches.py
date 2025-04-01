import cv2

for i in range(473, 944):
    # Read the image
    image = cv2.imread(f'Train/Train/JPEGImages/image ({i}).jpg')

    # Get image dimensions
    height, width, _ = image.shape
    if height > width:
        # Rotate image in 90 deg
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        height, width = width, height
    
    width1 = width // 3
    height1 = height // 3
    width2 = int(width // 1.5)
    height2 = int(height // 1.5)
    # Create negative patches
    neg_patch1 = image[0:height1, 0:width1]
    neg_patch2 = image[0:height1, width1:width2]
    neg_patch3 = image[height1:height2, 0:width1]
    neg_patch4 = image[height1:height2, width1:width2]

    # Display the image
    cv2.imwrite(f'patches/neg patches/tile_{i}_1.jpg', neg_patch1) 
    cv2.imwrite(f'patches/neg patches/tile_{i}_2.jpg', neg_patch2) 
    cv2.imwrite(f'patches/neg patches/tile_{i}_3.jpg', neg_patch3) 
    cv2.imwrite(f'patches/neg patches/tile_{i}_4.jpg', neg_patch4)
 
print("Negative patches created successfully.")
