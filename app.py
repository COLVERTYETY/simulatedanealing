import pygame as pg
import numpy as np
import time
import noise 
import simAnealing 

def generate(largeur,longueur):
    # noisemachine = noise._perlin.
    # noisemachine.randomize()
    # mysimple = noise._perlin.SimplexNoise(noisemachine)
    matrix = np.zeros((largeur,longueur))
    octave = 4
    seed = np.random.randint(10000)/10000
    #freq = 16* octave
    for x in range(largeur) :
        for y in range(longueur) :
            matrix[x][y] = (abs(noise.pnoise3(x/largeur,y/longueur,seed,octave)**(1/2))* 127.0) + 128.0
    return matrix

def printer(matrix):
    for row in matrix:
        print(row)

def drawmat(matrix,screen):
    (screenw,screenh) = screen.get_size()
    (length,depth) = matrix.shape
    cellw = float(screenw/length)
    cellh = float(screenh/depth)
    colorc = (0,128,128)#mix res
    for x in range(length):
        for y in range(depth):
            #calc color from val of cell
            colorc = (int(matrix[x][y]),0,int((255-matrix[x][y])))
            pg.draw.rect(screen,colorc,pg.Rect(int(cellw*x),int(cellh*y),int(cellw),int(cellh)))

def update(matrix,screen,x,y):
    (screenw,screenh) = screen.get_size()
    (length,depth) = matrix.shape
    cellw = float(screenw/length)
    cellh = float(screenh/depth)
    colorc = (0,128,128)#mix res
    #calc color from val of cell
    colorc = (int(255-matrix[x][y]),0,int((matrix[x][y])))
    pg.draw.rect(screen,colorc,pg.Rect(int(cellw*x),int(cellh*y),int(cellw),int(cellh)))
 
width = 200
height = 200

matrix = generate(width,height)
# printer(matrix)
swidth = 800
sheight = 800
pg.init()
screen = pg.display.set_mode((swidth, sheight))
#drawmat(matrix,screen)
screen.fill((0,0,0))
pg.display.flip()
done = False
kmax = 3000
k=0
solver = simAnealing.searcher2D(width,height)
print(solver.s)
while not done:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True
        if(k<kmax):
            k+=1
            solver.es = matrix[int(solver.s[0])][int(solver.s[1])]
            print(k,solver.es)
            solver.esnew = matrix[int(solver.snew[0])][int(solver.snew[1])]
            update(matrix,screen,int(solver.snew[0]),int(solver.snew[1]))
            solver.evaluate(((kmax-k+1)/kmax))
        #drawmat(matrix,screen)
        #printer(matrix)
        pg.display.flip()