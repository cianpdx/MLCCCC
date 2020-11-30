# MLCCCC
Machine Learning Chicken Coop Camera Counter

A Raspberry Pi or similar with a camera is placed in the roost of a chicken coop with a top-down view. At evening time motion sensing is turned on with MotionEye. Images are passed to the ML model to determine if all the chickens are inside the coop. Once they are all inside for some dwell time and confidence, the coop door can be shut for the night using some servo or motor driver output. 

Goal is to close the door as soon as possible after sunset, without trapping any chickens outside. 

classifiertool:
Hack program to help sort images into folders. May or may not be faster than sorting by hand. Many possible improvments, or adapt any of the many ML labelling tools. 

model_generator:
Takes the images and outputs MLCCCC_model. Followed from TF tutorial very closely. 

model_inference: 
Specify a test image and chicken count and confidence can be returned.
