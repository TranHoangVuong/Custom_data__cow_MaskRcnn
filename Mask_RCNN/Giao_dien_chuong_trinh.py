import sys
import tkinter
from tkinter import *

import PIL
from PIL import Image, ImageTk
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
import cv2
import numpy as np
import object_image as obji
import object_video as bojv


class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.parent.title("Couting object")
        self.pack(fill=BOTH, expand=1)
  
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
  
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Openimage", command=self.onOpenimage)
        fileMenu.add_command(label="Openvideo", command=self.onOpenvideo)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)


        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpenimage(self):
        global ftypes
        ftypes = [('Images', '*.jpg *.tif *.bmp *.gif *.png')]
        dlg = Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            global imgin
            imgin = cv2.imread(fl,cv2.IMREAD_COLOR);
            cv2.namedWindow("ImageIn", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("ImageIn", imgin)

            global imgout
            imgout = obji.objectImage(imgin)
            cv2.namedWindow("ImageOut", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("ImageOut", imgout)
            cv2.waitKey()


    def onOpenvideo(self):
        self = 0
        global imgout
        imgout = bojv.objectVideo(self)


    def onSave(self):
        dlg = SaveAs(self,filetypes = ftypes);
        fl = dlg.show()
        if fl != '':
            cv2.imwrite(fl,imgout)
       

root = Tk()
Main(root)
root.geometry("640x480+100+100")
root.mainloop()





