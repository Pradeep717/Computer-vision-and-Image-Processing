from PIL import Image


# Define a function to rotate an image by a given angle
def rotate_image(img_path, angles):
    # Open the image
    img = Image.open(img_path)

    # Iterate over the angles
    for angle in angles:
        # Rotate the image by the given angle
        rotated_img = img.rotate(angle, resample=Image.BICUBIC, expand=True)

        # Display the image
        rotated_img.show()

        # Save the image
        rotated_img.save(f'images/output/Q3/rotated_image_{angle}.jpg')
    return


# Define the image path and angles to rotate by
image_path = 'images/input/Q3/my_image.jpg'
rotate_angles = [45, 90]
# Rotate the image by 45 and 90 degrees
rotate_image(image_path, rotate_angles)
