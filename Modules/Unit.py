from PIL import Image, ImageTk



class Unit:
    def __init__(self, canvas, image_path, icon_path, scaleX=1.0, scaleY=1.0):
        # Default values for empty unit -> OVERRIDE
        self.name = '#name'
        self.team = 'Neutral'
        self.maxhp = 100; self.hp = 0
        self.image_raw = Image.open(image_path)
        self.icon_raw = Image.open(icon_path)
        self.devScale = 1
        self.sb = {
            'STR' : 10, 'DEX' : 10, 'CON' : 10, 'INT' : 10, 'WIS' : 10, 'CHA' : 10
        }
        self.moveset = [
        ]
        self.armorClass = 10
        self.initBonus = 0

        # Default values for ANY unit
        self.c = canvas
        self.scaleX, self.scaleY = scaleX, scaleY
        self.x, self.y = 600, 400
        self.mouseOffsetX = 0
        self.mouseOffsetY = 0
        self.obj = None
        self.isSelected = False
        self.active = False

        # Draw - Disabled to be used in subclasses
        self.icon = self.icon_raw.resize((40, 40), resample=1)
        self.tkIcon = ImageTk.PhotoImage(self.icon)
        #self.RenderUnit()

    # Mirror sprite
    def Mirror(self):
        self.image_raw = self.image_raw.transpose(Image.FLIP_LEFT_RIGHT)
        self.RenderUnit()
    # Turn sprite
    def Rotate(self, side): # sides: 'left', 'right'
        if side == 'right':
            self.image_raw = self.image_raw.transpose(Image.ROTATE_270)
        elif side == 'left':
            self.image_raw = self.image_raw.transpose(Image.ROTATE_90)
        self.RenderUnit()


    ## Binding object to be movable by mouse Drag-n-Drop
    def RenderUnit(self):
        # Image resizing
        imgSizeX, imgSizeY = self.image_raw.size
        self.image = self.image_raw.resize( (int(imgSizeX*self.scaleX*self.devScale), int(imgSizeY*self.scaleY*self.devScale)), resample=1)
        # Image to TK format
        self.tkImage = ImageTk.PhotoImage(self.image)
        # Updating
        self.c.delete(self.obj)
        self.obj = self.c.create_image(self.x, self.y, image=self.tkImage, anchor="center", tags="unit")
        self.c.tag_bind(self.obj, "<ButtonPress-1>", self.OnClick)
        self.c.tag_bind(self.obj, "<B1-Motion>", self.OnDrag)
        self.c.tag_bind(self.obj, "<ButtonRelease-1>", self.OnRelease)

    def OnClick(self, event):
        self.mouseOffsetX = event.x - self.x
        self.mouseOffsetY = event.y - self.y
    def OnDrag(self, event):
        new_x = event.x - self.mouseOffsetX
        new_y = event.y - self.mouseOffsetY
        self.c.coords(self.obj, new_x, new_y)
    def OnRelease(self, event):
        self.x, self.y = self.c.coords(self.obj)
        if self.isSelected:
            self.c.delete('SelectionMarker')
            posX, posY = self.c.coords(self.obj)
            self.c.create_rectangle(posX - self.tkImage.width() / 2, posY - self.tkImage.height() / 2, posX + self.tkImage.width() / 2,
                           posY + self.tkImage.height() / 2, width=1,
                           tags='SelectionMarker')