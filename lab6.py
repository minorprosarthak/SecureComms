#!/usr/bin/env python3
"""Recover the picture hidden in an AES-ECB encrypted BMP WITHOUT the key.

Usage: python3 ecb_unscramble.py aes_bmp.enc [out.png]

Idea: ECB maps equal 16-byte plaintext blocks to equal ciphertext blocks, so the
*equality pattern* of the ciphertext blocks reproduces the shape of the image.
"""
import sys
from collections import Counter
import numpy as np
from PIL import Image

HDR, W, H = 54, 640, 480            # BMP header size; width/height inferred from file size
src = sys.argv[1] if len(sys.argv) > 1 else "aes_bmp.enc"
dst = sys.argv[2] if len(sys.argv) > 2 else "aes_ecb_recovered.png"

data = open(src, "rb").read()
assert len(data) == HDR + W * H * 3, "unexpected size - re-derive W,H (see report)"

# 1. split into 16-byte AES blocks (the trailing 6 bytes are an incomplete block, ignored)
nb = len(data) // 16
blocks = [data[i * 16:(i + 1) * 16] for i in range(nb)]

# 2. most frequent block = encryption of 16 x 0xFF (white background)
background = Counter(blocks).most_common(1)[0][0]

# 3. label every distinct block with an arbitrary grey level, background = white
label, grey = {}, np.empty(nb, dtype=np.uint8)
for i, b in enumerate(blocks):
    grey[i] = 255 if b == background else 60 + (label.setdefault(b, len(label)) * 37) % 150

# 4. place each pixel (3 bytes: B,G,R) at its true file offset to find its block
offset = HDR + np.arange(W * H) * 3
pix = grey[np.minimum(offset // 16, nb - 1)].reshape(H, W)

# 5. BMP rows are stored bottom-up -> flip vertically
Image.fromarray(pix[::-1]).save(dst)
print("wrote", dst, "| blocks:", nb, "| distinct:", len(set(blocks)))
