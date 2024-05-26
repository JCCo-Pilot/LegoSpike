import runloop, color_matrix,color_sensor,distance_sensor, force_sensor, hub, motor
from hub import light_matrix, port
import color
speed = 300
armMove = -210

#armUp = motor.absolute_position(port.D) >200
armUp = True

#Async Methods that work
async def move(numRotations):
    motor.run_for_degrees(port.A,-360*numRotations,speed)
    motor.run_for_degrees(port.E,360*numRotations,speed)
async def moveBack():
    motor.run_for_degrees(port.A,360,speed)
    await motor.run_for_degrees(port.E,-360,speed)
async def moveForward():
    motor.run_for_degrees(port.A,-360,speed)
    await motor.run_for_degrees(port.E,360,speed)
async def rotateLeftNinety():
    await motor.run_for_degrees(port.A,295,speed)
    await motor.run_for_degrees(port.E,0,speed)
async def rotateRightNinety():
    await motor.run_for_degrees(port.E,295,speed)
    await motor.run_for_degrees(port.A,0,speed)
async def followBlackLine():
    if 

#non-async
def readColorSensor():
    if color_sensor.color(port.B) is color.RED:
        print("Red")
    if color_sensor.color(port.B) is color.GREEN:
        print("Green")
    if color_sensor.color(port.B) is color.BLUE:
        print("Blue")
    if color_sensor.color(port.B) is color.MAGENTA:
        print("Magenta")
    if color_sensor.color(port.B) is color.YELLOW:
        print("Yellow")
    if color_sensor.color(port.B) is color.ORANGE:
        print("Orange")
    if color_sensor.color(port.B) is color.AZURE:
        print("Azure")
    if color_sensor.color(port.B) is color.BLACK:
        print("Black")
    if color_sensor.color(port.B) is color.WHITE:
        print("White")
def moveBackSim():
    motor.run_for_degrees(port.A,360,speed)
    motor.run_for_degrees(port.E,-360,speed)
def moveForwardSim():
    motor.run_for_degrees(port.A,-360,speed)
    motor.run_for_degrees(port.E,360,speed)
def rotateLeftNinetySim():
    motor.run_for_degrees(port.A,295,speed)
    motor.run_for_degrees(port.E,0,speed)
def rotateRightNinetySim():
    motor.run_for_degrees(port.E,295,speed)
    motor.run_for_degrees(port.A,0,speed)
#methods that kinda work
async def runIntoWall():
    distance = distance_sensor.distance(port.F)
    #distance in millimeters
    while distance>100 :
        #print(distance)
        #motor.run_for_degrees(port.A,10,speed)
        #motor.run_for_degrees(port.E,10,speed)
        distance = distance_sensor.distance(port.F)
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
#main methods
async def main():
    # write your code here
    light_matrix.write("Hi!")
    readColorSensor()
    #await runIntoWall()
    #moveArmUp()
    #moveArmDown() 

runloop.run(main())
