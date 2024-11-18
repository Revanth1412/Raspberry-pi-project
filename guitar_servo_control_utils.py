import pigpio # !pip install pigpio
import time

RPI_IP = "192.168.1.12" # Ip address of the raspberry pi in the local network (can change everytime rpi boots)
RPI_PORT = 8888  # Default port for pigpio

pwm = pigpio.pi(RPI_IP, RPI_PORT)

class GuitarServo:
    def __init__(self, GPIO_pin_number, start_pulsewidth, end_pulsewidth):
        # pulse width of tower pro sg servo varies from 500 to 2500
        self.start_pulsewidth = start_pulsewidth
        self.end_pulsewidth = end_pulsewidth
        self.GPIO_pin_number = GPIO_pin_number # use BCM numbering
        self.position = None
        self._initialize()
    
    def move_to_start_position(self):
        print("moving to start position")
        pwm.set_servo_pulsewidth(self.GPIO_pin_number, self.start_pulsewidth)
        self.position = "start"
    
    def move_to_end_position(self):
        pwm.set_servo_pulsewidth(self.GPIO_pin_number, self.end_pulsewidth)
        self.position = "end"
    
    def pluck_string(self):
        if self.position == "start":
            self.move_to_end_position()
        elif self.position == "end":
            self.move_to_start_position()
    
    def _initialize(self):
        pwm.set_mode(self.GPIO_pin_number, pigpio.OUTPUT)
        pwm.set_PWM_frequency(self.GPIO_pin_number, 50) # frequency of pulse width modulation
        self.move_to_start_position()


# tune the start_pulsewith and end_pulsewidth (used for pluck action) for all servos empirically
guitar_servo_1 = GuitarServo(GPIO_pin_number=21, start_pulsewidth=500, end_pulsewidth=1000)
guitar_servo_2 = GuitarServo(GPIO_pin_number=22, start_pulsewidth=500, end_pulsewidth=1000)
guitar_servo_3 = GuitarServo(GPIO_pin_number=23, start_pulsewidth=500, end_pulsewidth=1000)
guitar_servo_4 = GuitarServo(GPIO_pin_number=24, start_pulsewidth=500, end_pulsewidth=1000)
guitar_servo_5 = GuitarServo(GPIO_pin_number=25, start_pulsewidth=500, end_pulsewidth=1000)
guitar_servo_6 = GuitarServo(GPIO_pin_number=26, start_pulsewidth=500, end_pulsewidth=1000)

# example usage -> guitar_servo_1.pluck_string()
# guitar_servo_6.pluck_string()

time.sleep(10) # waiting to finish all the requests to pi

