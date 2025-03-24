from random import randint
from tkinter import *
from Map import Map
from MenuBar import MenuBar
from Clock import Clock
from Bestiary import *
from PIL import Image, ImageTk


## APPLICATION MAIN WINDOW
root = Tk()
root.title("PLEASE, DON'T SCALE THIS WINDOW")
root.resizable(True, True)
root.state('zoomed')

c = Canvas(root, width=1200, height=800, bg="white", highlightthickness=0, background="white")
c.place(x=0, y=0, anchor='nw')
## INIT Map class
Map.InitModule(canvas=c)

# Пасхалка в коде: Илюха пидарас

## INSPECTOR WINDOW
ins = Tk()
MenuBar.InitModule(ins=ins)
ins.title("DM's panel | Inspector")
ins.resizable(False, False)
ins.geometry('320x730')
ins.wm_attributes('-topmost', True)

## PLAYER NAMES
playerNames = ['Mzhuka', 'Glurp', 'Ustalost', 'Valyana']


### Inspector's main panel frames (separated blocks)
## CLOCK: Element to track worlds time and track timed quests
Clock.ins = ins
Clock.Initialize()


### MenuBar commands (buttons)
MenuBar.sections['Map'].add_command(label='Background', command=MenuBar.Call_BackgroundSetup)
MenuBar.sections['Map'].add_separator()
MenuBar.sections['Map'].add_command(label='Toggle grid', command = Map.ToggleGrid)
MenuBar.sections['Map'].add_command(label='Grid settings', command = MenuBar.Call_GridSetup)
# -----
MenuBar.sections['Clock'].add_command(label='-1 day', command=None)
MenuBar.sections['Clock'].add_command(label='-1 hour', command=None)
MenuBar.sections['Clock'].add_command(label='-15 minutes', command=None)
MenuBar.sections['Clock'].add_separator()
MenuBar.sections['Clock'].add_command(label='+15 minutes', command=lambda: Clock.AddTime(15))
MenuBar.sections['Clock'].add_command(label='+30 minutes', command=lambda: Clock.AddTime(30))
MenuBar.sections['Clock'].add_command(label='+1 hour', command=lambda: Clock.AddTime(60))
MenuBar.sections['Clock'].add_command(label='+4 hours', command=lambda: Clock.AddTime(240))
MenuBar.sections['Clock'].add_command(label='+8 hours', command=lambda: Clock.AddTime(480))
MenuBar.sections['Clock'].add_command(label='+1 day', command=lambda: Clock.AddTime(1440))
MenuBar.sections['Clock'].add_separator()
MenuBar.sections['Clock'].add_command(label='Short rest', command=None)
MenuBar.sections['Clock'].add_command(label='Long rest', command=None)

Map.DrawGrid()

### CURRENT UNITS ON MAP
units = []
selectedUnit = None # Index, NOT object!!!

## LISTBOX: Stores a list of all units on table to track stats
unitlist = Listbox(ins, width=42, height=15, font=('Arial', 10))
unitlist.place(anchor=N, x=160, y=140)


def UpdateUnitlist():
    global unitlist; global units; global playerNames
    unitlist.delete(0, END)
    for i in units:
        temp = " "*(6-len(str(i.initiative))*2)
        temp2 = " "*(18-len(str(i.name)))
        temp3 = "" if i.name not in playerNames else "[P]  "
        unitlist.insert(END, f"{i.initiative}{temp}| {temp3} {i.name} {temp2}| {i.hp} / {i.maxhp} | AC: {i.armorClass}")

def OnUnitSelection(event):
    global selectedUnit; global unitlist; global c; global units; global statblock; global iconTkObject
    if selectedUnit is not None:
        units[selectedUnit].isSelected = False
    selectedUnit = unitlist.curselection()[0]
    units[selectedUnit].isSelected = True
    c.delete('SelectionMarker')
    i = units[selectedUnit]
    posX, posY = c.coords(i.obj)
    c.create_rectangle(posX-i.tkImage.width()/2, posY-i.tkImage.height()/2, posX+i.tkImage.width()/2, posY+i.tkImage.height()/2, width=1,
                       tags='SelectionMarker')
    statblock['name'].config(text=i.name.upper())
    statblock['health'].config(text=f"HP: {i.hp} / {i.maxhp}")
    statblock['armorClass'].config(text=f"AC: {i.armorClass}")
    statblock['STR_ind'].config(text=str(i.sb['STR']))
    statblock['DEX_ind'].config(text=str(i.sb['DEX']))
    statblock['CON_ind'].config(text=str(i.sb['CON']))
    statblock['INT_ind'].config(text=str(i.sb['INT']))
    statblock['WIS_ind'].config(text=str(i.sb['WIS']))
    statblock['CHA_ind'].config(text=str(i.sb['CHA']))
    statblock['moveset'].delete(0, END)
    for j in i.moveset:
        statblock['moveset'].insert(END, j)
