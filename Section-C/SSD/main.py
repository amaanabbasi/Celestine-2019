import numpy as np
from PIL import Image
from sse import SSE
from census import CENSUS

def stereo_match(left_img, right_img, kernel, max_offset):
    # Load in both images, assumed to be RGBA 8bit per channel images
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)
    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)    
    w, h = left_img.size  # assume that both images are same size   
    
    predictions = SSE(left_img, right_img, kernel, max_offset, w, h, left, right)
    
    # CENSUS(left_img, right_img, kernel, max_offset, w, h, left, right) 
    

if __name__ == '__main__':
    stereo_match("im0.png", "im1.png", 5, 30)  # 6x6 local search kernel, 30 pixel search range