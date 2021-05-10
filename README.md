# Hand-Detection
Hand Detection System utilizing deep learning library from MediaPipe by Google
 
 **CHECK OUT Live Video Output Below !!**

# Input
 * live frame


# Output
 * *Hand detected*
   * Palm detection 
   * 21 point detection 
# Algorithm

* **Palm Detection**

To detect **initial hand locations**, we utlize a *single-shot detector model* optimized for mobile real-time uses
Detecting hands is a decidedly complex task: we use model to work across a variety of hand sizes with a large scale span (~20x) relative to the image frame and be able to  detect occluded and self-occluded hands.

![image](https://user-images.githubusercontent.com/83566027/117607289-48794b80-b179-11eb-8e73-bdcb44870377.png)

* **Hand Landmark Model**

After the palm detection over the whole image our subsequent hand landmark model performs precise keypoint localization of 21 3D hand-knuckle coordinates inside the detected hand regions via regression, that is direct coordinate prediction. The model learns a consistent internal hand pose representation and is robust even to partially visible hands and self-occlusions.
![image](https://user-images.githubusercontent.com/83566027/117607044-cb4dd680-b178-11eb-89f0-a7fbc3030105.png)

# Result
![image](https://user-images.githubusercontent.com/83566027/117607125-efa9b300-b178-11eb-843d-57e696f9e9c4.png)
