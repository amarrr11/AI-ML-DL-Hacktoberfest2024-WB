# Import necessary libraries 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

# Create 20 data points randomly on the 2-D plane. 
# Data_points are random points located on the 2D plane. 
Data_points = np.random.randint(0, 50, (20, 2)).astype(np.float32) 

# Label the data points with their class labels. 
labels = np.random.randint(0, 2, (20, 1)).astype(np.float32) 
# labels are the classes assigned to data points. 

# Take the yellow class for 0 label and magenta class for 1 label 
yellow = Data_points[labels.ravel()== 0] 
magenta = Data_points[labels.ravel()== 1] 

# Plot the classes on the 2-D plane 
# o for circle 
plt.scatter(yellow[:, 0], yellow[:, 1], 80, 'y', 'o') 
# s for square 
plt.scatter(magenta[:, 0], magenta[:, 1], 80, 'm', 's') 
plt.show() 
