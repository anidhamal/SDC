# Vehicle Detection
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


The Project
---

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.


[//]: # (Image References)

[image1]: output_images/test_img_result_1.png “Test Image 1“
[image2]: output_images/test_img_result_2.png “Test Image 2“
[image3]: output_images/test_img_result_3.png “Test Image 3“
[image4]: output_images/test_img_result_4.png “Test Image 4“
[image5]: output_images/test_img_result_5.png “Test Image 5“
[image6]: output_images/test_img_result_6.png “Test Image 6“
[video1]: project_result.mp4 "Video"


### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

###Extract features & Train classifier

In this step, I wrote couple of helper functions to extract features of images like hog, bin and color. These features were then combined to get effective result. This data was normalized, randomized and splitter into training and test set data to avoid overfitting and making classifier more generalized.

I used these data to train LinearSVC classifier. I saved the trained classifier locally. I verified that my classifier is working as expected by running it against test images.

![alt text][image1]
![alt text][image2]
![alt text][image3]
![alt text][image4]
![alt text][image5]
![alt text][image6]

###Sliding Window & Heat map

In this step, I used sliding window technique to look for cars in specific part of the image. There were lot of false positives and duplications which was avoided using heat map.

### Processed Video detecting cars (video)

Here's a [link to my video result](./project_result.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project. 

There were couple of issues while processing video. It was giving lots of false positives even after heat map. I used different regions with different scale to find cars in the image. This can be improved by adding more regional cutouts to detect vehicles and avoid false positives.
