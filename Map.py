from PIL import Image, ImageTk, ImageEnhance

class Map:

    @classmethod
    def InitModule(cls, canvas):
        cls.c = canvas
        cls.background = cls.c.create_image(0, 0, anchor="nw", image=cls.bgConfig['imageInstance'], tags="ROOT")

    gridConfig = {
        'isActive' : True,
        'offsetX' : 0,
        'offsetY' : 0,
        'gridSizeX' : [50, 50],
        'gridSizeY' : [50, 50],
        'color' : '#606060',
        'width': 1
    }
    bgConfig = {
        'path' : None,
        'imageInstance' : None,
        'brightness' : 1
    }

    @classmethod
    def DrawGrid(cls):
        c = cls.c
        c.delete("grid")
        gridSizeX = Map.gridConfig['gridSizeX']; gridSizeY = Map.gridConfig['gridSizeY']
        offX, offY = (Map.gridConfig['offsetX'], Map.gridConfig['offsetY'])

        # Vertical lines
        c.create_line(600, 0, 600, 800, tags="grid", fill=Map.gridConfig['color'], width=Map.gridConfig['width'])
        i = 0
        while i * gridSizeX[1] < 600:
            c.create_line(600 - i * gridSizeX[1], 0, 600 - i * gridSizeX[0], 800, tags="grid",
                          fill=Map.gridConfig['color'], width=Map.gridConfig['width'])
            c.create_line(600 + i * gridSizeX[1], 0, 600 + i * gridSizeX[0], 800, tags="grid",
                          fill=Map.gridConfig['color'], width=Map.gridConfig['width'])
            i += 1

        # Horizontal lines
        n = int(1600 / (gridSizeY[0]+gridSizeY[1]))
        d = (gridSizeY[0]-gridSizeY[1])/(n-1)
        currentY = 800-gridSizeY[0]; i = 1
        while currentY > 0:
            c.create_line(0, int(currentY), 1200, int(currentY), tags="grid",
                          fill=Map.gridConfig['color'], width=Map.gridConfig['width'])
            currentY -= (gridSizeY[0]-d*i); i += 1

        # Z axis
        cls.c.tag_lower('grid')
        cls.c.tag_lower('ROOT')

    @classmethod
    def ToggleGrid(cls):
        c = cls.c
        if Map.gridConfig['isActive']:
            c.delete("grid")
            Map.gridConfig['isActive'] = False
        else:
            Map.DrawGrid()
            Map.gridConfig['isActive'] = True

    @classmethod
    def UpdateBackground(cls):
        temp = Image.open(cls.bgConfig['path'])
        temp = temp.resize( (1200, 800) , resample=1)
        enhancer = ImageEnhance.Brightness(temp)
        cls.bgConfig['imageInstance'] = ImageTk.PhotoImage(enhancer.enhance(Map.bgConfig['brightness']))
        cls.c.itemconfig(cls.background, image=cls.bgConfig['imageInstance'])