def ClearSelection(event):
    global unitlist; global selectedUnit
    unitlist.selection_clear(0, END)
    units[selectedUnit].isSelected = False
    selectedUnit = None
# Connecting this method to event listener
unitlist.bind("<<ListboxSelect>>", OnUnitSelection)


moveorder = Canvas(root, height=800, width=300, background='lightgrey')
moveorder.place(anchor=NW, x=1200, y=0)
currentUnit = None; lastActiveUnit = None
teamcolors = {
    'Party' : '#65c25d', 'PartyActive' : '#3ad42c',
    'Enemy' : '#cc5c5c', 'EnemyActive' : '#c92a2a',
    'Ally' : '#60bbd6', 'AllyActive' : '#09b0e3',
    'Neutral' : '#d4c053', 'NeutralActive' : '#dec016'
}


def UpdateMoveorder(allowGroups = True):
    global moveorder; global units; global playerNames; global currentUnit; global lastActiveUnit
    moveorder.delete(ALL)
    leftForGroup = 3 if allowGroups else 0
    for i in range(len(units)):
        active = bool(i == currentUnit)
        if leftForGroup != 3 and leftForGroup > 0:
            if units[i].team == units[i-1].team and abs(units[i].initiative - units[currentUnit].initiative) <= 3:
                active = True
            else:
                leftForGroup = 0
                lastActiveUnit = i - 1

        selectionOffset = 30 if active else 0
        color = teamcolors[str(units[i].team + 'Active')] if active else teamcolors[str(units[i].team)]

        moveorder.create_rectangle(0, 42 * i + (i * 10) + 15, 120+selectionOffset, 42 * (i + 1) + (i * 10) + 15,
                                       fill=color, outline='black', width=2)
        moveorder.create_image(75+selectionOffset, 42*i+(i*10)+16, image=units[i].tkIcon, anchor=NW)
        moveorder.create_text(20, 42*i+(i*10)+35, text=str(units[i].initiative), font=('Arial', 12), anchor=CENTER)
        leftForGroup -= 1 if active else 0
        if i == len(units)-1:
            leftForGroup = 0
        if active and leftForGroup == 0:
            lastActiveUnit = i
def NextUnit():
    global lastActiveUnit; global currentUnit
    if lastActiveUnit is None or currentUnit is None:
        lastActiveUnit = -1
    currentUnit = lastActiveUnit + 1
    if currentUnit > len(units) - 1:
        currentUnit = 0; lastActiveUnit = -1
    UpdateMoveorder()

def AddUnit(unit, scaleX=1, scaleY=1):
    global units; global playerNames
    if unit in globals():
        units.append(globals()[unit](c, [scaleX, scaleY]))
    units = sorted(units, key=lambda w: (-w.initiative, -w.sb['DEX'], w.name not in playerNames))
    UpdateUnitlist()

## INSPECTOR: Shows a current selected in LISTBOX unit's stat block
statblock = {
    'frame' : Frame(ins, width=310, height=200, borderwidth=1, relief="solid"),
    'name' : None
}
statblock['frame'].place(anchor=N, x=160, y=480)

statblock['name'] = Label(statblock['frame'], text="UNITNAME", bg='lightgrey', font=('Arial Black', 10), width=33)
statblock['name'].place(anchor=N, x=153, y=0)

statblock['health'] = Label(statblock['frame'], text="HP: 000 / 000", font=('Arial', 12))
statblock['health'].place(anchor=W, x=5, y=40)

statblock['armorClass'] = Label(statblock['frame'], text="AC: 00", font=('Arial', 12))
statblock['armorClass'].place(anchor=W, x=5, y=60)


statblock['STR_ind'] = Label(statblock['frame'], text="00", font=('Arial', 13))
statblock['STR_ind'].place(anchor=N, x=44, y=164)
Label(statblock['frame'], text=" STR ", font=('Arial', 8)).place(anchor=N, x=44, y=185)

statblock['DEX_ind'] = Label(statblock['frame'], text="00", font=('Arial', 13))
statblock['DEX_ind'].place(anchor=N, x=88, y=164)
Label(statblock['frame'], text=" DEX ", font=('Arial', 8)).place(anchor=N, x=88, y=185)

statblock['CON_ind'] = Label(statblock['frame'], text="00", font=('Arial', 13))
statblock['CON_ind'].place(anchor=N, x=132, y=164)
Label(statblock['frame'], text=" CON ", font=('Arial', 8)).place(anchor=N, x=132, y=185)

