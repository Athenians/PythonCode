from ev3dev2.button import Button
from globals import debug_print
import time
import ev3dev2.fonts as fonts
from  ev3dev2.console import Console
from ev3dev2.led import Leds
from myblocks import *

leds = Leds()
class MenuItem:
    def __init__(self, menu, line, linetype, linename, lineprog):
        self.menu = menu
        self.line = line
        self.linetype = linetype        
        self.linename = linename
        self.lineprog = lineprog 

class Menu(object):
    def __init__(self, cur_menu=0, cur_line=0, lcd= Console(font="Lat15-TerminusBold16"), menuname=[],menu=[] ):
        self.cur_menu = cur_menu
        self.cur_line = cur_line
        self.lcd = lcd
        self.menuname = menuname
        self.menu = menu

    #sets buttons so when called and pressed will do what was coded to do once pressed
    def left(self,state):
        if not state:
            debug_print('xLeft button pressed')
            self.cur_menu = self.cur_menu - 1
            if self.cur_menu <0:
                self.cur_menu = 0
            self.refreshflag = True
        return 0

    def right(self,state):  
        if not state:
            debug_print('xright button pressed')
            self.cur_menu = 0
            self.cur_line = 0
            self.refreshflag = True       
        return 0

    def up(self,state):
        if not state:
            debug_print('xUp button pressed')
            self.cur_line = self.cur_line -1
            if self.cur_line <0:
                self.cur_line = self.max_line
            self.refreshflag = True       
        return 0

    def down(self,state):
        if not state:
            debug_print('xDown button')
            self.cur_line = self.cur_line + 1
            if self.cur_line > self.max_line:
                self.cur_line = 0
            self.refreshflag = True       
        return 0

    def enter(self,state):
        if not state:
            debug_print('xEnter button pressed')
            if self.cur_linetype == 'M':
                self.cur_menu = int(self.cur_lineprog)
                self.cur_line = 0
            else:
                # run the function
                self.lcd.text_at(self.cur_lineprog, column=1,row=1, reset_console = True,inverse=True)
                debug_print('cur_lineprog: ' + self.cur_lineprog)
                function=getattr(self.eve,self.cur_lineprog)
                debug_print('function: ' + str(function))
                leds.set_color('LEFT','YELLOW')
                leds.set_color('RIGHT','YELLOW')                
                function()
       
        self.refreshflag = True
        return 0

    def getmenuitem(self,imenu,iline):
        #debug_print('getmenuitem: ' +'imenu: ' + str(imenu) + ' iline: ' + str(iline) )
        for x in self.menu:
            #debug_print('getmenuitem: ' + ' x.menu: ' + str(x.menu) +' x.line: ' + str(x.line) )
            if x.menu == imenu and x.line == iline:
                return x.linename, x.linetype, x.lineprog
            
        return 'xxx','x','xxx'
  
    def displaymenu(self):

        #display menu name top center
        self.lcd.text_at(self.menuname[self.cur_menu], column=1,row=1, reset_console = True,inverse=True)

        debug_print('menuname: ' + self.menuname[self.cur_menu])
        #print(self.menuname[self.cur_menu])

        for obj in self.menu:
            if obj.menu == self.cur_menu:
                cur_tuple = self.getmenuitem(obj.menu, obj.line)
                cur_linename = cur_tuple[0]
                xrow = obj.line + 1
                xdisplay = str(xrow) + '. ' + cur_linename 
                debug_print(' line: ' + xdisplay + ' cur: ' + str(obj.line == self.cur_line))
                self.lcd.text_at(xdisplay, column = 2,row=xrow + 2,inverse=(obj.line == self.cur_line))
        print()

    def getmaxline(self):
        maxline = 0
        for obj in self.menu:
            if obj.menu == self.cur_menu:
                if obj.line > maxline:
                    maxline = obj.line
        return maxline

    def runmenu(self,eve):
        debug_print('menu start')
        self.eve = eve

        #set up menu names
        self.menuname = []
        self.menuname.append('Main')
        self.menuname.append('Tools')
        self.menuname.append('Missions')

        debug_print('menu name' + self.menuname[0])
        #setting up the menu lines
        self.menu = []
        self.menu.append(MenuItem(0,0,'M',self.menuname[1],'1'))
        self.menu.append(MenuItem(0,1,'M',self.menuname[2],'2'))
        self.menu.append(MenuItem(0,2,'P','DoIt','all_missions'))
        self.menu.append(MenuItem(1,0,'P','AAASetup','aaasetup'))
        self.menu.append(MenuItem(1,1,'P','Calibratcs','calibratecs'))
        self.menu.append(MenuItem(2,0,'P','Pickle_Dragon','mission_pickle_dragon'))
        self.menu.append(MenuItem(2,1,'P','M02','M02'))
        self.menu.append(MenuItem(2,2,'P','oil_platform','mission_oil_platform'))
    


        self.cur_menu = 0
        self.cur_line = 0
        self.refreshflag = True

        # set up button controls
        btn = Button()
        btn.on_left = self.left
        btn.on_right = self.right
        btn.on_up = self.up
        btn.on_down = self.down
        btn.on_enter = self.enter

        while True:
            if btn.check_buttons(buttons=['backspace']):
                debug_print('xbackspace button pressed')
                break    
            
            btn.process() 
 
            #display menu on screen only if a button is pushed
            if self.refreshflag:
                #calculate max_line based on menu
                self.max_line = self.getmaxline()   

                debug_print('bcur_menu: ' + str(self.cur_menu) + ' cur_line: ' + str(self.cur_line))             
                debug_print('max_line: ' + str(self.max_line))             
                
                #parse list for current menu and item
                cur_tuple = self.getmenuitem(self.cur_menu, self.cur_line)
                #self.cur_linename = cur_tuple[0]
                self.cur_linetype = cur_tuple[1]
                self.cur_lineprog = cur_tuple[2]                           

                self.displaymenu()
                self.refreshflag = False
 
                time.sleep(0.1)
                
        debug_print('menu End')
