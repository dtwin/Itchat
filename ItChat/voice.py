# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time
import atexit
# 这个类表示单个的SG90模块


class Steering:
    max_delay = 0.2
    min_delay = 0.04

    def __init__(self, channel1,channel2, init_position1,init_position2, min_angle, max_angle, speed):
        self.channel1 = channel1
        self.channel2 = channel2
        self.init_position1 = init_position1
        self.init_position2 = init_position2
        self.position1 = init_position1
        self.position2 = init_position2
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.speed = speed

        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel1, GPIO.OUT, initial=False)
        GPIO.setup(self.channel2, GPIO.OUT, initial=False)

        self.pwm1 = GPIO.PWM(self.channel1, 50)  # PWM
        self.pwm2 = GPIO.PWM(self.channel2, 50)  # PWM
        self.pwm1.start(2.5 + 10 * self.position1 / 180)  # 让舵机1转到初始位置
        self.pwm2.start(2.5 + 10 * self.position2 / 180)  # 让舵机2转到初始位置
        time.sleep(Steering.max_delay)
        self.pwm1.ChangeDutyCycle(0)  # 这一步比较重要，如果不加的话，舵机会不规则抖动（具体原因还不知道）
        self.pwm2.ChangeDutyCycle(0) 
        time.sleep(Steering.min_delay)

    def forwardRotation(self):
        print("current postion: " + str(self.position1))

        if (self.position1 + self.speed) <= self.max_angle:
            self.position1 = self.position1 + self.speed
            self.pwm1.ChangeDutyCycle(2.5 + 10 * self.position1 / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm1.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)

    def reverseRotation(self):
        print("current postion: " + str(self.position1))

        if (self.position1 - self.speed) >= self.min_angle:
            self.position1 = self.position1 - self.speed
            self.pwm1.ChangeDutyCycle(2.5 + 10 * self.position1 / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm1.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)

    def UpRotation(self):
        print("current postion: " + str(self.position2))

        if (self.position2 + self.speed) <= self.max_angle:
            self.position2 = self.position2 + self.speed
            self.pwm2.ChangeDutyCycle(2.5 + 10 * self.position2 / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm2.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)

    def DownRotation(self):
        print("current postion: " + str(self.position2))

        if (self.position2 + self.speed) <= self.max_angle:
            self.position2 = self.position2 + self.speed
            self.pwm2.ChangeDutyCycle(2.5 + 10 * self.position2 / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm2.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)

    def reset(self):
        '''
        Reset the steering to the middle
        '''
        self.position1 = self.init_position1
        self.position2 = self.init_position2
        self.pwm1.start(2.5 + 10 * self.init_position1 / 180)  # 让舵机转到初始位置
        self.pwm2.start(2.5 + 10 * self.init_position2 / 180) 
        time.sleep(Steering.max_delay)
        self.pwm1.ChangeDutyCycle(0)  # 这一步比较重要，如果不加的话，舵机会不规则抖动（具体原因还不知道）
        self.pwm2.ChangeDutyCycle(0) 
        time.sleep(Steering.min_delay)

    def stop(self):
        self.pwm.stop()
        time.sleep(Steering.max_delay)
        GPIO.cleanup()


if __name__ == "__main__":
    steer = Steering(23, 21, 90, 90, 0, 180, 10)
    while True:
        direction = input("Please input direction ~UP=1;DOWN=2;LEFT=3;RIGHT=4;STOP=0~:")
        
        if direction == 1:
            steer.UpRotation()
        elif direction == 2:
            steer.DownRotation()
        elif direction == 3:
            steer.forwardRotation()
        elif direction == 4:
            steer.reverseRotation()
        elif direction == 0:
            steer.stop()
        
        
