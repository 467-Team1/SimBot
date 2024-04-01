import lcm
import numpy as np
import pygame
from lcmtypes import mbot_motor_command_t
from lcmtypes import mbot_encoder_t
import time
import sys
import os

def main():
    lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

    # For Testing Purposes ONLY #
    pygame.init()
    pygame.display.set_caption("MBot TeleOp")
    screen = pygame.display.set_mode([100,100])

    time.sleep(0.5)

    already_bw = False
    already_fw = False

    while True:
        # Exit Condition if Ctrl+C is 
        try:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()

        # Input from Visual Camera Model - Left and Right Hand Gesture
        # gesture_direction = input("Enter Direction: ")
        # gesture_speed = input("Enter Speed: ")
            
        key_input = pygame.key.get_pressed() 

        cur_motor_command = mbot_motor_command_t()
        cur_motor_command.trans_v = 0.0
        cur_motor_command.angular_v = 0.0

        if  key_input[pygame.K_UP]:
            print("Forward")
            if(already_fw == False):
                for inc in np.linspace(0, 0.25, 10):
                    cur_motor_command.trans_v = cur_motor_command.trans_v + inc
                    already_fw = True

        elif key_input[pygame.K_DOWN]:
            print("Backward")
            if(already_bw == False):
                for inc in np.linspace(0, 0.25, 10):
                    cur_motor_command.trans_v = cur_motor_command.trans_v - inc
                    already_bw = True

        elif key_input[pygame.K_LEFT]:
            print("Left")
            if cur_motor_command.trans_v > 0:
                last_speed = cur_motor_command.trans_v
                for inc in np.linspace(0, last_speed, 10):
                    cur_motor_command.trans_v = cur_motor_command.trans_v - inc
            cur_motor_command.angular_v = 0.5

        elif key_input[pygame.K_RIGHT]:
            print("Right")
            if cur_motor_command.trans_v > 0:
                last_speed = cur_motor_command.trans_v
                for inc in np.linspace(0, last_speed, 10):
                    cur_motor_command.trans_v = cur_motor_command.trans_v - inc
            cur_motor_command.angular_v = -0.5

        if key_input[pygame.K_w]:
            print("Slow")
            # Slow down speed until trans_v = 0.05
            while cur_motor_command.trans_v > 0.05:
                cur_motor_command.trans_v -= 0.05
        elif key_input[pygame.K_s]:
            print("Fast")
            # Increase speed until trans_v = 0.5
            while cur_motor_command.trans_v < 0.5:
                cur_motor_command.trans_v += 0.05

        elif key_input[pygame.K_SPACE]:
            print("Stop")
            # Stop the robot
            if cur_motor_command.trans_v > 0:
                while cur_motor_command.trans_v > 0:
                    cur_motor_command.trans_v -= 0.05
            
            elif cur_motor_command.trans_v < 0:
                while cur_motor_command.trans_v < 0:
                    cur_motor_command.trans_v += 0.05

            if cur_motor_command.angular_v > 0:
                while cur_motor_command.angular_v > 0:
                    cur_motor_command.angular_v -= 0.05

            elif cur_motor_command.angular_v < 0:
                while cur_motor_command.angular_v < 0:
                    cur_motor_command.angular_v += 0.05

        lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())
        time.sleep(0.05)


if __name__== "__main__":
    main()