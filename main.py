import os, re

filepath = os.path.dirname(__file__).join(['testdata/'])
finishedpath = os.path.dirname(__file__).join(['finished/'])
files = os.listdir('./testdata')

for file in files:
    file = file.lower()
    re.sub('german|x265|x264|hevc|ac3|hdr|webdl|web.*dl|1080p|720p|480p|2160p|fullhd|eac3|web','', file)
    print(file)
