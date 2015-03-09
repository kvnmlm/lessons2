import os
import glob
import shutil
import time

# file location to check
directorySource = 'D:\k\Projects\LessonsAudio'
#directorySource = 'G:\STEREO\FOLDER03'

# file destination
directoryDestination = 'D:\k\Projects\LessonsAudio'


instructor = 'BobGoins'
className = 'FretboardTheory'


# files I'm looking for
mask='{}\*[0-9].wav'.format(directorySource)


for pathSource in glob.glob(mask):
  
	#print pathSource
  
	(dirName, fileNameFull) = os.path.split(pathSource)
	#print dirName
	#print fileNameFull
	
	fileName, extension = fileNameFull.split('.')
	#print fileName
	#print extension
	
	dateStr, timeStr = fileName.split('-')
	#print timeStr
	#print dateStr

	day = dateStr[-2:]
	#print day

	#month = dateStr[-4:-2]
	month = dateStr[2:4]
	#print month

	year_2_digits = dateStr[:2]
	#print year_2_digits

	year = "20" + year_2_digits
	#print year

	dateWithDashes = year +  '-' + month + '-' + day
	#print dateWithDashes

	fileNameDestination = dateWithDashes + '-' + className + '-' + instructor
	#print fileNameDestination

	pathDestination = directoryDestination + os.path.sep + fileNameDestination + '.wav'
	print "\n"
	print "     source = %s" % pathSource
	print "destination = %s" % pathDestination

	#shutil.copyfile(pathSource,pathDestination)

	#break

print "\n"
