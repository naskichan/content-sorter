#!/usr/bin/env python3

import os, re

#filepath = os.path.dirname(__file__)
#finishedpath = os.path.dirname(__file__).join(['finished/'])
filepath = os.getcwd()
print('listing all files in '+filepath)
files = os.listdir(filepath)

changes = {}

def toUpper(obj):
    char_elem = obj.group(0)
    return char_elem.upper()

for file in files:
    original = file
    file = file.lower()
    file = re.sub('german|.265|.264|hevc|ac3|hdr|webdl|web.*dl|1080p|720p|480p|2160p|fullhd|eac3|web|aac|bluray|dubbed|ger\S{3}sub|4sf|dts|dl','', file)
    file = re.sub('\.(?=[^.]*\.)', '-', file)
    file = re.sub(' ', '-', file)
    file = re.sub('-{2,}', '-', file)
    file = re.sub('^-|', '', file)
    file = re.sub('(?<=\d-)(.*)(?=\..{3}$)', '', file)
    file = re.sub('-\.', '.', file)
    file = re.sub('.\d{1,2}', toUpper, file)
    file = re.sub('(?<=[A-Z])(?=\d[A-Z.])', '0', file)
    changes[original] = file

changes = sorted(changes.items(), key=lambda item: item[1])
for k,v in changes:
    print('mv \u001b[31m{}\u001b[0m \n\t to \u001b[32m{}\u001b[0m'.format(k,v))

print('Totaling '+str(len(changes))+' elements')
key = input('does that sound fine to you? Type y to execute\n')

if(key == 'y'):
    print("ok less go!")
    for k,v in changes:
        source = ''.join([filepath, '/', k])
        target = ''.join([filepath, '/', v])
        os.rename(source, target)
else:
    print('aborting')