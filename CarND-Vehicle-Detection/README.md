## Writeup Template

---

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.


[//]: # (Image References)

[image1]: ./output_images/test_img_result_1.png "Test Image 1"
[image2]: ./output_images/test_img_result_2.png "Test Image 2"
[image3]: ./output_images/test_img_result_3.png "Test Image 3"
[image4]: ./output_images/test_img_result_4.png "Test Image 4"
[image5]: ./output_images/test_img_result_5.png "Test Image 5"
[image6]: ./output_images/test_img_result_6.png "Test Image 6"
[video1]: project_result.mp4 "Video"


### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

###Extract features & Train classifier

In this step, I wrote couple of helper functions to extract features of images like hog, bin and color. The code for this step is contained in the third cell of “Vehicle_Detection.ipynb”. You can find the individual functions for extracting features in first cell. 

###Train Classifier

In this step, I downloaded the data of `vehicle` and `non-vehicle`. This data was normalized, randomized and splitted into training and test set data to avoid overfitting and making classifier more generalized.

I used these data to train LinearSVC classifier. I saved the trained classifier locally. I verified that my classifier is working as expected by running it against test images.


![alt text][image1]

![alt text][image2]

![alt text][image3]

![alt text][image4]

![alt text][image5]

![alt text][image6]


### Tried various combinations
I tried couple of features and got effective result after combining hog, bin and color features. I also tried various parameters to get effective result and finally settled on following. You can find the code in `Train Classifier` cell.

```
color_space = 'YCrCb' # Can be RGB, HSV, LUV, HLS, YUV, YCrCb
orient = 10  # HOG orientations
pix_per_cell = 8 # HOG pixels per cell
cell_per_block = 2 # HOG cells per block
hog_channel = "ALL" # Can be 0, 1, 2, or "ALL"
spatial_size = (32, 32) # Spatial binning dimensions
hist_bins = 64    # Number of histogram bins
spatial_feat = True # Spatial features on or off
hist_feat = True # Histogram features on or off
hog_feat = True # HOG features on or off
```

###Sliding Window & Heat map

In this step, I used sliding window technique to look for cars in specific part of the image. There were lot of false positives and duplications which was avoided using heat map.

I used following params to find the car in following frames
```
1. ystart = 350, ystop = 500, xstart= 550, xstop= 850, scale = 1.25
2. ystart = 350, ystop = 700, xstart= 200, xstop= 500, scale = 1.51
3. ystart = 350, ystop = 700, xstart= 700, xstop= 1280, scale = 1.51
4. ystart = 350, ystop = 700, xstart= 200, xstop= 500, scale = 1.51
5. ystart = 350, ystop = 700, xstart= 700, xstop= 1280, scale = 1.51 
```

### Processed Video detecting cars (video)

Here's a [link to my video result](./project_result.mp4)

You can find the details about code in `Vehicle_Detection.ipynb`

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project. 

There were couple of issues while processing video. It was giving lots of false positives even after heat map. I used different regions with different scale to find cars in the image. This can be improved by adding more regional cutouts to detect vehicles and avoid false positives.
