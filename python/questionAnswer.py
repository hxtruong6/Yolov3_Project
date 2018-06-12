import darknet
import re
import collections
from functools import reduce
import cv2

typeQ = ["howMany", "whatIs"]
listAnimal = ["dog","horse", "hen", "pig", "sheep", "pecock", "heron", "vulture", "crow", "gibbon", "hedgehog", "monkey", "ant-eater", "chimpanzee", "otter", "rhinoceros", "mongoose", "wolf", "hippopotamus", "yak",  "bull", "moose", "giraffe", "flamingo", "robin", "parrot", "sparrow toucan", "lion", "buffalo", "goat", "tiger", "squirrel", "kangaroo", "mouse", "rabbit", "armdillo", "fox", "koala", "boar"]

def resultImage(imagePath):
    net = darknet.load_net("cfg/yolov3.cfg", "yolov3.weights", 0)
    meta = darknet.load_meta("cfg/coco.data")
    r = darknet.detect(net, meta, imagePath)
    resIm = []
    for rr in r:
        resIm.append(rr[0])
    print(resIm)
    return resIm

def howMany(qs, keyWords, resIm):
    print(qs.lower().capitalize())
    counter = collections.Counter(resIm)

    if keyWords[0] == "people":        
        if counter["person"]>1:
            print("There are "+ str(counter["person"]) + " people.")
        else:
            print("There is "+ str(counter["person"]) + " people.")
    
    elif "animals" in keyWords or "animal" in keyWords:
        listRes = counter.keys()
        #print(listRes)
        count = 0
        for k in listRes:
            if k in listAnimal:
                count += counter[k]
                print(str(counter[k])+ " "+ str(k))
        print("There are "+ str(count)+ " animals.")
    elif ("object" or "objects" or "things" or "thing" ) in keyWords:
        print("There are " + str(reduce(lambda x, y: x + y, counter.values()))+ " objects in the image.")
    

def whatIs(qs, keyWords, resIm):
    print(qs.lower().capitalize())
    res = list(set(val for val in resIm))
    if (len(res)>1):
        print("That are "+ res[0]+ ", ")
        for rr in res[1:len(res)-2]:
            print( rr + ", ")
        print(res[len(res)-2] + " and "+ res[len(res)-1] + ".")
    else:
        print("That is "+ res[0] + ".")

def typeQuestion(qs):
    words = []
    words = re.findall(r"[\w']+",qs.lower())
    # for w in words:
    #     print(w)

    keyWords = []
    if "how" in words and "many" in words:
        _type = typeQ[0] 
    	#print("return number")
    elif "what" in words:
        _type = typeQ[1]
    	#print("return object")

    for w in words:
    	if w in {"people", "animal", "animals", "that", "object", "objects", "things", "thing"}:
    		keyWords.append(w)
    print( str(_type) + " " + str(keyWords))
    return _type, keyWords

def answerIm(imagePath, qs):
    _type, keyWords = typeQuestion(qs)
    resIm = resultImage(imagePath)
    if _type == "howMany":
        howMany(qs, keyWords, resIm)
    elif _type == "whatIs":
        whatIs(qs, keyWords, resIm)

if __name__ == "__main__":
	#typeQuestion("What THE FucK?")
	#typeQuestion("HoW ManY THE FucK?")
    #imagePath = "/media/hxtruong/Data/College/HK_IV/Research_Paper/Yolov3/darknet/data/2007_000762.jpg"
    imagePath = "/media/hxtruong/Data/College/HK_IV/Research_Paper/Yolov3/darknet/data/person.jpg"
    #qs = "HoW ManY people in there?"
    qs = "HoW ManY object in there?"
    #qs = "What is that?"
    answerIm(imagePath, qs)

    # Show image
    cv2.imshow("Image",cv2.imread(imagePath))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
