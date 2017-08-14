## Writeup Template

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./examples/result_images/UndistortedImage6.png "Undistorted"
[image2]: ./examples/result_images/ThresholdedImage6.png "Thresholded"
[image3]: ./examples/result_images/WarpedImage6.png  "Warped and Visualized"
[image4]: ./examples/warped_straight_lines.jpg "Warp Example"
[image5]: ./examples/color_fit_lines.jpg "Fit Visual"
[image6]: ./examples/result_images/* "Output"
[video1]: ./examples/project_video.mp4 "Video"
[image7]: ./examples/result_images/CameraCalibrationTest.png "Camera Calibration Test"
[image8]: ./examples/result_images/PerspectiveTransformed.png "Bird's View"

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### Camera Calibration
In this step, I calibrated the camera to find camera matrix and distortion coefficients. 

I used opencv functions `findChessboardCorners()` and `drawChessboardCorners`. You can find the details about this function in `Advanced_Lane_Finding.ipynb`
Output of this function is being used to undistort the camera images.

![alt text][image7]

#### Perspective Transform

In this step, I used opencv functions `getPerspectiveTransform` and `warpPerspective`. It helps to get bird's view of the images which helps to find radius curvature of the lanes.
You can find the details about this function in `Advanced_Lane_Finding.ipynb` as `perspective_transform`.


```python
    src = np.float32([[590, 450], 
                     [700, 450],
                     [1150, img_size[1]],
                     [200, img_size[1]]])

    dst = np.float32([[300, 0],
                      [950, 0],
                      [950, img_size[1]],
                      [300, img_size[1]]])
```

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image8]

#### Pipeline

In this step, I used a combination of color and gradient thresholds to generate a binary image. Here's an example of my output for this step.  

![alt text][image2]

#### Fit polynomial

Then I used transformed image to fit lane line in 2nd order polynomial kinda like this:

#### 5. Radius of Curvature 

I calculated radius of curvature of the lane. You can find the details in function `radius_curvature`. 

#### 6. Draw polygon on the frame to detect polygonal shape of the detected line.
I implemented this step to draw polygon on the image and also added strings for radius curvature and camera offset on the image.  Here is an example of my result on a test image:

![alt text][image3]

---

### Pipeline (video)


Here's a [link to my video result](./project_video.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project. 

While testing i found that polygon was going out of control on the curve. So i added mask which essentially avoided detecting wrong lanes. It has limitation in detecting actual lanes like  lanes in challenge videos, which can be improved by adding mask inside the polygon. 
