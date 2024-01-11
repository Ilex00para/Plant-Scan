import cv2
import matplotlib.pyplot as plt
import os 

directory = "C:/Users/jacob/OneDrive/Desktop/Master/Thesis/Plant-Scan/raw_leaflet_scans"

def loop_through_scans(directory):
    files = os.listdir(directory)
    return files

def read_the_image():
    files = loop_through_scans(directory)
    for image_name in files:
        # Load the image
        image = cv2.imread(str(image_name))
        # Display the image
        plt.imshow(image)
        plt.show()

read_the_image()