statblock['INT_ind'] = Label(statblock['frame'], text="00", font=('Arial', 13))
statblock['INT_ind'].place(anchor=N, x=176, y=164)
Label(statblock['frame'], text=" INT ", font=('Arial', 8)).place(anchor=N, x=176, y=185)

statblock['WIS_ind'] = Label(statblock['frame'], text="00", font=('Arial', 13))
statblock['WIS_ind'].place(anchor=N, x=220, y=164)
Label(statblock['frame'], text=" WIS ", font=('Arial', 8)).place(anchor=N, x=220, y=185)

statblock['CHA_ind'] = Label(statblock['frame'], text="00", font=('Arial', 13))
statblock['CHA_ind'].place(anchor=N, x=264, y=164)
Label(statblock['frame'], text=" CHA ", font=('Arial', 8)).place(anchor=N, x=264, y=185)

statblock['moveset'] = Listbox(statblock['frame'], selectmode='none', exportselection=0, width=41, height=4, font=('Arial', 10))
statblock['moveset'].place(anchor=N, x=153, y=78)


## COMMAND LANE
comlane = Entry(ins, width=33, font=('Arial', 12))
comlane.place(anchor=W, x=10, y=710)

def ComlaneExecute(event):
    global comlane; global units; global selectedUnit; global unitlist; global c; global playerNames; global currentUnit
    success = False
    command = comlane.get().strip().split(' ')
    if command[0] == 'hp' and selectedUnit is not None:
        units[selectedUnit].hp += int(command[1])
        success = True
    if command[0] == 'ac' and selectedUnit is not None:
        units[selectedUnit].armorClass = int(command[1])
        success = True
    if command[0] == 'rename' and selectedUnit is not None:
        units[selectedUnit].name = " ".join(command[1].split("_"))
        success = True
    if command[0] == 'sb' and selectedUnit is not None:
        units[selectedUnit].sb[command[1]] = int(command[2])
        success = True
    if command[0] == 'maxhp' and selectedUnit is not None:
        units[selectedUnit].maxhp = int(command[1])
        success = True
    if command[0] == 'mirror' and selectedUnit is not None:
        units[selectedUnit].Mirror()
        success = True
    if command[0] == 'setscale' and selectedUnit is not None:
        units[selectedUnit].scaleX = float(command[1])
        units[selectedUnit].scaleY = float(command[2])
        units[selectedUnit].RenderUnit()
        success = True
    if command[0] == 'scale' and selectedUnit is not None:
        units[selectedUnit].scaleX *= float(command[1])
        units[selectedUnit].scaleY *= float(command[2])
        units[selectedUnit].RenderUnit()
        success = True
    if command[0] == 'ds' and selectedUnit is not None:
        if selectedUnit is not None:
            units[selectedUnit].isSelected = False
        unitlist.selection_clear(0, END)
        selectedUnit = None
        success = True
        c.delete('SelectionMarker')
    if command[0] == 'rotate' and selectedUnit is not None:
        units[selectedUnit].Rotate(command[1])
        success = True
    if command[0] == 'delete' and selectedUnit is not None:
        c.delete(units[selectedUnit].obj)
        units.pop(selectedUnit)
        success = True
        selectedUnit = None
        c.delete('SelectionMarker')
    if command[0] == 'add':
        AddUnit(command[1])
        success = True
    if command[0] == 'rerollinit':
        for i in units:
            i.initiative = randint(1, 20) + i.sb['DEX']//2-5 + i.initBonus
        units = sorted(units, key=lambda w: (-w.initiative, -w.sb['DEX'], w.name not in playerNames))
        UpdateUnitlist()
        UpdateMoveorder()
        success = True
    if command[0] == 'upd':
        UpdateMoveorder()
        success = True
    if command[0] == 'm':
        if len(command) > 1  and selectedUnit is not None:
            currentUnit = selectedUnit
            if command[1] == "-":
                UpdateMoveorder(allowGroups = False)
            elif command[1] == "+":
                UpdateMoveorder()
        else:
            NextUnit()
    if command[0] == 'team' and selectedUnit is not None:
        units[selectedUnit].team = command[1]
        UpdateMoveorder()
        success = True
    if success:
        UpdateUnitlist()
        if selectedUnit is not None:
            unitlist.selection_clear(0, END)
            unitlist.selection_set(selectedUnit)
            unitlist.activate(selectedUnit)
            unitlist.event_generate("<<ListboxSelect>>")
        comlane.delete(0, END)

ins.bind('<Return>', ComlaneExecute)


### DEBUG
AddUnit("Ustalost")
AddUnit("Mzhuka")
AddUnit("Glurp")



### MAINLOOP
root.mainloop()