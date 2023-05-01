# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2, imutils, urllib.request, time
import numpy as np
import pyshine as ps
import os

# Load CV2 CasadeClassifier
try:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
except Exception as e:
    print('Error: ',e)


# Load Yolo (change accoridng to location of files)
net = cv2.dnn.readNet(r"/home/muse/Desktop/workspace/esp32cam-interface/yolo/yolov4-tiny.weights",
                      r"/home/muse/Desktop/workspace/esp32cam-interface/yolo/yolov4-tiny.cfg") 
classes = []
with open("/home/muse/Desktop/workspace/esp32/yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.face_btn = QtWidgets.QPushButton(self.centralwidget)
        self.face_btn.setGeometry(QtCore.QRect(10, 550, 221, 41))
        self.face_btn.setAutoFillBackground(False)
        self.face_btn.setObjectName("face_btn")
        self.obj_btn = QtWidgets.QPushButton(self.centralwidget)
        self.obj_btn.setGeometry(QtCore.QRect(270, 550, 221, 41))
        self.obj_btn.setObjectName("obj_btn")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(830, 50, 131, 31))
        self.close_btn.setObjectName("close_btn")
        self.pic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pic_btn.setGeometry(QtCore.QRect(830, 110, 131, 31))
        self.pic_btn.setObjectName("pic_btn")
        self.brt_slider = QtWidgets.QSlider(self.centralwidget)
        self.brt_slider.setGeometry(QtCore.QRect(820, 200, 71, 271))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.brt_slider.setFont(font)
        self.brt_slider.setOrientation(QtCore.Qt.Vertical)
        self.brt_slider.setObjectName("brt_slider")
        self.blur_slider = QtWidgets.QSlider(self.centralwidget)
        self.blur_slider.setGeometry(QtCore.QRect(910, 200, 71, 271))
        self.blur_slider.setOrientation(QtCore.Qt.Vertical)
        self.blur_slider.setObjectName("blur_slider")
        self.brtLabel = QtWidgets.QLabel(self.centralwidget)
        self.brtLabel.setGeometry(QtCore.QRect(820, 470, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.brtLabel.setFont(font)
        self.brtLabel.setObjectName("brtLabel")
        self.blurLabel = QtWidgets.QLabel(self.centralwidget)
        self.blurLabel.setGeometry(QtCore.QRect(930, 470, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.blurLabel.setFont(font)
        self.blurLabel.setObjectName("blurLabel")
        self.frame_box = QtWidgets.QLabel(self.centralwidget)
        self.frame_box.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.frame_box.setText("")
        self.frame_box.setPixmap(QtGui.QPixmap("../images/dogs2.jpg"))
        self.frame_box.setScaledContents(True)
        self.frame_box.setObjectName("frame")
        self.cif_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cif_btn.setGeometry(QtCore.QRect(670, 52, 118, 33))
        self.cif_btn.setObjectName("cif_btn")
        self.vga_btn = QtWidgets.QPushButton(self.centralwidget)
        self.vga_btn.setGeometry(QtCore.QRect(670, 91, 118, 33))
        self.vga_btn.setObjectName("vga_btn")
        self.svga_btn = QtWidgets.QPushButton(self.centralwidget)
        self.svga_btn.setGeometry(QtCore.QRect(670, 130, 118, 33))
        self.svga_btn.setObjectName("svga_btn")
        self.red_btn = QtWidgets.QPushButton(self.centralwidget)
        self.red_btn.setGeometry(QtCore.QRect(670, 232, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.red_btn.setFont(font)
        self.red_btn.setObjectName("red_btn")
        self.green_btn = QtWidgets.QPushButton(self.centralwidget)
        self.green_btn.setGeometry(QtCore.QRect(670, 271, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.green_btn.setFont(font)
        self.green_btn.setObjectName("green_btn")
        self.blue_btn = QtWidgets.QPushButton(self.centralwidget)
        self.blue_btn.setGeometry(QtCore.QRect(670, 310, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.blue_btn.setFont(font)
        self.blue_btn.setObjectName("blue_btn")
        self.firebase_btn = QtWidgets.QPushButton(self.centralwidget)
        self.firebase_btn.setGeometry(QtCore.QRect(540, 550, 221, 41))
        self.firebase_btn.setObjectName("firebase_btn")
        self.resolution_label = QtWidgets.QLabel(self.centralwidget)
        self.resolution_label.setGeometry(QtCore.QRect(670, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.resolution_label.setFont(font)
        self.resolution_label.setObjectName("resolution_label")
        self.special_label = QtWidgets.QLabel(self.centralwidget)
        self.special_label.setGeometry(QtCore.QRect(670, 200, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.special_label.setFont(font)
        self.special_label.setObjectName("special_label")
        self.vflip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.vflip_btn.setGeometry(QtCore.QRect(670, 390, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.vflip_btn.setFont(font)
        self.vflip_btn.setObjectName("vflip_btn")
        self.hflip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hflip_btn.setGeometry(QtCore.QRect(670, 430, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.hflip_btn.setFont(font)
        self.hflip_btn.setObjectName("hflip_btn")
        self.none_btn = QtWidgets.QPushButton(self.centralwidget)
        self.none_btn.setGeometry(QtCore.QRect(670, 470, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.none_btn.setFont(font)
        self.none_btn.setObjectName("none_btn")
        self.negative_btn = QtWidgets.QPushButton(self.centralwidget)
        self.negative_btn.setGeometry(QtCore.QRect(670, 350, 118, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.negative_btn.setFont(font)
        self.negative_btn.setObjectName("negative_btn")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(20, 520, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''
            ALL CHANGES ARE BELOW
        '''
        # Styling buttons
        self.frame_box.setStyleSheet('border: 2px solid black;')
        self.obj_btn.setStyleSheet("background-color : yellow")
        self.face_btn.setStyleSheet("background-color : yellow")
        self.firebase_btn.setStyleSheet("background-color : yellow")
        
        # Setup 
        self.cap = cv2.VideoCapture(0)
        self.font = cv2.FONT_HERSHEY_PLAIN
        self.starting_time = time.time()
        self.filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        self.frame = None
        self.temp_frame = None

        # Change base_url according to your camera server
        self.base_url = 'http://10.0.0.170/'
        
        self.res_url = {'cif' : self.base_url + 'control?var=framesize&val=5', 
                    'vga': self.base_url + 'control?var=framesize&val=6',
                    'svga': self.base_url + 'control?var=framesize&val=7'}
        
        self.base_vfx_url = self.base_url + 'control?var=special_effect&val='
        self.vfx_url = {
            'none' : '0',
            'negative' : '1',
            'red'  : '3',
            'green' : '4',
            'blue' : '5',
        }
        # Status of effects
        self.hflipped = False
        self.vflipped = False
        self.mirrored = False
        
        # Status of camera
        self.f_detect = False
        self.o_detect = False
        self.active = False
        
        # Capture and current resolution of camera
        self.current_res = self.res_url.get('cif')
        self.capture_url = self.base_url + 'capture'

        self.blur_val = 0
        self.brt_val = 0
        self.frame_id = 0

        # Camera index: 0  for webcam and 1 for ESP32-Cam
        self.indx = 1

        # Button hooking to functions
        self.face_btn.clicked.connect(self.face_detection)
        self.obj_btn.clicked.connect(self.object_detection)
        self.close_btn.clicked.connect(self.release_capture)
        self.blur_slider.valueChanged['int'].connect(self.blur_value)
        self.brt_slider.valueChanged['int'].connect(self.brt_value)
        self.firebase_btn.clicked.connect(self.firebase_update)
        self.cif_btn.clicked.connect(lambda : self.change_res('cif'))
        self.vga_btn.clicked.connect(lambda : self.change_res('vga'))
        self.svga_btn.clicked.connect(lambda : self.change_res('svga'))
        self.negative_btn.clicked.connect(lambda : self.change_vfx('1'))
        self.red_btn.clicked.connect(lambda : self.change_vfx('3'))
        self.green_btn.clicked.connect(lambda : self.change_vfx('4'))
        self.blue_btn.clicked.connect(lambda : self.change_vfx('5'))
        self.none_btn.clicked.connect(self.no_effect)
        self.vflip_btn.clicked.connect(self.vflip)
        self.hflip_btn.clicked.connect(self.hflip)
        self.pic_btn.clicked.connect(self.take_pic)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ESP32 Interface"))
        self.face_btn.setText(_translate("MainWindow", "Start Face Detection"))
        self.obj_btn.setText(_translate("MainWindow", "Start Object Detection"))
        self.close_btn.setText(_translate("MainWindow", "Close"))
        self.pic_btn.setText(_translate("MainWindow", "Take Picture"))
        self.brtLabel.setText(_translate("MainWindow", "Brightness"))
        self.blurLabel.setText(_translate("MainWindow", "Blur"))
        self.cif_btn.setText(_translate("MainWindow", "CIF (400x296)"))
        self.vga_btn.setText(_translate("MainWindow", "VGA(640X480)"))
        self.svga_btn.setText(_translate("MainWindow", "SVGA(800x600)"))
        self.red_btn.setText(_translate("MainWindow", "Red Tint"))
        self.green_btn.setText(_translate("MainWindow", "Green Tint"))
        self.blue_btn.setText(_translate("MainWindow", "Blue Tint"))
        self.firebase_btn.setText(_translate("MainWindow", "Capture and Save to Firebase"))
        self.resolution_label.setText(_translate("MainWindow", "Resolution"))
        self.special_label.setText(_translate("MainWindow", "Special Effects"))
        self.vflip_btn.setText(_translate("MainWindow", "V-Flip"))
        self.hflip_btn.setText(_translate("MainWindow", "H-Flip"))
        self.none_btn.setText(_translate("MainWindow", "No Effect"))
        self.negative_btn.setText(_translate("MainWindow", "Negative"))
        self.main_label.setText(_translate("MainWindow", "Main Controls"))
    
    # Capture function using camera index
    def capture(self, indx):
        if indx == None:
            return
        elif indx == 0: # Webcam
            _, self.frame = self.cap.read()
        elif indx == 1: # ESP32-Cam
            imgResp = urllib.request.urlopen(self.capture_url)
            imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
            self.frame = cv2.imdecode(imgNp, -1)
        else:
            print("Error: No Capture Source Available")
    
    # Update current frame function
    def update_frame(self, img):
        self.temp_frame = img
        img = imutils.resize(img,width=761)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        kernel_size = (self.blur_val+1, self.blur_val+1)
        frame = cv2.blur(frame, kernel_size)
        frame = self.change_brt(frame, self.brt_val)
        img = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.temp_frame = imutils.resize(frame,width=640)
        self.temp_frame = cv2.cvtColor(self.temp_frame, cv2.COLOR_BGR2RGB)
        self.frame_box.setPixmap(QtGui.QPixmap.fromImage(img))

    # Object detection function
    def object_detection(self):
        # Checks if object and or face detection is active
        if self.o_detect:
            self.o_detect = False
            self.obj_btn.setText("Start Object Detection")
            self.obj_btn.setStyleSheet("background-color : yellow")
        else:
            self.f_detect = False
            self.o_detect = True
            self.face_btn.setText("Start Face Detection")
            self.face_btn.setStyleSheet("background-color : yellow")
            self.obj_btn.setText("Stop Object Detection")
            self.obj_btn.setStyleSheet("background-color : red")       

        while self.o_detect:
            # Process all pending events
            QtWidgets.QApplication.processEvents()
            # Capture if current frame is None
            if self.frame is None:
                self.capture(self.indx)
            else:
                self.capture(self.indx)        
                height, width, channels = self.frame.shape

                # Detecting objects
                blob = cv2.dnn.blobFromImage(self.frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
                
                net.setInput(blob)
                outs = net.forward(output_layers)

                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.2:
                            # Object detected
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)

                            # Rectangle coordinates
                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)

                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                # Labelling of Confidence and Object
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        confidence = confidences[i]
                        color = colors[class_ids[i]]
                        cv2.rectangle(self.frame, (x, y), (x + w, y + h), color, 2)
                        fin = label + " " + str(round(confidence, 2))
                        (label_width, label_height), baseline = cv2.getTextSize(fin, self.font, 1.2, 1)

                        rect_width = label_width + 10
                        rect_height = label_height + 10
                        rect_x1 = x
                        rect_y1 = y
                        rect_x2 = rect_x1 + rect_width
                        rect_y2 = rect_y1 + rect_height
                        
                        cv2.rectangle(self.frame, (x,y), (rect_x2, rect_y2), color, -1)
                        label_x = rect_x1 + 5
                        label_y = rect_y2 - 5
                        cv2.putText(self.frame, fin, (label_x, label_y), self.font, 1.2, (255,255,255), 2)
                # Update frame
                self.update_frame(self.frame)
                
                key = cv2.waitKey(1) & 0xFF
                if self.o_detect == False:
                    # Exit and clear frame box and release capture
                    self.frame_box.setPixmap(QtGui.QPixmap(""))
                    self.frame = None
                    self.cap.release()
                    break

    # Face detection function           
    def face_detection(self):
        if self.f_detect:
            self.f_detect = False
            self.face_btn.setText("Start Face Detection")
            self.obj_btn.setStyleSheet("background-color : yellow")
        else:
            self.f_detect = True
            self.o_detect = False
            self.obj_btn.setText("Start Object Detection")
            self.obj_btn.setStyleSheet("background-color : yellow")
            self.face_btn.setText("Stop Face Detection")
            self.face_btn.setStyleSheet("background-color : red")
        while self.f_detect:
            QtWidgets.QApplication.processEvents()
            if self.frame is None:
                self.capture(self.indx)
            else:
                self.capture(self.indx)
                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            
            try:
                faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.15,  
                minNeighbors=7, 
                minSize=(80, 80), 
                flags=cv2.CASCADE_SCALE_IMAGE)
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(self.frame, (x, y), (x + w, y + h), (10, 228,220), 5) 
            except Exception as e:
                pass
            self.update_frame(self.frame)
            key = cv2.waitKey(1) & 0xFF
            if self.f_detect == False:
                self.face_btn.setStyleSheet("background-color : yellow")
                self.frame = None
                self.cap.release()
                self.frame_box.setPixmap(QtGui.QPixmap(""))
                break
           
    # Release capture function
    def release_capture(self):
        # Set frame_box empty and release capture and exit the program
        self.frame_box.setPixmap(QtGui.QPixmap(""))
        self.cap.release()
        exit(0)
    
    # Blur value function
    def blur_value(self, value):
        self.blur_val = value
        print('Blur: ',value)

    # Brightness value function
    def brt_value(self, value):
        self.brt_val = value
        print("Brightness: ", value)
    
    # Change brightness function
    def change_brt(self, img, value):
        if img is not None:
            hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            h,s,v = cv2.split(hsv)
            lim = 255 - value
            v[v>lim] = 255
            v[v<=lim] += value
            final_hsv = cv2.merge((h,s,v))
            img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
            return img
        else:
            print("Error: image is None")

    # Take picture function
    def take_pic(self):
        # Save the iamge to local and active directory
        self.filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        self.timestamp = str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))
        self.temp_frame = ps.putBText(self.temp_frame,self.timestamp,text_offset_x=20,text_offset_y=20,vspace=10,hspace=10, font_scale=0.5,background_RGB=(228,225,222),text_RGB=(0,0,0))
        cv2.imwrite(self.filename,self.temp_frame)
        print('Saved as:', self.filename)

    # Change resoluton function
    def change_res(self, res):
        if res == 'cif':
            print("Previous res: ", self.current_res)
            self.current_res = self.res_url.get('cif')
            imgResp = urllib.request.urlopen(self.current_res)
            if self.f_detect:
                # Refresh capture
                self.f_detect = False
                self.f_detect = True
            elif self.o_detect:
                self.o_detect = False
                self.o_detect = True
            else:
                return
            print("Current res: ", self.current_res)
        elif res == 'vga':
            print("Previous res: ", self.current_res)
            self.current_res = self.res_url.get('vga')
            imgResp = urllib.request.urlopen(self.current_res)
            if self.f_detect:
                self.f_detect = False
                self.f_detect = True
            elif self.o_detect:
                self.o_detect = False
                self.o_detect = True
            else:
                return
            print("Current res: ", self.current_res)
        elif res == 'svga':
            print("Previous res: ", self.current_res)
            self.current_res = self.res_url.get('svga')
            imgResp = urllib.request.urlopen(self.current_res)
            if self.f_detect:
                self.f_detect = False
                self.f_detect = True
            elif self.o_detect:
                self.o_detect = False
                self.o_detect = True
            else:
                return
            print("Current res: ", self.current_res)
        else:
            print("ERROR: Unavailable Resoultion")

    # Change visual/special effects function
    def change_vfx(self, vfx):
        vfx_url = self.base_vfx_url+vfx
        print(vfx_url)
        imgResp = urllib.request.urlopen(vfx_url)
        if self.f_detect:
            self.f_detect = False
            self.f_detect = True
        elif self.o_detect:
            self.o_detect = False
            self.o_detect = True
        else:
            return
    
    # Firebase update function (unfinished)
    def firebase_update(self):
        # Not implemented yet
        pass

    # Horizontal flip function
    def hflip(self):
        if self.hflipped:
            imgResp = urllib.request.urlopen(self.base_url + 'control?var=hmirror&val=0')
            self.hflipped = False
        else:
            imgResp = urllib.request.urlopen(self.base_url + 'control?var=hmirror&val=1')
            self.hflipped = True

    # Vertical flip function
    def vflip(self):
        if self.vflipped:
            imgResp = urllib.request.urlopen(self.base_url + 'control?var=vflip&val=0')
        else:
            imgResp = urllib.request.urlopen(self.base_url + 'control?var=vflip&val=1')
            self.vflipped = True
    
    # No special effects function
    def no_effect(self):
        self.vflipped = False
        self.vflip()
        self.hflipped = False
        self.hflip()
        self.change_vfx('0')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
