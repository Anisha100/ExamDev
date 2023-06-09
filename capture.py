# program to capture single image from webcam in python

import cv2 as cv
from PIL import Image
import os
import glob
# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
# importing OpenCV library
from flask import flask
app=Flask(__name__)
@ap.route("/downloads", methods=['GET,'POST'])
def home():
  
	cam_port = 0
	cam = cv.VideoCapture(cam_port)
	mylist=[]
	for x in range(4):
 
		# reading the input using the camera
		result, image = cam.read()
		img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		pil_image = Image.fromarray(img)
		mylist.append(pil_image)

	mylist[0].save(
    	"test.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=mylist[1:]
	)
		
	return send_from_directory("test.pdf")
if __name__=="__main__":
	app.run(debug=True)	

	
	
	
	
	
	
	
	