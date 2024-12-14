from djitellopy import Tello
import time

tello = Tello()
tello.connect()

tello.takeoff()

tello.move_up(100)


tello.land()


# tello.send_rc_control(0,0,0,100)
# time.sleep(3)
# tello.send_rc_control(0,0,0,0)

# tello.land()



