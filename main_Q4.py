import cv2
import numpy as np


# Define a function to reduce the spatial resolution of an image
def average_block(img_path, block_sizes):
    # Load the image as grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Iterate over the block sizes
    for block_size in block_sizes:
        # Create a copy of the image to hold the result
        result = np.copy(img)

        # Get the size of the image
        h, w = img.shape

        # Iterate over the image in blocks and replace the pixels with the average value of the block
        for i in range(0, h - block_size + 1, block_size):
            for j in range(0, w - block_size + 1, block_size):
                # Calculate the start and end indices of the block
                start_i, end_i = i, i + block_size
                start_j, end_j = j, j + block_size

                # Get the block from the original image
                block = img[start_i:end_i, start_j:end_j]

                # Calculate the average of the block
                avg = np.mean(block)

                # Replace all pixels in the block with the average
                result[start_i:end_i, start_j:end_j] = avg

        # Display the image
        cv2.imshow(f'Average Block Image {block_size}x{block_size}', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the image
        cv2.imwrite(f'images/output/Q4/average_block_image_{block_size}x{block_size}.jpg', result)

    return


# Define the block sizes to use and the path to the image
blocks = [3, 5, 7]
image_path = 'images/input/Q1/my_image.jpg'
# Operation to simulate the image spatial resolution reduction, and display the results
average_block(image_path, blocks)
