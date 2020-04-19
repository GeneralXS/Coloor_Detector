#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import cv2
#from skimage.color import rgb2lab, deltaE_cie76
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--image', required=True, dest='image', help ='path to the image')

parser.add_argument('-D','--show', dest='Display', default='chart', choices=['chart', 'bar'], help ='Display chart of detected color')

args = parser.parse_args()
image = args.image
dis = args.Display

def get_image(image_path):
    img = cv2.imread(image)
    print('The Shape: {}'.format(img.shape))
    return img
        
  
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]),int(color[1]),int(color[2]))
    

def get_colors(image,number_of_colors,Display): 
    modified = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified = modified.reshape(modified.shape[0]*modified.shape[1], 3)   
    from sklearn.cluster import KMeans
    clusters = KMeans(n_clusters = number_of_colors)
    cluster = clusters.fit_predict((modified))
    
    from collections import Counter
    counts = Counter(cluster)
    center_color = clusters.cluster_centers_
    order_color = [center_color[i] for i in counts.keys()]
    hex_color = [RGB2HEX(order_color[i]) for i in counts.keys()]
    rgb_color = [order_color[i] for i in counts.keys()]
    from datetime import datetime as dt
    import sys, time
    if (Display == "chart"):
        gen = 'Generating Pie-Chart' + '...'*3 +'\n' 
        for l in gen:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.02)
        plt.figure(figsize = (10, 8))
        plt.pie(counts.values(), labels = hex_color, colors= hex_color)
        plt.title('Colors Detected')
        plt.show()
        return rgb_color
    elif Display == "bar":
        per = [10,20,25,40,60,75,80,100]
        plt.plot(counts.values(),per, color = [hex_color])
        plt.xlabel(hex_color)
        plt.ylabel(per)
        return rgb_color
        

if image:
    pics = get_image(image)
    
    if dis == 'chart':
        get_colors(pics, 8, "chart")
    else:
        get_colors(pics, 8, "bar")
