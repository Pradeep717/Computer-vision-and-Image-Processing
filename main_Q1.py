import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Define a function to reduce the intensity levels of an image, which takes the image path and a list of levels as input
def reduce_intensity_levels(img_path, levels):
    # Open the image
    img = Image.open(img_path)
    # convert image to grayscale
    img = img.convert('L')

    # Create a figure to hold the subplots
    fig = plt.figure(figsize=(15, 10))

    for i, level in enumerate(levels):
        img_array = np.array(img)

        # Reduce the intensity levels
        reduction_factor = 256 // level
        reduced_img_array = (img_array // reduction_factor) * reduction_factor

        # Convert the array back to an image
        reduced_img = Image.fromarray(reduced_img_array.astype('uint8'))

        # Create a new subplot for this image
        fig.add_subplot(2, len(levels)//2, i+1)
        plt.axis('off')
        plt.title(f'Intensity Levels: {level}')
        plt.imshow(reduced_img, cmap='gray')

        # Save the image
        reduced_img.save(f'images/output/Q1/reduced_intensity_image_level_{level}.jpg')

    # Display all the subplots
    plt.tight_layout()
    plt.show()
    return


# Define the image path and the intensity levels to reduce to
image_path = 'images/input/Q1/my_image.jpg'
variable_intensities = [256, 128, 64, 32, 16, 8, 4, 2]


# Reduce the intensity levels of the image and display the results, saving each image to the output Q1 directory
reduce_intensity_levels(image_path, variable_intensities)
