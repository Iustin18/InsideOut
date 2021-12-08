import PySimpleGUI as sg
import cv2
import mainWindow
import face_recognition

def verifyFacialRecogn(frame):
    cv2.imwrite('Frame2' + '.jpg', frame)
    picture_of_me = face_recognition.load_image_file("Frame2.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    pictureM = face_recognition.load_image_file("mihai1.png")
    encodingM = face_recognition.face_encodings(pictureM)[0]

    pictureI = face_recognition.load_image_file("iustin1.png")
    encodingI = face_recognition.face_encodings(pictureI)[0]

    resultsM = face_recognition.compare_faces([my_face_encoding], encodingM)
    resultsI = face_recognition.compare_faces([my_face_encoding], encodingI)

    if resultsM[0] == True:
        return "Mihai"
    elif resultsI[0] == True:
        return "Iustin"
    else:
        return 0

def registerEncoding(frame):
    cv2.imwrite('Frame2' + '.jpg', frame)
    picture_of_me = face_recognition.load_image_file("Frame2.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    print(my_face_encoding)



def main():

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Login', size=(10, 1), font='Helvetica 14'),
               sg.Button('Register', size=(10,1),font='Helvetica 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(800, 400))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    recording = False
    takePicture = False
    register= False
    while True:
        event, values = window.read(timeout=20)
        if event == 'Login':
            takePicture=True
        if event == sg.WIN_CLOSED:
            return
        elif event == 'Record':
            recording = True

        if event == 'Register':
            register = True

        if recording:
            ret, frame = cap.read()
            img = cv2.imencode('.png', frame)[1]
            imgbytes = img.tobytes()  # ditto
            if(register):
                registerEncoding(frame)
                register = False
            if(takePicture):
                takePicture=False
                ret = verifyFacialRecogn(frame)
                if ret==0:
                    sg.PopupOK('User necunoscut', keep_on_top=True)
                else:
                    sg.PopupOK(ret + ' ai fost logat, Welcome', keep_on_top=True)
                    window.close()
                    return 1

            window['image'].update(data=imgbytes)



if main()==1:
    mainWindow.mainWindow()




