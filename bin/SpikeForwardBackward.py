import runloop, color_matrix,color_sensor,distance_sensor, force_sensor, hub, motor
from hub import light_matrix, port
speed = 300
armMove = -210

#armUp = motor.absolute_position(port.D) >200
armUp = True
#176->26 -> arm
async def moveBack():
    motor.run_for_degrees(port.A,360,speed)
    await motor.run_for_degrees(port.E,-360,speed)
async def moveForward():
    motor.run_for_degrees(port.A,-360,speed)
    await motor.run_for_degrees(port.E,360,speed)
def moveArmUp():
    global armUp
    if armUp== False:
        motor.run_for_degrees(port.D,-armMove,speed)
        armUp = True
        print("yes")

def moveArmDown():
    global armUp
    if armUp :
        motor.run_for_degrees(port.D,armMove,speed)
        armUp = False
    
async def main():
    # write your code here
    #await light_matrix.write("Hi!")
    await moveBack()
    await moveForward()
    await moveBack()
    await moveForward()
    await moveBack()
    await moveForward()
    await moveBack()
    await moveForward()
    await moveBack()
    await moveForward()
    await moveBack()
    await moveForward()
    #moveArmUp()
    #moveArmDown() 

runloop.run(main())
