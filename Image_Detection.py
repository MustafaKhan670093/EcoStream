#Import the object detection class
from imageai.Detection import ObjectDetection
import os

#returns a working directory for the actual folder of the file
execution_path = os.getcwd()

#Initialize the detector
detector = ObjectDetection()

#this sets the initial object detection model instance to the pre trained "RetinaNet" model. This was downloaded from a whl
detector.setModelTypeAsRetinaNet()

#Set the model path of the model file we downloaded (the resnet model that uses the COCO database)
detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))

#Load the model
detector.loadModel()

#analyzing the image and then creating a file that highlights the isolated objects in the initial folder
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "input.jpg"),
                                             output_image_path=os.path.join(execution_path , "output.jpg"))

#compare the image to the images stored in the COCO database and find the percentage of similarity
for x in detections:
    print(x["name"] , " : " , x["percentage_probability"] )

#create the new image and store it in the filepath
from IPython.display import Image
Image("output.png")