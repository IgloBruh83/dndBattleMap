from tkinter import *
from Map import Map

class MenuBar:

    @classmethod
    def InitModule(cls, ins):
        cls.ins = ins
        menubar = cls.menubar = Menu(ins)
        cls.sections = {
            'Map': Menu(menubar, tearoff=0),
            'Clock': Menu(menubar, tearoff=0),
        }
        for i in ['Map', 'Clock']:
            menubar.add_cascade(label=i, menu=cls.sections[i])
        ins.config(menu=menubar)

    @staticmethod
    def Call_GridSetup():
        win = Tk()
        win.geometry('300x325')
        win.resizable(False, False)
        win.title('Grid settings')
        # Helping labels for settings panel
        Label(win, text="Offset (px)", font=("Arial", 12)).place(anchor='center', x=150, y=20)
        Label(win, text="x:", font=("Arial", 12)).place(anchor='center', x=70, y=50)
        Label(win, text=":y", font=("Arial", 12)).place(anchor='center', x=230, y=50)
        Label(win, text="Grid size (Horizontal) (px)", font=("Arial", 12)).place(anchor='center', x=150, y=90)
        Label(win, text="base:", font=("Arial", 12)).place(anchor='e', x=70, y=120)
        Label(win, text=":end", font=("Arial", 12)).place(anchor='w', x=230, y=120)
        Label(win, text="Grid size (Vertical) (px)", font=("Arial", 12)).place(anchor='center', x=150, y=150)
        Label(win, text="base:", font=("Arial", 12)).place(anchor='e', x=70, y=180)
        Label(win, text=":end", font=("Arial", 12)).place(anchor='w', x=230, y=180)
        Label(win, text="Color", font=("Arial", 12)).place(anchor='center', x=100, y=220)
        Label(win, text="Width", font=("Arial", 12)).place(anchor='center', x=210, y=220)
        ## Functional fields to enter values
        field_offsetX = Text(win, width=5, height=1, font=("Arial", 14)); field_offsetX.place(anchor='center', x=110, y=50)
        field_offsetY = Text(win, width=5, height=1, font=("Arial", 14)); field_offsetY.place(anchor='center', x=190, y=50)
        field_gridSizeXbase = Text(win, width=5, height=1, font=("Arial", 14)); field_gridSizeXbase.place(anchor='center', x=110, y=120)
        field_gridSizeXfalloff = Text(win, width=5, height=1, font=("Arial", 14)); field_gridSizeXfalloff.place(anchor='center', x=190, y=120)
        field_gridSizeYbase = Text(win, width=5, height=1, font=("Arial", 14)); field_gridSizeYbase.place(anchor='center', x=110, y=180)
        field_gridSizeYfalloff = Text(win, width=5, height=1, font=("Arial", 14)); field_gridSizeYfalloff.place(anchor='center', x=190, y=180)
        field_gridColor = Text(win, width=10, height=1, font=("Arial", 14)); field_gridColor.place(anchor='center', x=100, y=250)
        field_gridWidth = Text(win, width=5, height=1, font=("Arial", 14)); field_gridWidth.place(anchor='center', x=210, y=250)
        ## Setting up current values to fields based on Map.gridConfig
        field_offsetX.insert("1.0", str(Map.gridConfig['offsetX']))
        field_offsetY.insert("1.0", str(Map.gridConfig['offsetY']))
        field_gridSizeXbase.insert("1.0", str(Map.gridConfig['gridSizeX'][0]))
        field_gridSizeXfalloff.insert("1.0", str(Map.gridConfig['gridSizeX'][1]))
        field_gridSizeYbase.insert("1.0", str(Map.gridConfig['gridSizeY'][0]))
        field_gridSizeYfalloff.insert("1.0", str(Map.gridConfig['gridSizeY'][1]))
        field_gridColor.insert("1.0", str(Map.gridConfig['color']))
        field_gridWidth.insert("1.0", str(Map.gridConfig['width']))
        ## ACTION
        def Action():
            Map.gridConfig['offsetX'] = int(field_offsetX.get("1.0", END))
            Map.gridConfig['offsetY'] = int(field_offsetY.get("1.0", END))
            Map.gridConfig['gridSizeX'][0] = int(field_gridSizeXbase.get("1.0", END))
            Map.gridConfig['gridSizeX'][1] = int(field_gridSizeXfalloff.get("1.0", END))
            Map.gridConfig['gridSizeY'][0] = int(field_gridSizeYbase.get("1.0", END))
            Map.gridConfig['gridSizeY'][1] = int(field_gridSizeYfalloff.get("1.0", END))
            Map.gridConfig['color'] = field_gridColor.get("1.0", END).replace('\n', '')
            Map.gridConfig['width'] = int(field_gridWidth.get("1.0", END))
            Map.DrawGrid()
        ## Action button
        Button(win, text='Apply', command=Action, font=("Arial", 12)).place(anchor='center', x=150, y=290)

    @staticmethod
    def Call_BackgroundSetup():
        win = Tk()
        win.geometry('300x200')
        win.resizable(False, False)
        win.title('Background settings')
        # Helping labels for settings panel
        Label(win, text="Image path (relative):", font=("Arial", 12)).place(anchor='center', x=150, y=20)
        Label(win, text="Brightness (%):", font=("Arial", 12)).place(anchor='center', x=150, y=90)
        ## Functional fields to enter values
        field_path = Text(win, width=23, height=1, font=("Arial", 14)); field_path.place(anchor='center', x=150, y=50)
        field_brightness = Text(win, width=5, height=1, font=("Arial", 14)); field_brightness.place(anchor='center', x=150, y=120)
        ## Setting up current values to fields based on Map.gridConfig
        field_path.insert("1.0", "" if Map.bgConfig['path'] is None else str(Map.bgConfig['path']))
        field_brightness.insert("1.0", str(Map.bgConfig['brightness']*100))
        ## ACTION
        def Action():
            temp = field_path.get("1.0", END).replace('\n', '')
            Map.bgConfig['path'] = temp if temp != '' else None
            Map.bgConfig['brightness'] = float(field_brightness.get("1.0", END))/100
            Map.UpdateBackground()
        ## Action button
        Button(win, text='Apply', command=Action, font=("Arial", 12)).place(anchor='center', x=150, y=165)