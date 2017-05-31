
# Writeup/ P1 - Finding Lane Lines

## The goals / steps of this project are the following:

## Make a pipeline that finds lane lines on the road


### Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

  * My pipeline consisted of 6 steps. 
    * First, I converted the images to grayscale by calling grayscale()
    * Blurred the image by calling gaussian_blur() with kernel 5.
    * Found edges of the image using canny()
    * Created region of interest as quadrilateral shape
    * Feed the image to hough_lines with tuned values. It will also draw lines on the image w thickness.
    * Created Stacked image by adding original image and lined image

  * In order to draw a single line on the left and right lanes, I modified the draw_lines() function by using extrapolation. I followed following steps.
    * Get slopes of every line in lines
    * Add co-ordiantes of these lines in the list for acceptable slopes (0.5 to 0.8)
    * I created helper function draw_lane(). Call it to draw left and right lanes

  * draw_lane()
    * It gets the average of co-ordinates. 
    * Finds average slope of the line.
    * Uses known values and extrapolation formula to find x co-ordinates 
    * These co-ordinates will then be feed to OScv2 for drawing the line.

### Identify potential shortcomings with your current pipeline

  * Potential shortcoming would be 
    * what would happen when lanes doesn't exists or blurred.
    * when other cars are changing lane so lanes are not captured in camera
    * Roads are curvy.
    * Obstacles
    * what would happend when in the dark night


### Suggest possible improvements to your pipeline

  * A possible improvement would be to
    * Instead of using only two points to draw lines, use cluster of points on the lane
    * Find the area of quadrilateral to draw lines.
