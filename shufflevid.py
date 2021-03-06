# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:55:39 2019
created by https://github.com/tswart-res/videoscrambler

"""
from pathlib import Path

dirVid = Path('/Users/elise/Downloads/Python/test')  # set this to your directory where the video is (make sure there is only 1 video with the .mp4 extension in here without a '-' in the name). Make sure slash direction is c
videoextension = 'mp4'  # set the video extension here

import os
import fnmatch
import random
import subprocess

asps = []
for root, dirs, files in os.walk(dirVid):
    asps = fnmatch.filter(files, '*-*.{}'.format(videoextension))
    rootname = set(files).difference(asps)
    rootname = fnmatch.filter(rootname, '*.{}'.format(videoextension))
    rootname = str(rootname)
    rootname = rootname[2:len(rootname) - 6]

for index, a in enumerate(asps):
    asps[index] = "file '" + root + '//' + a + "'"

random.shuffle(asps)

# print(asps)
randomordertxt = '{}/{}_RandomisedOrder.txt'.format(root, rootname)
randomorderVid = '{}/{}_RandomisedOrder.{}'.format(root, rootname, videoextension)

with open(randomordertxt, 'w') as file_handler:
    for item in asps:
        file_handler.write("{}\n".format(item))

concat_text = "ffmpeg -f concat -safe 0 -i {} -c copy {}".format(randomordertxt, randomorderVid)

subprocess.check_output(concat_text, shell=True)

## if you then want to convert the video to a different format or strip the audio from the video you can also use ffmpeg with different arguments eg.,

# ffmpeg -i "P000_1.mp4" -vcodec msmpeg4v3 -b:v 4000K -acodec wmav2 -b:a 192K -aspect 4:3 -s 1280x960 -ss 00:00:00 -to 00:10:00 "Part 1 Vid 1.wmv"