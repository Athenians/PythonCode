#!/usr/bin/env python3

from ev3dev2.button import Button
from globals import debug_print
import time
import ev3dev2.fonts as fonts
from  ev3dev2.console import Console

class MenuItem:
    def __init__(self, menu, line,linename, linetype, lineprog):
        self.menu = menu
        self.line = line
        self.linename = linename
        self.linetype = linetype
        self.lineprog = lineprog

class Menu(object):
    def __init(self, menu = 0, line = 0,  **kwargs):
        self.menu = menu
        self.line = line
 

    #sets buttons so when called and pressed will do what was coded to do once pressed
    def left(self,state):
        if state:
            #debug_print('Left button pressed')
            self.menu = self.menu -1
            if self.menu <0:
                self.menu = 0
        #else:
        #    debug_print('Left button released')
        self.refreshflag = True
        return 0

    def right(self,state):  
        if state:
            debug_print('right button pressed')
            #self.turret.on(speed=-45)
        #else:
            #debug_print('right button released')
            #self.turret.off()
        self.refreshflag = True
        return 0

    def up(self,state):
        if state:
            debug_print('Up button pressed')
            self.line = self.line -1
            if self.line <0:
                self.line = self.max_line
        #else:
            #debug_print('Up button released')
        self.refreshflag = True
        return 0

    def down(self,state):
        if state:
            debug_print('Down button pressed')
            self.line = self.line + 1
            if self.line > self.max_line:
                self.line = 0
        #else:
        #    debug_print('Down button released')
        self.refreshflag = True
        return 0

    def enter(self,state):
        if state:
            debug_print('Enter button pressed')
            if self.cur_linetype == 'M':
                self.cur_menu = int(self.cur_lineprog)
                self.cur_line = 0
            else:
                self.cur_lineprog    #this should run the function          
        #else:
        #    debug_print('Enter button released')
        self.refreshflag = True
        return 0

    def getmenuitem(self,menulist,menu,line):
        for obj in menulist:
            if obj.menu == menu and obj.line == line:
                return menulist.linename, menulist.linetype, menulist.lineprog
            else:
                return 'xxx','x','xxx'
  
    def displaymenu(self,menulist,menuname, menu,line):
        lcdfontB = "Lat15-TerminusBold16"       
        lcd = Console(font=lcdfontB)

       #clear screen
        lcd.reset_console()
        #display menu name top center
        lcd.text_at(menuname, column=1,row=1, alignment="C",inverse=True)


        for obj in menulist:
            if obj.menu == menu:
                cur_tuple = self.getmenuitem(menu,obj.menu,obj.line)
                cur_linename = cur_tuple[0]

                lcd.text_at(cur_linename, column = 1,row=2+obj.line, alignment="C",inverse=(obj.line == line))

    def getmaxline(self,menulist,menu):
        maxline = 0
        for obj in menulist:
            if obj.menu == menu:
                if obj.line > maxline:
                    maxline = obj.line
        return maxline

    def runmenu(self):
        #set up menu names
        menuname = []
        menuname.append('Main')
        menuname.append('Tools')
        menuname.append('Missions')

        #setting up the menu lines
        menu = []
        menu.append(MenuItem(0,0,'M',menuname[1],'1'))
        menu.append(MenuItem(0,1,'M',menuname[2],'2'))
        menu.append(MenuItem(0,3,'P','DoIt','all_missions(eve)'))
        menu.append(MenuItem(1,0,'P','AAASetup','eve.aaasetup()'))
        menu.append(MenuItem(1,1,'P','Calibratcs','eve.calibratecs()'))
        menu.append(MenuItem(2,0,'P','mission01','mission01(eve)'))
        menu.append(MenuItem(2,1,'P','mission02','mission02(eve)'))
        menu.append(MenuItem(2,2,'P','mission03','mission03(eve)'))

        cur_menu = 0
        cur_line = 0
        refreshflag = True

        # set up button controls
        btn = Button()
        btn.on_left = self.left
        btn.on_right = self.right
        btn.on_up = self.up
        btn.on_down = self.down
        btn.on_enter = self.enter

        while True:
            if btn.check_buttons(buttons=['backspace']):
                break    
            #calculate max_line based on menu
            self.max_line = self.getmaxline(menu,cur_menu)

            #display menu on screen 
            if refreshflag:
                self.displaymenu(menu,menuname[cur_menu],cur_menu,cur_line)
                refreshflag = False

            btn.process() 
            cur_tuple = self.getmenuitem(menu,cur_menu,cur_line)
            #self.cur_linename = cur_tuple[0]
            self.cur_linetype = cur_tuple[1]
            self.cur_lineprog = cur_tuple[2]

            time.sleep(0.01)





#  these are my notes.

#   pseudo code:

#   Mission xx
#   Place robot in starting position (manually)
#   ensure arm is 0x0
#   Move forward 30mm -- speed normal
#   turn 90deg -- speed normal
#   find line -- speed normal
#   follow line for 300 mm -- speed normal -- left side of line , right sensor
#   turn -90 -- speed normal
#   move forward 50mm -- speed fast
#   arm to 20x0
#   arm to 20x20
#   complete mission
#   go home
#   while going home, arm to 0x0


# commands you'll need
# left_pos = self.left_motor.position      # this gets you the current motor position of the left motor - returns encoder counts
# left_rotations = float(left_pos / self.left_motor.count_per_rot)  # this converts encoder counts to rotations
# left_mm = float(left_rotations * self.Wheel_Dia)  # distance travelled on the LEFT wheel
# current_mm = (left_mm + right_mm) / 2


