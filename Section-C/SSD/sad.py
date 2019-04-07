import numpy as np
from PIL import Image

left_img = 'im0.png'
right_img = 'im1.png'

left_img = Image.open(left_img).convert('L')
left_img = np.asarray(left_img)

right_img = Image.open(right_img).convert('L')
right_img = np.asarray(right_img)    

disp = 200
h, w = left_img.shape
disp_map = np.zeros((w, h), np.uint8)

for j in range(h):
    for i in range(w):
        tmp = 1000000
        for d in range(disp):
            if i+d >= w:
                continue  
            ad = np.sum(abs(left_img[j,i] - right_img[j,i+d]))
            if ad < tmp:
                tmp = ad
                disp_map[j,i] = d
print(tmp)