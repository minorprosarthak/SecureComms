#!/usr/bin/env python3 
from PIL import Image 
from collections import Counter 
import numpy as np 
data = open('aes_bmp.enc', 'rb').read() 
blocks = [data[i:i+16] for i in range(0, len(data), 16)] 
background = Counter(blocks).most_common(1)[0][0] 
pixels = b''.join(b'\xff' * 16 if b == background else b'\x78' * 
16 for b in blocks) 
img = np.frombuffer(pixels[54:54 + 640*480*3], 
dtype=np.uint8).reshape(480, 640, 3).min(axis=2) 
img = np.roll(img, -8, axis=1)[::-1] 
Image.fromarray(img).save('result.png')
