from RobotArm import SmartRobotArm

robotArm = SmartRobotArm()
robotArm.loadMyLevel([[],["green"],["white"],["green","white"],["red","white"],["white","white"],["blue"],["blue","blue","blue"],["blue", "green", "green"],["red"]])

# Jouw python instructies zet je vanaf hier:
robotArm.moveRightTimes(6)
print(robotArm.getStackSize())

robotArm.moveLeftTimes(3)

robotArm.moveLeft()

robotArm.moveTo(5)
robotArm.moveTo(1)
robotArm.moveTo(1)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()