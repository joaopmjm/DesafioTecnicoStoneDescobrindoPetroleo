class grid:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
        self.ships = []
    def addShip(self, navio):
        self.ships.append(navio)
        return self.ships.index(navio)
        
    def setX(self,x):
        self.x = int(x)
        
    def setY(self,y):
        self.y = int(y)
        
    def getLenght(self):
        return self.x
    
    def getHeight(self):
        return self.y
    
    def mount(self, commands, grid):
        com = commands[0]
        x, y = com.split(" ")
        self.setX(x)
        self.setY(y)
        commands = commands[1:len(commands)]
        for i in range(int(len(commands)/2)):
            x = i*2 
            navioX, navioY, navioOri = commands[x].split(" ")
            N = ship(grid)
            N.setX(navioX)
            N.setY(navioY)
            N.setOrientation(navioOri)
            for m in commands[x+1]:
                if m == 'M':
                    N.move()
                elif m == 'L':
                    N.turnLeft()
                elif m == 'R':
                    N.turnRight()
            self.addShip(N)    
    def getShips(self):
        shipos = ""
        for ship in self.ships:
            shipos += ship.getPos() + "\n"
        return shipos

class ship: # Classe navio representa 1 navio sonda
    def __init__(self, gird, x=0, y=0, orientation='E'):
        self.oriMapping = {'E':0,'N':1,'W':2,'S':3}
        self.x = y;            # Posicao X do navio na malha
        self.y = x;            # Posicao Y do navio na malha
        self.grid = gird;
        self.orientation = self.oriMapping[orientation];
    
    def setX(self,x):
        self.x = int(x)
    
    def setY(self, y):
        self.y = int(y)
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setOrientation(self, ori):
        self.orientation = self.oriMapping[ori];
    
    def turnLeft(self): # Giro de 90 graus em sentido anti horario
        self.orientation += 1
        if self.orientation > 3:
            self.orientation = 0
        
    def turnRight(self):  # Giro de 90 graus em sentido horario
        self.orientation -= 1
        if self.orientation < 0:
            self.orientation = 3
    
    def getOrientation(self):
        if self.orientation == 0: return 'E'
        if self.orientation == 1: return 'N'
        if self.orientation == 2: return 'W'
        if self.orientation == 3: return 'S'
        
    def move(self):
        if (self.orientation == 0 and self.x < self.grid.getLenght()):
            self.x += 1
        elif (self.orientation == 1 and self.y < self.grid.getHeight()):
            self.y += 1
        elif (self.orientation == 2 and self.x > 0):
            self.x -= 1
        elif (self.orientation == 3 and self.y > 0):
            self.y -= 1
        else:
            print("Movement to " + self.getOrientation() + " went wrong!")
    
    def getPos(self):
        return str(self.x) + " " + str(self.y) + " " + self.getOrientation()