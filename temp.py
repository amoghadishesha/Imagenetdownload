# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Amogh Adishesha

"""

from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import PIL.Image
import urllib
import os
import random

wnid_list=['01695060','03197337'] #Komodo Dragons and Watches. add more classes here

#%%
f=open('labelmap.txt','r')
content=f.readlines()
contents=[]
for lin in content:
    sub=lin.split(' ')
    contents.append(sub)
contents = [item for sublist in contents for item in sublist]

def label_maker(contents,num):
    # used for naming the folders automatically with human labels
    n='n'+num
    label_str= contents[contents.index(n)+2].replace('\n','')
    return label_str

pathfortrain= r'./content/train' #make folder for saving images. change path if required 
pathfortest= r'./content/test'  #make folder for saving images. change path if required
os.makedirs(pathfortrain, exist_ok=True)
os.makedirs(pathfortest, exist_ok=True)


def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format, Resize it to 256x256
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image= cv2.resize(image,(img_rows,img_cols), interpolation = cv2.INTER_CUBIC)
	# return the image
    return image


#%%
for item in wnid_list:
    name=label_maker(contents,item)
    page_path='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n'+item
    page=requests.get(page_path) #each synset
    soup = BeautifulSoup(page.content, 'html.parser')
    str_soup=str(soup)
    split_urls=str_soup.split('\r\n')
    print("number of images in",name,len(split_urls))
    subpathtrain=os.path.join(pathfortrain,name)
    subpathtest=os.path.join(pathfortest,name)
    os.makedirs(subpathtrain, exist_ok=True)
    os.makedirs(subpathtest, exist_ok=True)
    img_rows, img_cols = 256, 256 #number of rows and columns to convert the images to
    input_shape = (img_rows, img_cols, 3)
    numtrain=100
    numtest=50
    numbers = [i for i in range(len(split_urls))]
    trainidx=random.sample(numbers, numtrain)
    testidx=[]
    while len(testidx)!=numtest:
        s=random.randint(0,len(split_urls))
        if s not in trainidx:
            testidx.append(s)
    c=0
    for unit0 in trainidx:
        c+=1
        urlpointer=split_urls[unit0]
        try:
            I=url_to_image(urlpointer)
            savepath=os.path.join(subpathtrain,(str(c)+'.jpg'))
            cv2.imwrite(savepath,I)
            print(c)
        except:
            None
    c=0
    del unit0
    for unit1 in testidx:
        c+=1
        
        urlpointer=split_urls[unit1]
        try:
            
            I=url_to_image(urlpointer)
            savepath=os.path.join(subpathtest,(str(c)+'.jpg'))
            cv2.imwrite(savepath,I) 
            print(c)
        except:
            None
    del unit1

    
    




