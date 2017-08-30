#**Traffic Sign Recognition** 
---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/visualization_dataset_training.png "Visualization Training Dataset"
[image2]: ./examples/visualization_dataset_test.png "Visualization Test Dataset"
[image3]: ./examples/original.png "Original"
[image4]: ./examples/gray_normalized.png "Grayscale n Normalized"
[image5]: ./test_images/test1.jpg "Traffic Sign 1"
[image6]: ./test_images/test2.jpg "Traffic Sign 2"
[image7]: ./test_images/test3.jpg "Traffic Sign 3"
[image8]: ./test_images/test4.jpg "Traffic Sign 4"
[image9]: ./test_images/test5.jpg "Traffic Sign 5"
[image_test1]: ./test_images/test6.jpg "Traffic Sign 6"
[image_test2]: ./examples/softmax_probability.png "Softmax Probability"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---

###Data Set Summary & Exploration

####1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the pandas library to calculate summary statistics of the traffic
signs data set:

* The size of training set is 34799
* The size of the validation set is 4410
* The size of test set is 12630
* The shape of a traffic sign image is (32, 32, 3)
* The number of unique classes/labels in the data set is 43

####2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a bar chart showing how the data is distributed in Training and Test set.

![alt text][image1]

![alt text][image2]

###Design and Test a Model Architecture

####1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. 

As a first step, I decided to convert the images to grayscale because traffic signs have similar color combinations. It doesn’t have that much effect while training network.

I have also normalized the data and shuffle the data to avoid overfitting.

Here is an example of a traffic sign image after grayscaling and normalized.

![alt text][image3]

![alt text][image4]


####2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

| Layer         	|     Description	        		| 
|:---------------------:|:---------------------------------------------:|
| Input         	| 32x32x1 Gray image   				| 
| Convolution 5x5     	| 1x1 stride, same padding, outputs 28x28x6 	|
| RELU			|						|
| Max pooling	      	| 2x2 stride,  outputs 16x16x64 		|
| Convolution 5x5	| 1x1 stride, same padding, outputs 10x10x16    |
| RELU			|						|
| Max pooling	      	| 2x2 stride,  outputs 5x5x16	 		|
| Flatten		|						|
| Fully connected	| outputs 120					|
| RELU			|						|
| Fully connected	| outputs 84					|
| Fully connected	| outputs 43					| 


####3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used following parameters

* EPOCHS = 30
* BATCH_SIZE = 128
* learning_rate = 0.001


####4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* validation set accuracy after 30th Epoch is 0.950

If an iterative approach was chosen:
* What was the first architecture that was tried and why was it chosen?
* What were some problems with the initial architecture?
* How was the architecture adjusted and why was it adjusted? Typical adjustments could include choosing a different model architecture, adding or taking away layers (pooling, dropout, convolution, etc), using an activation function or changing the activation function. One common justification for adjusting an architecture would be due to overfitting or underfitting. A high accuracy on the training set but low accuracy on the validation set indicates over fitting; a low accuracy on both sets indicates under fitting.
* Which parameters were tuned? How were they adjusted and why?
* What are some of the important design choices and why were they chosen? For example, why might a convolution layer work well with this problem? How might a dropout layer help with creating a successful model?

If a well known architecture was chosen:
* What architecture was chosen?
I chose LeNet architecture as it’s proven to be the good architecture for MNIST data.
* Why did you believe it would be relevant to the traffic sign application?
It has performed quite better with MNIST data.
* How does the final model's accuracy on the training, validation and test set provide evidence that the model is working well?
 Validation accuracy is pretty good over 94%.

###Test a Model on New Images

####1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are Six German traffic signs that I found on the web:

![alt text][image5] 

![alt text][image6] 

![alt text][image7] 

![alt text][image8] 

![alt text][image9] 

![alt text][image_test1]


####2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction and probability:

| Image			        |     Prediction	        	|           Probability                  |
|:-----------------------------:|:-------------------------------------:| :-------------------------------------:|
| Ahead only      		| Ahead only   				| 	1.0				 |
| Stop     			| Stop 					|	1.0				 |
| Road Work			| Priority Road				|	1.0				 |
| Go Straight or Left	      	| Go Straight or Left			|	1.0				 |
| Speed limit (30km/h)		| Speed limit (30km/h)      		|	1.0				 |
| Turn Right ahead		| Turn Right ahead      		|	1.0				 |


![alt text][image_test2]


The code for making predictions on my final model is located in the 11th cell of the Ipython notebook.