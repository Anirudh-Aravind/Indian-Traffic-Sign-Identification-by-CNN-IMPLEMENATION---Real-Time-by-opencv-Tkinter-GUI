# Indian Traffic Sign Identification by CNN : Implementation -> Real Time by opencv / Tkinter GUI

Real time Identification of Indian traffic signs by openCV and show which class that traffic sign belongs to by using Keras and Deep Learning 2D convolution layer and deployed as web app by Flask web framework and also a shows a simple tkinter GUI using the same model


## Output for Flask API
<img width="880" alt="2021-08-03 (5)" src="https://user-images.githubusercontent.com/84184475/128228106-e50ddc33-284a-4654-8da5-7b60021f3477.png"><img width="829" alt="2021-08-03 (8)" src="https://user-images.githubusercontent.com/84184475/128228214-1581d3a4-dd62-4484-9062-92a0c16a9ec2.png"><img width="807" alt="2021-08-03 (6)" src="https://user-images.githubusercontent.com/84184475/128228246-bd848298-0f3c-428c-9a10-6544c1da51c3.png">

## Output for tkinter GUI
<img width="598" alt="TksteepDesc" src="https://user-images.githubusercontent.com/84184475/128228489-b8cd3e21-d1ad-4914-970a-ad2364408fbd.png">

### Over view
Here in this project used 21 Traffic Sign classes present in India. And each class consist only around 100-200 images, So the output is not always showing correct result beacuse of this small volume of data. Even though if the model trained with sufficient amount of data it gives more accurate result. 

## Steps followed

### 1. Data Collection
Here takes 21 traffic sign classes present in India. This data collected from google by searching the Traffic sign name , eg:  stop traffic sign in India . But output is not satisfying  because it shows only 10-20 images of stop traffic sign and remaining  others are different signs. So to overcome that used a technique called 'Data Augmentation',  by using this can increase the amount of data by adding slightly modified copies of already existing data. This manner created a dataset consisting 21 classes and each class contain around 100-200 images.
Program Code ---> Image_Augmentation.ipynb

### 2. Model Training
Model is created by using CNN and model trained with images of pixels size 64x64. The used traffic signs and their count are shown below.

![image](https://user-images.githubusercontent.com/84184475/128230738-e95fe151-d387-4f5e-a5ee-efdd95120280.png)



While testing it shows accurate result with validation images

![image](https://user-images.githubusercontent.com/84184475/128230933-47788c9e-6f8d-425f-9355-9b09ca6c9b25.png)


Program Code  ---> TR_Sign_Model.ipynb


### 3. Implementation using Flask API and tkinter GUI 
Flask is a micro web framework written in Python that allows us to build up web-applications.

Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.

For run the implementation code arrange the files in the follwing order

<img width="188" alt="File_save" src="https://user-images.githubusercontent.com/84184475/128232160-c1bf437c-585a-4f03-9829-84132c1f75cc.png">




# you can download the dataset from the below link
https://drive.google.com/drive/folders/1wU5yopEV6NnNFSeXSG9hx-QKe65Ea0-I?usp=sharing



# you can download the Trained Model from the below link
https://drive.google.com/file/d/19-X6jyaWEvVucq5jogK6w9YOUJIdEsF4/view?usp=sharing
