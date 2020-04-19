#!/usr/bin/env pyhton3
#importing Essential libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from datetime import datetime as dt

now = dt.now()

def banners(S):
    import sys
    import time
    for x in S:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.0192)
banner = '''
  \   \      /   / ------------
   \   \    /   /  |_______   /
    \   \  /   /          /  /
     \   \/   /          /  /    ________   _______   _
     /   /\   \         /  /    |  ______| |  ___  | | |
    /   /  \   \       /  /     | |        | |   | | | |
   /   /    \   \     /  /      | |______  | |___| | | |______
  /   /      \   \   /  /       |________| |_______| |________|

 Github_@https://github.com/GeneralXS twitter_@https://twitter.com/Muhammad1Nuur 
'''

