# RealTimeNeuralStyleBeautify

<h3>Theme Chosen</h3>
AI in Entertainment through Neural Style Transfer deployed in real time video capture with different styles.

<h3>Project Description</h3>
We used OpenCV to capture real time videos and take snaps of every frame and processed each image by normalizing it and resizing it according to our input dimensions and processed it in the style of the input chosen by the user.

To implement this in a user friendly manner, we have created an application using Tkinter module in Python. The user has choice to either select his/her own image by specifying a directory path and then selecting any given style. Also, they can select to capture a real time video with their desired style using the same application. We also implemented a small web application for the same (https://github.com/raghav275/Neural_Style_Transfer_Website)

Here is a view of the application developed using Tkinter:
![alt text](https://github.com/pip33eed/RealTimeNeuralStyleBeautify/blob/master/ss1.png "Sneak Peek")

The user has to copy the directory to the path of the image along with it's image name and insert in, and click on submit:
![alt text](https://github.com/pip33eed/RealTimeNeuralStyleBeautify/blob/master/ss2.png "Directory")

The results are like below:

### Before Transformation:
![alt text](https://github.com/pip33eed/RealTimeNeuralStyleBeautify/blob/master/vmikGbI.jpg "Battlefield")








### After Transformation:
![alt text](https://github.com/pip33eed/RealTimeNeuralStyleBeautify/blob/master/scream.png "After filter")



## On Person (before):
![alt text](https://github.com/pip33eed/RealTimeNeuralStyleBeautify/blob/master/raghav_gupta.jpeg "Raghav")







## On Person (after):
![alt text](https://github.com/pip33eed/RealTimeNeuralStyleBeautify/blob/master/raghav.png "raghu")





## How our project stands out against the other exisiting solutions or products?
We implemented a real time neural style transfer that captures both image and video. The existing products work only on static images. We have extended the idea to different platforms like Desktop and Website (linked above).

## Optimizations
Due to limited computational power we have tried to incorporate maximum smoothness as possible by normalizing the image, compressing it, resizing it and also by making sure that only the previous frame gets processed so that the buffer is least and frames per second increases.



<h3>Future Scope</h3>
We aim to extend this implementation to many styles and further do better optimizations to increase the frame rate as well as the resolution. We also aim to make the GUI more user friendly and robust.
We want to deploy this on Android using TensorFlow Lite in future, so that it becomes more wide spread and more easily accessible by the general public.






<hr></hr>

<h2>Installation:</h2>
<h1>• Dependencies:</h1>
<ul>
  <li>OpenCV (opencv-python==3.4.2.17)</li>
  <li>Tkinter</li>
  
</ul>

Then, to run the script from terminal just use:
`python3 tkinterProgram.py`
` 

