# Image-Processing-Project

a GUI Program that applies several image processing techniques (Image Filters, Edge Detectors, Morphological Operations and Segmentation) to an image.

#### Dependencies
  -  python
  -  tkinter
  -  pillow
  -  opencv-python
  -  numpy

### Demo Tutorial

https://github.com/ahmedmontaser110/Image-Processing-Project/assets/26957856/1d546cc4-bed2-434d-8ac6-355fa478642a

### Image Processing Techniques Included

#### Filters
1. **LPF**: reduces high-frequency noise and smooths an image by allowing only low-frequency information to pass through, while attenuating high-frequency components. LPFs are commonly used for noise reduction, image smoothing, and preprocessing tasks in various applications such as image enhancement, compression, and feature extraction.

2. **HPF**: enhances high-frequency components while attenuating low-frequency information. It works by emphasizing rapid changes or edges in pixel values while suppressing gradual variations or smooth regions. HPFs are commonly used for edge detection, sharpening images, and extracting fine details from images. They help highlight important features and edges in an image while reducing the impact of background or low-frequency components.

3. **Mean Filter**: used for smoothing or blurring images by replacing each pixel value with the average of its neighborhood. It helps reduce high-frequency noise and small-scale variations, making images smoother. The size of the neighborhood determines the extent of smoothing. It's simple and widely used for noise reduction and image preprocessing tasks.

4. **Median Filter**:used for noise reduction by replacing each pixel value with the median value of its neighborhood. It effectively removes salt-and-pepper noise and preserves edges better than the Mean Filter. The size of the neighborhood determines the extent of noise reduction. Median filtering is efficient and commonly used for removing impulse noise in images.


#### Edge Detectors
1. **Roberts edge detector**: a simple edge detection technique employing two 2x2 convolution kernels to detect horizontal and vertical edges separately. It's computationally efficient but may produce noisy results due to its simplicity.

2. **Prewitt edge detector**: utilizing a pair of 3x3 kernels, offers improved noise suppression compared to Roberts, yet it remains susceptible to noise. 

3. **Sobel edge detector**: employing 3x3 kernels but incorporating Gaussian smoothing, provides enhanced noise reduction and edge localization, making it widely used in various image processing tasks.


#### Morphological Operations
Fundamental techniques in image processing for shape analysis, noise reduction, and feature extraction.

1. **Erosion**: shrinks or erodes the boundaries of objects in an image, for each pixel in the image, erosion replaces its value with the minimum value of its neighbors within a specified kernel or structuring element. As a result, erosion tends to remove pixels near the boundaries of objects, causing the objects to appear smaller or thinner

2. **Dilation**: expands or thickens the boundaries of objects in an image, for each pixel in the image, dilation replaces its value with the maximum value of its neighbors within a specified kernel or structuring element. As a result, dilation tends to add pixels to the boundaries of objects, causing the objects to appear larger or thicker.

3. **Open**: removes small objects and smoothes boundaries.

4. **Close**: fills small gaps and joins nearby objects.

5. **Hough circle transform**: detects circular shapes in an image, widely used in computer vision applications for tasks like object detection and medical image analysis. It identifies circles by transforming the image space to a parameter space, where circles are represented as peaks, allowing robust detection even in the presence of noise or partial occlusion.

#### Segmentation
1. **Thresholding segmentation**: create binary images by dividing the grayscale image into two regions based on a threshold value. Pixels with intensity values above the threshold are assigned one value (often white or foreground), while pixels below the threshold are assigned another value (often black or background). Thresholding is simple yet effective for tasks like object detection, image segmentation, and feature extraction, where clear intensity differences exist between foreground and background regions.

2. **Edge Dectection segmentation**: focuses on identifying edges or boundaries between objects in an image. It involves detecting significant changes or discontinuities in pixel intensities, which often correspond to object boundaries or features. Common edge detection techniques include gradient-based methods such as Sobel, and Prewitt, which highlight edges by computing the gradient magnitude or detecting local intensity variations. Edge detection segmentation is widely used in applications such as object detection, image registration, and boundary detection.



