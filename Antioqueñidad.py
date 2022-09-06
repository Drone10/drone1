import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

print(tello.get_battery())
tello.takeoff()
tello.set_speed(50)
tello.move_up(100)

cv2.imwrite("picture6.png", frame_read.frame)

tello.move_forward(330)

tello.rotate_clockwise(90)

tello.flip_right()

cv2.imwrite("picture7.png", frame_read.frame)

tello.move_forward(100)
tello.rotate_clockwise(180)
cv2.imwrite("picture8.png", frame_read.frame)
tello.flip_right()
tello.move_right(100)

tello.rotate_counter_clockwise(270)
tello.move_down(50)
tello.move_back(150)
tello.go_xyz_speed(100,-100,100,50)
tello.go_xyz_speed(-100,100,-100,50)
tello.flip_forward()
tello.move_forward(100)
tello.flip_back()
tello.move_back(200)
tello.move_left(150)
tello.move_back(100)
print(tello.get_battery())


tello.land()