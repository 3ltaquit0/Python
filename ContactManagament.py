from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Sistema de Gestión de Contactos")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")

#============================VARIABLES===================================
NOMBRE = StringVar()
APELLIDO = StringVar()
GENERO = StringVar()
EDAD = StringVar()
DIRECCION = StringVar()
CONTACTO = StringVar()



#============================METHODS=====================================

def Database():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, genero TEXT, edad TEXT, direccion TEXT, contacto TEXT)")
    cursor.execute("SELECT * FROM `member` ORDER BY `apellido` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  NOMBRE.get() == "" or APELLIDO.get() == "" or GENERO.get() == "" or EDAD.get() == "" or DIRECCION.get() == "" or CONTACTO.get() == "":
        result = tkMessageBox.showwarning('', 'Porfavor complete los campos requeridos', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contact.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (nombre, apellido, genero, edad, direccion, contacto) VALUES(?, ?, ?, ?, ?, ?)", (str(NOMBRE.get()), str(APELLIDO.get()), str(GENERO.get()), int(EDAD.get()), str(DIRECCION.get()), str(CONTACTO.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `apellido` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        NOMBRE.set("")
        APELLIDO.set("")
        GENERO.set("")
        EDAD.set("")
        DIRECCION.set("")
        CONTACTO.set("")

def UpdateData():
    if GENERO.get() == "":
       result = tkMessageBox.showwarning('', 'Porfavor completa los datos requeridos', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contact.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `nombre` = ?, `apellido` = ?, `genero` =?, `edad` = ?,  `direccion` = ?, `contacto` = ? WHERE `mem_id` = ?", (str(NOMBRE.get()), str(APELLIDO.get()), str(GENERO.get()), str(EDAD.get()), str(DIRECCION.get()), str(CONTACTO.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `apellido` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        NOMBRE.set("")
        APELLIDO.set("")
        GENERO.set("")
        EDAD.set("")
        DIRECCION.set("")
        CONTACTO.set("")


def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    NOMBRE.set("")
    APELLIDO.set("")
    GENERO.set("")
    EDAD.set("")
    DIRECCION.set("")
    CONTACTO.set("")
    NOMBRE.set(selecteditem[1])
    APELLIDO.set(selecteditem[2])
    EDAD.set(selecteditem[4])
    DIRECCION.set(selecteditem[5])
    CONTACTO.set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Sistema de Gestión de Contactos")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Masculino", variable=GENERO, value="Masculino",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Femenino", variable=GENERO, value="Femenino",  font=('arial', 14)).pack(side=LEFT)

    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Actualizando contactos", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="Nombre", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Apellido", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Genero", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Edad", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Direccion", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contacto", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=NOMBRE, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=APELLIDO, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=EDAD,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=DIRECCION,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACTO,  font=('arial', 14))
    contact.grid(row=5, column=1)


    #==================BUTTONS==============================
    btn_updatecon = Button(ContactForm, text="Actualizar", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


#fn1353p
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Porfavor seleccione algo primero', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Esta usted seguro que quiere borrar este contacto?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("contact.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def AddNewWindow():
    global NewWindow
    NOMBRE.set("")
    APELLIDO.set("")
    GENERO.set("")
    EDAD.set("")
    DIRECCION.set("")
    CONTACTO.set("")
    NewWindow = Toplevel()
    NewWindow.title("Agregar contactos")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Masculino", variable=GENERO, value="Masculino",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Femenino", variable=GENERO, value="Femenino",  font=('arial', 14)).pack(side=LEFT)

    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Agregar Nuevo Contacto", font=('arial', 16), bg="orange", width=300)
    lbl_title.pack(fill=X)
    lbl_nombre = Label(ContactForm, text="Nombre", font=('arial', 14), bd=5)
    lbl_nombre.grid(row=0, sticky=W)
    lbl_apellido = Label(ContactForm, text="Apellido", font=('arial', 14), bd=5)
    lbl_apellido.grid(row=1, sticky=W)
    lbl_genero = Label(ContactForm, text="Género", font=('arial', 14), bd=5)
    lbl_genero.grid(row=2, sticky=W)
    lbl_edad = Label(ContactForm, text="Edad", font=('arial', 14), bd=5)
    lbl_edad.grid(row=3, sticky=W)
    lbl_direccion = Label(ContactForm, text="Dirección", font=('arial', 14), bd=5)
    lbl_direccion.grid(row=4, sticky=W)
    lbl_contacto = Label(ContactForm, text="Contacto", font=('arial', 14), bd=5)
    lbl_contacto.grid(row=5, sticky=W)

    #===================ENTRY===============================
    nombre = Entry(ContactForm, textvariable=NOMBRE, font=('arial', 14))
    nombre.grid(row=0, column=1)
    apellido = Entry(ContactForm, textvariable=APELLIDO, font=('arial', 14))
    apellido.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    edad = Entry(ContactForm, textvariable=EDAD, font=('arial', 14))
    edad.grid(row=3, column=1)
    direccion = Entry(ContactForm, textvariable=DIRECCION, font=('arial', 14))
    direccion.grid(row=4, column=1)
    contacto = Entry(ContactForm, textvariable=CONTACTO, font=('arial', 14))
    contacto.grid(row=5, column=1)


    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="GUARDAR", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)





#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="#6666ff")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#6666ff")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(Top, text="Sistema de Gestión de Contactos", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+ AGREGAR", bg="#66ff66", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="BORRAR", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("ID", "Nombre", "Apellido", "Género", "Edad", "Dirección", "Contacto"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('Nombre', text="Nombre", anchor=W)
tree.heading('Apellido', text="Apellido", anchor=W)
tree.heading('Género', text="Género", anchor=W)
tree.heading('Edad', text="Edad", anchor=W)
tree.heading('Dirección', text="Dirección", anchor=W)
tree.heading('Contacto', text="Contacto", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=50)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=100)
tree.column('#4', stretch=NO, minwidth=0, width=50)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()