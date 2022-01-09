import threading

import matplotlib.pyplot as plt
from fer import FER

count = 0

emotiiGlobal = { "angry":0.0,"disgust":0.0,"fear":0.0,"happy":0.0,"sad":0.0,"surprise":0.0,"neutral":0.0}
#pondere = { "angry":1.0,"disgust":1.0,"fear":1.0,"happy":1.0,"sad":1.0,"surprise":1.0,"neutral":1.0}
pondere = { "angry":1.3,"disgust":2.0,"fear":2.0,"happy":1.0,"sad":2.5,"surprise":1.3,"neutral":1.6}

def maxEmotion(dictionar):
    max = 0
    em = ""
    for x in dictionar:
        dictionar[x] = dictionar[x] * pondere[x]
    for x in dictionar:
         if max < dictionar[x]:
            max = dictionar[x]
            em = x
    return em
    '''
    for x in dictionar:
        emotiiGlobal[x] += dictionar[x]
    '''

def testing(emotion):
    name = emotion + ".txt"
    f = open(name, "r")
    count = 0
    succes = 0
    suma = 0
    for x in f:
        x = x[:-1]
        x = "emotii/" +  emotion+"/"+x

        img = plt.imread(x)
        detector = FER(mtcnn=True)
        emotions = detector.detect_emotions(img)

        for y in emotions:
            count = count+1
            '''
            threads = []
            thread = threading.Thread(target=maxEmotion, args=(y["emotions"]))
            threads.append(x)
            thread.start()
            '''
            if maxEmotion(y["emotions"]) == emotion:
                succes = succes + 1

            #maxEmotion(y["emotions"])

    procent = succes/count * 100
    print(emotion)
    print(procent , "%")
    print()




testing("angry")
#testing("disgust")
testing("fear")
testing("happy")
testing("neutral")
testing("sad")
testing("surprise")