import PySimpleGUI as sg
import cv2
import matplotlib.pyplot as plt
from fer import FER

cat = 0

emotii = {
  "angry": 0.00,
  "disgust": 0.00,
  "fear": 0.00,
  "happy": 0.00,
  "sad": 0.00,
  "surprise": 0.00,
  "neutral": 0.00,
}
def medie_emotii(frame):
    cv2.imwrite('Frame' + '.jpg', frame)
    #image = Image.open('Frame.jpg')
    #image.show()

    img = plt.imread("Frame.jpg")
    detector = FER(mtcnn=True)
    print(detector.detect_emotions(img))
    plt.imshow(img)


def mainWindow():
    sg.theme('Black')

    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Stop', size=(10, 1), font='Helvetica 14'), ]]

    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(800, 400))

    cap = cv2.VideoCapture(0)
    recording = False
    takePicture = False
    x=0

    while True:
        event, values = window.read(timeout=20)
        if event == sg.WIN_CLOSED:
            return
        elif event == 'Record':
            recording = True
        elif event == 'Stop':
            emotiePredominanta=emotii();
            sg.Popup(emotiePredominanta, keep_on_top=True)
        if recording:
            ret, frame = cap.read()

            if(x==20):
                medie_emotii(frame)
                x=0

            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            if (takePicture):
                takePicture = False
            x=x+1


            window['image'].update(data=imgbytes)

def emotii():
    return "Fericit"