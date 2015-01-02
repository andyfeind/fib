from scene import *
import scene

from fib import fib_seq
from random import random
import sys

import photos


class fScene (Scene):
    def setup(self):
        # This will be called before the first frame is drawn.

        self.cellSize = (50,50)
        self.offset = (100,100)
        self.cellSpacing = (10,10)
        self.nrCells = 10
        self.fibseq = fib_seq(self.nrCells)
        #self.cells = []
        
        print self.fibseq
        #self.bgimage = photos.get_fullscreen_image()

        self.root_layer = Layer(Rect(
            self.offset[0],
            self.offset[1],
            self.size.w - self.offset[0] * 2,
            self.size.h - self.offset[1] * 2
        ))
        #self.root_layer.image = self.bgimage
        #print self.root_layer.frame
        #self.root_layer.background = Color(0.5, 0.5, 0.5)

        ii = [
            int((random() * 0.6 + 0.4) * self.cellSize[0])
            for n in range(self.nrCells)
        ]
        #n = 0 
        jj =[
            int((random() * 0.6 + 0.4) * self.cellSize[1])
            for n in range(self.nrCells)
        ]
                                          
        #print ii, jj
        
        #i = 0
        #j = 0
        for idx, i in enumerate(ii):
            for jdx, j in enumerate(jj):
                #rect(
                #    idx * (i + se
                posx = sum(ii[:idx]) + idx * self.cellSpacing[0]
                posy = sum(jj[:jdx]) + jdx * self.cellSpacing[1]
                #print idx, jdx, sum(ii[:idx]), sum(jj[:jdx]), posx, posy, i, j
                layer = Layer(Rect(posx, posy, i, j))
                alpha = 0.8
                layer.background = Color(1, 1, 1, alpha)
                #layer.background = Color(random(), 1, 1, alpha)
                #'''
                layer.animate(
                    'alpha', 
                    0.0, 
                    duration=random() * 0.6 + 0.4, 
                    #delay=jdx,
                    curve=curve_bounce_in,
                    autoreverse=True, 
                    repeat=sys.maxint
                )#'''
                self.root_layer.add_layer(layer)
        #for i in range(self.nrCells):
            
            '''
            for j in range(self.nrCells):
                #self.cells.append((
                rsizex = self.cellSize[0] * random()                                    
                layer = Layer(Rect(
                    i * (self.cellSize[0] + self.cellSpacing[0]),
                    j * (self.cellSize[1] + self.cellSpacing[1]),
                    self.cellSize[0],
                    self.cellSize[1]
                    #rrsize,
                    #rrsize
                    ))
                #alpha = random()
                
                alpha = 1
                layer.background = Color(1, 1, 1, alpha)
                layer.animate(
                    'alpha', 
                    0.0, 
                    duration=random() * 0.6 + 0.4, 
                    delay=random() * 0.4 + 0.6,
                    curve=curve_bounce_in,
                    autoreverse=True, 
                    repeat=sys.maxint
                )
                
                rdur = random() * 0.6 + 0.4
                rdel = random() * 0.4 + 0.6
                rscale = random() * 0.6 + 0.4
                
                layer.animate(
                    'scale_x', 
                    rscale,
                    duration=rdur, 
                    delay=rdel,
                    #curve=curve_bounce_in,
                    autoreverse=True, 
                    repeat=sys.maxint
                )               #)
                layer.animate(
                    'scale_y', 
                     rscale, 
                     duration=rdur, 
                     delay=rdel,
                     #curve=curve_bounce_in,
                     autoreverse=True, 
                     repeat=sys.maxint
                )               #)                
                #'''
                #self.root_layer.add_layer(layer)
                
        #print self.root_layer.sublayers
        #print dir(self.root_layer)
    
    def draw(self):
        # This will be called for every frame (typically 60 times per second).
        background(0, 0, 0)
        #scene.image(self.bgimage, 0,0, self.size.w, self.size.h)       
        # Draw a red circle for every finger that touches the screen:
        #for touch in self.touches.values():rn
        #    ellipse(touch.location.x - 50, touch.location.y - 50, 100, 100)

        #for layer in self.root_layer.sublayers:
        #    layer.update(self.dt)
        #    layer.draw()
        self.root_layer.update(self.dt)
        self.root_layer.draw()
        '''
        revfib = self.fibseq[::-1]
        for i, f in enumerate(revfib):
            rect(
                 i * (self.cellSize[0]) + sum(revfib[:i]),
                 0,
                 f * self.cellSize[0],
                 f * self.cellSize[1]
            )
        #
        for cell in self.cells:
            fill(1, 1, 1, cell[4])
            rect(
                cell[0],
                cell[1],
                cell[2],
                cell[3]
            )
        

    def touch_began(self, touch):
        pass
    
    def touch_moved(self, touch):
        pass

    def touch_ended(self, touch):
        pass
        '''
run(fScene())
