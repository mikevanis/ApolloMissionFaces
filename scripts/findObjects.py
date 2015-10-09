import numpy as np
import cv2
import sys
import glob, os

usage = """Correct usage: python findObjects.py /path/to/images haarcascade.xml /path/to/output"""

numOfResults = 0
numOfFiles = 0

def drawObjects(objects, frame):
	for(x,y,w,h) in objects:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

	return frame

# make sure we have enough arguments
if len(sys.argv) < 3:
	print >> sys.stderr, usage
	sys.exit(1)

# if fifth argument is present, set saveResults flag
saveResults = False
if len(sys.argv) == 4:
	saveResults = True
	outputPath = sys.argv[3]

haarcascade = sys.argv[2]
objectCascade = cv2.CascadeClassifier(haarcascade)

# find all images in directory
prevDirectory = os.getcwd()
searchPath = sys.argv[1]
os.chdir(searchPath)

# go through them one by one
for file in glob.glob("*.jpg"):
	numOfFiles += 1
	print("looking at " + file)
	
	img = cv2.imread(file, 1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	objects = objectCascade.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize=(30,30),
		flags=cv2.CASCADE_SCALE_IMAGE
	)
	if len(objects) > 0:
		print("result found!")
		numOfResults += 1
		if saveResults == True:
			os.chdir(prevDirectory)
			if not os.path.exists(outputPath):
				os.makedirs(outputPath)
			result = drawObjects(objects, img)
			cv2.imshow("result", result)
			cv2.imwrite(outputPath + file, result)
			print("result saved.")
			os.chdir(searchPath)

# print number of objects found
print("processed " + `numOfFiles` + " images.")
print("number of results: " + `numOfResults`)
