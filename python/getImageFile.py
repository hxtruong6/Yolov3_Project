from os import listdir
from os.path import isfile, join

def getFiles(mypath):
	#mypath = "/media/hxtruong/Data/College/HK_IV/Research_Paper/Yolov3/darknet/VOCdevkit/PersonDataset"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	#print(onlyfiles)
	return onlyfiles

if __name__ == "__main__":
	mypath = "/media/hxtruong/Data/College/HK_IV/Research_Paper/Yolov3/darknet/VOCdevkit/PersonDataset"
	files = getFiles(mypath)
	print(files)