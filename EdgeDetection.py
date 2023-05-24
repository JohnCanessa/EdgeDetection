# **** ****
import numpy as np
import matplotlib.pyplot as plt

# **** ****
import skimage
from skimage import color, data, io
from skimage.filters import roberts, sobel


# **** read the image ****
skyline_color = skimage.io.imread('./images/pexels-skyline.jpg')    # 3D array

# **** convert RGB to grayscale before we perfomr edge detection ****
skyline = color.rgb2gray(skyline_color)                             # 2D array

# **** ****
plt.figure(figsize=(12, 12))
plt.imshow( skyline,
            cmap='gray')
plt.title('skyline')
plt.show()                                                          # show the image


# **** use the roberts filter to detect edges ****
skyline_edge_roberts = roberts(skyline)

# **** show the image ****
plt.figure(figsize=(12, 12))

plt.imshow( X=skyline_edge_roberts,
            cmap='gray')
plt.title('skyline_edge_roberts')
plt.show()                                                          # show the image


# **** use the sobel filter to detect edges 
#      Sobel is a more sensitive to diagonal edges than Roberts ****
skyline_edge_sobel = sobel(skyline)

# **** show the image ****
plt.figure(figsize=(12, 12))
plt.imshow( X=skyline_edge_sobel,
            cmap='gray')
plt.title('skyline_edge_sobel')
plt.show()                                                          # show the image


# **** ****
fig, axes = plt.subplots(   1, 
                            2, 
                            figsize=(8, 8),                         # width, height in inches
                            sharex=True,                            # x-axis will be shared among all subplots
                            sharey=True)                            # y-axis will be shared among all subplots
 
# **** flatten axes ****
ax = axes.ravel()
 
# **** plot roberts skyline ****
ax[0].set_title('skyline_edge_roberts')
ax[0].imshow(   skyline_edge_roberts,
                cmap='gray')
 
# **** plot sobel skyline ****
ax[1].set_title('skyline_edge_sobel')
ax[1].imshow(   skyline_edge_sobel,
                cmap='gray')
 
# **** fit plots within your figure cleanly (an alternative to tight_layout is constrained_layout) ****
fig.tight_layout()
 
# **** display the plots****
plt.show()