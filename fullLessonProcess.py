import os
import sys
import glob
import shutil
import time
from subprocess import call


def main (): 
	# file location to check
	#directorySource = 'D:\k\Projects\LessonsAudio'
	directorySource = 'G:\STEREO\FOLDER03'
	
	# file destination
	#directoryDestination = 'D:\k\Projects\LessonsAudio'
	directoryDestination = 'D:\k\Projects\LessonsAudio\Testing'
	
	
	instructor = 'BobGoins'
	className = 'FretboardTheory'
	
	
	# files I'm looking for
	mask='{}\*[0-9].wav'.format(directorySource)     # this is for SD card
	#mask='{}\\15*[0-9].wav'.format(directorySource)  # this is for hard drive
	
	print mask
	
	
	for pathSource in glob.glob(mask):
	  
		print pathSource
	  
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
	
		pathDestination      = directoryDestination + os.path.sep + fileNameDestination + '.wav'
		pathLevelatedFile    = directoryDestination + os.path.sep + fileNameDestination + '.output.wav'
		pathLevelatedMp3File = directoryDestination + os.path.sep + fileNameDestination + '.output.mp3'
		pathSave        = directoryDestination + os.path.sep + 'Save' 
		pathSaveFile    =             pathSave + os.path.sep + fileNameFull
		print "\n"
		print "      source = %s" % pathSource
		print " destination = %s" % pathDestination
		print "   levelated = %s" % pathLevelatedFile
		print " evelatedMp3 = %s" % pathLevelatedMp3File
		print "    pathSave = %s" % pathSave
		print "pathSaveFile = %s" % pathSaveFile

		break
	
		shutil.copyfile(pathSource,pathDestination)
	
		# This is saving the original in paranoia, first line moves it, second copies it
		# Eventually put first one back and then zip likely.
		shutil.copyfile(pathSource,pathSaveFile)
		#shutil.move(pathSource,pathSave)  # this 
	
	print "\n"
	sys.stdout.flush()
	#call("ls")
	
	# Here had to mirror the images folder from levelator to make this work. Oof.
	call("levelatorCmdLine.exe %s" % pathDestination)
	
	
	# Here we convert to mp3 file
	call("lame --quiet -q0 -b320 %s %s" % (pathLevelatedFile, pathLevelatedMp3File) )
	
	print "\n"

if __name__ == '__main__':
	main()


