import numpy as np
from PIL import Image

targets = np.asarray(Image.open('deptho.png'))
predictions = np.asarray(Image.open('depth.png'))

# Predicted images can have slightly different shape
# So to rectify this code strips rows and columns from the target rows
# to make the shape equal to the predicted image shape
rows, cols = (i-j for i,j in zip(targets.shape, predictions.shape))

targets = targets[rows:,cols:]

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

print(rmse(predictions, targets))    