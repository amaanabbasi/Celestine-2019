import numpy as np
from PIL import Image

iname = 'im0.png'
oname = 'depth1.png'



src_img = Image.open(iname).convert('L')
w, h = src_img.size

#Convert image to Numpy array
src_bytes = np.asarray(src_img)

#Initialize output array
census = np.zeros((h-2, w-2), dtype='uint8')

#centre pixels, which are offset by (1, 1)
cp = src_bytes[1:h-1, 1:w-1]

#offsets of non-central pixels 
offsets = [(u, v) for v in range(3) for u in range(3) if not u == 1 == v]

#Do the pixel comparisons
for u,v in offsets:
    census = (census << 1) | (src_bytes[v:v+h-2, u:u+w-2] >= cp)

#Convert transformed data to image
print(census.shape)
Image.fromarray(census).save('depth1.png')