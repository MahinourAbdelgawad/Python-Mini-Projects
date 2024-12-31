import matplotlib.pyplot as plt
import math as math
import sys
import os

arm_length = 10 # each arm segment is 10
og_angle1, og_angle2, og_angle3 = 50, 15, 100 # original angles

def draw_arm(angle1, angle2, angle3):
    angle1 = math.radians(angle1) # trig functions are in radians
    angle2 = math.radians(angle2)
    angle3 = math.radians(angle3)

    # calculating final positions of each joint
    x1 = arm_length * math.cos(angle1)
    y1 = arm_length * math.sin(angle1)

    x2 = x1 + arm_length * math.cos(angle2)
    y2 = y1 + arm_length * math.sin(angle2)

    x3 = x2 + arm_length * math.cos(angle3)
    y3 = y2 + arm_length * math.sin(angle3)

    plt.clf() # clearing the plot to allow changes

    plt.plot([0, x1], [0, y1], marker = "o")
    plt.plot([x1, x2], [y1, y2], marker = "o")
    plt.plot([x2, x3], [y2, y3], marker = "o")
    plt.axis('equal')
    plt.title("Robotic Arm Simulation")


def main():
    plt.ion()
    draw_arm(og_angle1,og_angle2,og_angle3) # display starting position
    curr_angle1, curr_angle2, curr_angle3 = og_angle1, og_angle2, og_angle3

    while True: # to loop until user decides to exit

        os.system("cls" if os.name == "nt" else "clear") # clear terminal each time for cleanliness

        print("""ROBOTIC ARM SIMULATOR
              Select an option by entering the corresponding number:
              (1) Change angle of first joint
              (2) Change angle of second joint
              (3) Change angle of third joint
              (4) Reset Arm
              (5) Exit""")
        
        choice = input()
        while not choice.isdigit() or int(choice) not in range(1,6):
            choice = input("\nInvalid option. Please enter a number from 1 to 5:\n")

        choice = int(choice)

        if choice == 5:
            sys.exit()

        if choice == 4: # reset
            draw_arm(50,15,100)
        else:
            new_angle = input("Enter new angle (in degrees):\n")

            # angle validation
            while True:
                try:
                    new_angle = float(new_angle)
                    if 0 <= new_angle <= 180:
                        break
                    else:
                        new_angle = input("Please enter an angle  between 0 and 180 degrees:\n")
                except ValueError:
                    new_angle = input("Please enter a number:\n")

            new_angle = float(new_angle)

            if choice == 1:
                curr_angle1 = new_angle
            elif choice == 2:
                curr_angle2 = new_angle
            elif choice == 3:
                curr_angle3 = new_angle
            
            draw_arm(curr_angle1, curr_angle2, curr_angle3) # update diagram



        
if __name__ == "__main__":
    main()