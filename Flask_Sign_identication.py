from flask import Flask,render_template,Response
import cv2
import numpy as np
from tensorflow.keras.models import load_model

framewidth=800
frameheight=600
brightness= 80

camera=cv2.VideoCapture(0)
camera.set(3,framewidth)   # Here set(3,..) is used for frame width adjustment, Similarly 4,10 used for frame height
camera.set(4,frameheight)  # and brightness adjustment of resulting real time video frame
camera.set(10,brightness)

app=Flask(__name__)

def generate_frame():
    while True:
        succes,frame=camera.read()
        if not succes:
            break
        else:
            model=load_model("model/Sign_Identification_MODEL.h5")
            ret, frame = camera.read()
            img = cv2.resize(frame, (64, 64))
            img = img.reshape(1, 64, 64, 3)
            img = img / 255
            img=np.array(img)

            sign_Class = {
                 0: 'Dangerous DIP',
                 1: 'Horn Prohibited',
                 2: 'Hump',
                 3: 'Left Hair Pin Bend',
                 4: 'Right Hair Pin Bend',
                 5: 'Left_Hand Curve',
                 6: 'Right Hand Curve',
                 7: 'Left Reverse Bend',
                 8: 'Right Reverse Bend',
                 9: 'Loose Gravel',
                 10: 'Narrow Bridge',
                 11: 'No Parking',
                 12: 'No Stopping or Standing',
                 13: 'Pedestrain Crossing',
                 14: 'School Ahead',
                 15: 'Slippery Road',
                 16: 'Speed Limit 50',
                 17: 'Steep Ascent',
                 18: 'Steep Descent',
                 19: 'Stop',
                 20: 'STRAIGHT PROHIBITOR NO ENTRY'
            }

            predict = model.predict([img])
            print(predict)
            max_val_index = np.argmax(predict)
            result = sign_Class[max_val_index]
            print(max_val_index)
            probability = np.amax(predict)
            prob=round(probability*100,2)
            maxv = predict.max()
            print(maxv)

            x,y,w,h=20,25,375,50
            frame=cv2.rectangle(frame,(x,x),(x+w,y+h),(0,0,0),-1)


            for index,value in enumerate(predict):
                print(value)
                if value.any()>0.7 and prob>70:
                    frame=cv2.putText(frame, str(result), (x + int(w / 10), y + int(h / 2)),
                                      cv2.FONT_HERSHEY_SIMPLEX, 0.7,(2, 5, 255), 2)
                    frame=cv2.putText(frame,str("Probability :")+str(prob)+"%",
                            (x + int(w / 10), y + int(h / 2)+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                else:
                    frame=cv2.putText(frame,"No Traffic Sign Identified" , (x + int(w / 10), y + int(h / 2)),
                                      cv2.FONT_HERSHEY_SIMPLEX, 0.7,(2, 255, 5), 2)


                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def home():
    return  render_template('index.html')
@app.route('/video')
def video():
    return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)