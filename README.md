# Imagenetdownload
Script to download images from ImageNet

The first one is temp.py which is the script for downloading images and the second is labelmap.txt which is a text file with the 1000 classes. Please download both the files into the same folder. 
Refer to the labelmap text file to decide which image sets you need. Copy the WNIDs (02077923 (omit the letter n)) and paste it in the script.
Run the temp.py file once you have checked the requirements

Required packages:
1. Beautifulsoup4
2.numpy
3.requests
4.opencv
5.pillow (PIL)
6.urllib3
7.os ,random

1. Imagenet is a collection of image urls (many from flickr) and other websites. They are sorted by their classes (synsets) .The default image sizes vary from image to image. My script saves 256x256 sized images. You can change this to any size you want but if it is bigger than the actual image, it might cause stretching. 
2. the script creates two main folders -[Train and Test] and both will have subfolders of all the synsets(classes) you download. 
3. Currently I have written the script for Komodo Dragons and Digital watches. You can add more WNID (WORDNET ID) e.g.- '01695060' to the wnid list in the starting of the script and that would get you multiple classes.
4. Many images would have been moved/deleted from the original URLs and I skip them this might lead to downloading lesser than your target number. Check folder sizes for true estimates. 
