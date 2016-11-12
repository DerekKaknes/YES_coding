from PIL import Image, ImageFilter
import cv2, unittest, pygame, time, psutil
import numpy as np

class RobotCar:
    def __init__(self, vc):
        self.vc = vc

    def determine_light_color(self, image):
        """Add your code here to determine the color of the light.  Your 
        program should look at the pixel values in the image and then return
        either 'green', 'yellow', or 'red'."""
        return 'red'

    def drive(self, wait=5):
        print "RobotCar is driving - hit escape to exit"
        while True:
            self.analyze_traffic_light()
            key = raw_input('Press Enter to continue or "q" to quit: ')
            if key.lower() == 'q':
                self.release()
                print "Pulling over and shutting down..."
                break

    def analyze_traffic_light(self):
        print "Coming up to a traffic light..."
        im = self.capture_image()
        im.show(title='Traffic Light')
        time.sleep(2)
        im.close()
        for proc in psutil.process_iter():
            if proc.name() == 'Preview' or proc.name().lower() == 'display':
                proc.kill()
        light_color = self.determine_light_color(im)
        self.process_action(light_color)

    def capture_image(self):
        rval = False
        while not rval:
            rval, frame = self.vc.read()
            if rval:
                im = Image.fromarray(frame, mode='RGB')
            return im

    def process_action(self, light_color):
        if light_color == 'green':
            self.green_light()
        elif light_color == 'red':
            self.red_light()
        elif light_color == 'yellow':
            self.yellow_light()
        else:
            raise Exception("Did not recognize light color as either green, yellow or red")

    def green_light(self):
        print "Green Light - Go!"

    def red_light(self):
        print "Red Light - Stop!"

    def yellow_light(self):
        print "Yellow Light - Slow Down!"

    def release(self):
        self.vc.release()

if __name__ == '__main__':
    # Open video capture from computer's webcam
    vc = cv2.VideoCapture(0)
    # Initialize RobotCar with vc
    robot = RobotCar(vc)
    robot.drive()

