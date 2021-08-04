import tkinter as  tk
from tkinter import filedialog
from tkinter import *
from PIL import  ImageTk,Image
import numpy as np
import cv2

from keras.models import load_model
model=load_model("model/Sign_Identification_MODEL.h5")

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

# INITIALISE  GUI
top=tk.Tk()
top.geometry('800x600')
top.configure(background="#e6bfb1")
top.title("Traffic Sign Identification")

label=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
sign_image= Label(top)


def classify(file_path):

    img=cv2.imread(file_path)
    imge=cv2.resize(img,(64,64))
    imge=imge.reshape(1,64,64,3)
    imge=imge/255
    imge=np.array(imge)

    predict_values=model.predict([imge])
    print(predict_values)
    maxVal_index=np.argmax(predict_values)
    print(maxVal_index)
    probability = np.amax(predict_values)
    prob = round(probability * 100, 2)
    print(prob)
    # sign=sign_Class[maxVal_index]
    # print(sign)
    for index,value in enumerate(predict_values):
        if value.any()>0.7 and prob>70:
            sign=sign_Class[maxVal_index]
        else:
            sign=str("No signal Identified")
    label.configure(foreground='#011638',text=sign)

def show_classify_button(file_path):
    classify_b=Button(top,text='Classify Image',command=lambda : classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156',foreground="white",font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text='Upload an Image',command=upload_image,padx=10,pady=5)
upload.configure(background='#364156',foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading=Label(top,text="Know your Traffic Sign",pady=15,font=('arial',20,'bold'))
heading.configure(background='#f2e8e6',foreground='#364156')
heading.pack()
top.mainloop()