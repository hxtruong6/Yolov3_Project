import darknet 
import getImageFile

path = "/media/hxtruong/Data/College/HK_IV/Research_Paper/Yolov3/darknet/VOCdevkit/PersonDataset"
imageFiles = getImageFile.getFiles(path)

net = darknet.load_net("cfg/yolov3.cfg", "yolov3.weights", 0)
meta = darknet.load_meta("cfg/coco.data")
resultPath = "/media/hxtruong/Data/College/HK_IV/Research_Paper/Yolov3/darknet/VOCdevkit/PersonDataset/Result"

for i in imageFiles:
	# str(path + '/' + i) : path of each image in folder
    res = darknet.detect(net, meta, str(path + '/' + i))
    fi = open(str(resultPath + '/' + i[:len(i)-3] + 'txt'),"w+")
	#fi.write("Name Prob X Y Width Height\n")
    for r in res:
    	temp = r[0] + " " + str(round(r[1] * 100,2)) + " " + str(round(r[2][0],2)) + " " + str(round(r[2][1],2)) + " " + str(round(r[2][2],2)) + " " + str(round(r[2][3],2))
        print(temp)
        fi.write(temp + '\n')
    fi.close()
    print ''