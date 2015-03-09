import os
rootdir = 'D:\k\Projects\LessonsAudio'

for subdir, dirs, files in os.walk(rootdir):
        for file in files:
                print os.path.join(subdir, file)
                print subdir
                print file
                break
