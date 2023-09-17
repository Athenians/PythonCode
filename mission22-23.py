def all_missions(eve):
    debug_print('About to run mission_wndmill')
    mission_windmill(eve)

    debug_print('About to run mission_high_five')
    mission_high_five(eve)

    debug_print('About to run mission_oil_platform')
    mission_oil_platform(eve)


def mission_windmill(eve):
    eve.aaasetup()
    eve.calibrategs()
    #eve.motor_mover(60,-0.77,eve.attach)
    eve.moveblock(25,25,505)
    eve.moveblock(-35,-35,110)
    eve.moveblock(-10,10,45)
    #eve.aaasetup()
    eve.moveblock(40,40,420)
    eve.moveblock(10,-10,90)
    eve.moveblock(20,20,130)

    for x in range (3): 
        #eve.aaasetup
        eve.moveblock(20,20,60)
        time.sleep(0.35)
        eve.moveblock(-20,-20,50)

    '''
    eve.moveblock(30,30,315)
    eve.aaasetup()
    eve.motor_mover(20,1,eve.attach)
    eve.aaasetup()
    '''
    #eve.aaasetup()
     #time.sleep(0.35)
    #eve.aaasetup()
    eve.moveblock(15,15,220)
    #eve.aaasetup()
    eve.motor_mover(10,1.5,eve.attach)
    eve.moveblock(-5,-5,50)
    eve.motor_mover(20,-1.5,eve.attach)
    eve.moveblock(-45,-45,1000)
    eve.moveblock(-35,-10,100)
    eve.motor_mover(10,1.5,eve.attach)

    #eve.aaasetup()


def mission_high_five(eve):
    eve.aaasetup()
    eve.moveblock(40,40,630)
    #eve.aaasetup()
    eve.line_finder(10,10,'r','b')
    eve.moveblock(10,0,180)
    #eve.aaasetup()
    eve.moveblock(20,20,55)
    eve.moveblock(-20,-20,200)
    eve.moveblock(0,10,180)
    eve.moveblock(45,45,870)
    eve.aaasetup()

def mission_oil_platform(eve):
    eve.moveblock(15,15,520)
    for x in range (3): 
        #eve.aaasetup
        eve.moveblock(20,20,40)
        time.sleep(0.35)
        eve.moveblock(-20,-20,40)





