from ctypes.wintypes import RGB
import tkinter as tk
from tkinter import *
import pyautogui
import numpy as np
from cv2 import *
from PIL import Image
from PIL import ImageTk
#import imutils
root= tk.Tk ()
main_window = root
main_window.geometry('1020x900')
main_window.title('Oppy Capture')
main_window.config(background='#AA82D5')


def login_window():
    login_window = Toplevel(root)
    login_window.title ('Oppy Login')
    login_window.iconbitmap('C:/Users/Kinterx/Desktop/pruebas/icono.ico')
    login_window.geometry ('300x300')
    login_window.config(background='#C4C8BD')
    

    def search_data():
        username_data = username.get()
        password_data = password.get()
        print(username_data , password_data)
        
        login_file = open('registration.txt', 'a')
        login_file.write(username_data)
        login_file.write('\t')
        login_file.write(password_data)
        login_file.write ('\n')
        login_file.close


    image =  PhotoImage(file = 'C://Users/Kinterx/Desktop/pruebas/oppy_logo.png')
    image = image.subsample(2,2)
    label_logo = Label(login_window, image=image).grid(pady=10)
    label_username = Label(login_window, text='Username').grid(row=1, column=0, sticky=W, padx=10, pady=10)
    label_password = Label(login_window, text='Password').grid(row=2, column=0, sticky=W, padx=10)
    button_login = Button(login_window, text='Entrar',width=20, command=search_data).grid(row=5, pady=10)
    button_stop = Button(login_window, text='Cancelar', width= 20, command=login_window.destroy).grid(row=6, pady=10)

    

    username = StringVar()
    password = StringVar()

    entry_username = Entry(login_window, textvariable=username, width=22)
    entry_password = Entry(login_window, textvariable=password, width=22, show='*')
    entry_username.grid(row=1, padx=70)
    entry_password.grid(row=2, padx=70)

    login_window.mainloop()

#-------------- CONSOLA -----------------#
consola = Label(root, text='CONOSOLA DE GRABACIÓN', font= 'bold').grid (column=0, row=1, padx=5, pady=5)
rec = Button(text = "Grabar",width=20).grid(column=0, row=2)
pause = Button(text = "Pausar")
parar = Button(text = "Parar")
#--------------------------RECORDER----------------------------#
def recorder():
    while True:
        #----SCREEN RESOLUTION----#
        resolution = pyautogui.size()
        #resolution = (800,600)
        #----DEFINE CODEC----#
        fourcc = VideoWriter_fourcc(*"XVID")
        FPS = 60

        #----VIDEO WRITE OBJECT----#
        out = cv2.VideoWriter("output.avi", fourcc, FPS, (resolution))

        #----SCREENSHOTS----#

        img = pyautogui.screenshot()

        #----CONVER PIXEL TO A NUMPY ARRAY TO WORK WHIT OPENCV----#
        frame = np.array(img)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #----WRITE THE FRAME----#
        #out.write (frame)
        #----SHOW THE FRAME----#
        #cv2.imshow('screeshot', frame)
        #frame= imutils.resize(image, width=180)
        ima = Image.fromarray(frame)
        imge = ImageTk.PhotoImage(ima)
        preiviewlbl.configure(image=imge)
        preiviewlbl.image = imge
        #----PRESS KEY TO STOP----#
        root.update_idletasks()
        #if cv2.waitKey(1) == ord("q"):
            #break
        
    #cv2.destroyAllWindows()
    #out.relese()

preiviewlbl = tk.Label()
preiviewlbl.grid(row=1, column=3,padx=6, pady=6)
def stop_recorder():
    fd
#---------------------------MENU BAR---------------------------#
menubar = Menu(main_window)
file_menu = Menu(menubar, tearoff=0)
edit_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Archivos', menu=file_menu)
file_menu.add_command(label='Iniciar Secion', command=login_window)
file_menu.add_separator()
file_menu.add_command(label='Salir', command= root.destroy)
menubar.add_cascade(label='Editar', menu=edit_menu)
edit_menu.add_command(label='Grabar', command= recorder)
edit_menu.add_command(label='Pausar')
edit_menu.add_command(label='Parar',command= )



root.config(menu=menubar)
root.mainloop()

