from tkinter import *

class Clock:

    
    ## A reference to app's inspector panel
    ins = None # ALWAYS MUST BE ASSIGNED MANUALLY

    ## Time variables, temp variables, etc.
    year = 1287
    month = 10
    day = 15
    time = 0
    monthsLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lastAction = 0

    ## Technical variables & references
    @classmethod
    def Initialize(cls):
        cls.frame = Frame(cls.ins, width=310, height=120, borderwidth=1, relief="solid"); cls.frame.place(anchor=N, x= 160, y=5)
        cls.repeatButton = Button(cls.frame, text="Repeat", command=lambda: Clock.AddTime(Clock.lastAction)); cls.repeatButton.place(anchor=W, x=5, y=15)
        cls.timeObject = Label(cls.frame, text="00:00", font=('Arial', 32)); cls.timeObject.place(anchor=CENTER, x=155, y=30)
        cls.dateObject = Label(cls.frame, text="15 / 10 / 1287", font=('Arial', 12)); cls.dateObject.place(anchor=CENTER, x=155, y=60)

    # Action
    @classmethod
    def AddTime(cls, minutes):
        cls.time += minutes
        if cls.time >= 1440:
            cls.time -= 1440
            cls.day += 1
        if cls.day > cls.monthsLen[cls.month-1]:
            cls.day = 1
            cls.month += 1
        if cls.month > 12:
            cls.month = 1
            cls.year += 1
        temp1 = "0" if len(str(cls.time // 60)) == 1 else ""
        temp2 = "0" if len(str(cls.time % 60)) == 1 else ""
        cls.timeObject.config(text=f"{temp1}{cls.time // 60}:{temp2}{cls.time % 60}")
        cls.dateObject.config(text=f"{cls.day} / {cls.month} / {cls.year}")
        cls.lastAction = minutes