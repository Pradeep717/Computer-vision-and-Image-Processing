import cv2
import numpy as np


# Define a function to perform spatial averaging on an image
def spatial_average(img_path, kernel_sizes):
    # Load the image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (640, 480))

    for kernel_size in kernel_sizes:
        # Create an averaging kernel
        kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)

        # Apply the kernel to the image using cv2.filter2D
        avg_img = cv2.filter2D(img, -1, kernel)

        # Display the image
        cv2.imshow(f'Average Image {kernel_size}x{kernel_size}', avg_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the image
        cv2.imwrite(f'images/output/Q2/average_image_{kernel_size}x{kernel_size}.jpg', avg_img)
    return


# Define the image path and kernel sizes
image_path = 'images/input/Q2/my_image.jpg'
kernels = [3, 10, 20]
# Perform spatial average for 3x3, 10x10, and 20x20 neighborhoods
spatial_average(image_path, kernels)
