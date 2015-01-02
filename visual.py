from scene import *

from fib import fib_seq, fib_pos, fib_spiral

NRCELLS = 500

class MyScene (Scene):
    def setup(self):
        self.nrCells = 10
        self.cellsize = 15
        #self.fibseq = fib_seq(self.nrCells)
        #print self.fibseq
        self.origin = (self.size.w / 2.0, self.size.h / 2.0)
        self.scale = 15.0
    
    def draw(self):
        # This will be called for every frame (typically 60 times per second).
        background(0, 0, 0)
        # Draw a red circle for every finger that touches the screen:
        fill(1, 0, 0)
        for touch in self.touches.values():
            ellipse(touch.location.x - 50, touch.location.y - 50, 100, 100)

        noce = self.nrCells
#        for i in range(1, noce):
#        for i in range(1, self.nrCells):
#            pos = fib_pos(i*21)
#            fill(0.7,0.5,0, 1.0-i/noce+0.1)
#            ellipse(
#                pos[0] * self.scale + self.origin[0],
#                pos[1] * self.scale + self.origin[1],
#                self.cellsize, self.cellsize)
        spiral = fib_spiral(89, noce)
        for p in spiral:
           ellipse(
                p[0] * self.scale + self.origin[0],
                p[1] * self.scale + self.origin[1],
                self.cellsize, self.cellsize)
    
    def touch_began(self, touch):
        pass
    
    def touch_moved(self, touch):
        pass

    def touch_ended(self, touch):
        pass

run(MyScene())
