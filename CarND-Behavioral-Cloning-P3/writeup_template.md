#**Behavioral Cloning** 

##Writeup Template

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road

[//]: # (Image References)

[image1]: ./examples/track_center.jpg "Normal track"
[image2]: ./examples/track_opposite.jpg "Opposite track"
[image3]: ./examples/track_recovery0.jpg "Recovery Image"
[image4]: ./examples/track_recovery1.jpg "Recovery Image"
[image5]: ./examples/track_recovery2.jpg "Recovery Image"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
###Files Submitted & Code Quality

####1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md summarizing the results

####2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

####3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

###Model Architecture and Training Strategy

####1. An appropriate model architecture has been employed

My model is inspired from NVIDIA’s architecture which consists of a convolution neural network with 5x5 filter sizes and depths between 24 and 64 (model.py lines 45-68) 

The model includes RELU layers to introduce nonlinearity (code line 49, 51, 53), and the data is normalized in the model using a Keras lambda layer (code line 46). 

####2. Attempts to reduce overfitting in the model

The model contains maxPooling layers in order to control overfitting (model.py lines 50, 52, 54). 

The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 71).

####4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road. Also driving the vehicle in opposite side of the track. 

For details about how I created the training data, see the next section. 

###Model Architecture and Training Strategy

####1. Solution Design Approach

The overall strategy for deriving a model architecture was to produce efficient measurements and make vehicle to stay on the track. 

My first step was to use a convolution neural network model similar to the Nvidia’s SDC architecture. I thought this model might be appropriate because it has enough combination of convolution and connected layers.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model with couple of MaxPooling layers.

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track. To improve the driving behavior in these cases, I increased the size of the data on curves. Flipping of images also helped a lot.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

####2. Final Model Architecture

The final model architecture (model.py lines 45-72) consisted of a convolution neural network with the following layers and layer sizes

```
model.add(Convolution2D(24, 5, 5, activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(36, 5, 5, activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(48, 5, 5, activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(64, 3, 3, border_mode='same', activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(64, 3, 3, border_mode='same', activation="relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(1164))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('relu'))
model.add(Dense(1))
```


####3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][image1]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to recover on its own when it understands what to do when it is going out of track. These images show what a recovery looks like starting from ... :

![alt text][image3]
![alt text][image4]
![alt text][image5]

I also recorded one lap on opposite direction in order to have more data points.

![alt text][image2]

To augment the data set, I also flipped images and angles thinking that this would give more data points when the vehicle is turning on left or right curves.
After the collection process, I had lots of data points which is used to train the model.


I finally randomly shuffled the data set and put 20% of the data into a validation set. 
The validation set helped determine if the model was over or under fitting. I used an adam optimizer so that manually training the learning rate wasn't necessary.
