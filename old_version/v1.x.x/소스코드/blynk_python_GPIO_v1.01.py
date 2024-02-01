"""
* blynk GPIO 제어 프로그램
* 수정 : 2018. 08. 14
* 제작 : eleparts 부설연구소
* SW ver. 1.0.1

기반 코드 및 필수 라이브러리 - blynk / python (Blynk library V0.1.3)
https://github.com/vshymanskyy/blynk-library-python
"""
import BlynkLib
import time
import RPi.GPIO as GPIO 



BLYNK_AUTH = 'YourAuthToken'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.IN)

# Register Virtual Pins
# blynk앱에서 버튼 누를경우 동작(Virtual Pins 1)
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
 
  print('Current V1 value: {}'.format(value))
  if(value == '1'):
    GPIO.output(21, 1)
  else:
    GPIO.output(21, 0)

# blynk앱에서 버튼 누를경우 동작 (Virtual Pins 2)
@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):

  print('Current V2 value: {}'.format(value))
  if(value == '1'):
    GPIO.output(20, 1)
  else:
    GPIO.output(20, 0)


# blynk앱에서 주기적으로 호출하도록 설정 (Virtual Pins 3)
@blynk.VIRTUAL_READ(3)
def my_read_handler():
  
  SW = GPIO.input(16)

  try:  
    if(SW != my_read_handler.lastSW):
      print("SW GPIO value : %d "% (SW))

      if(SW):
        blynk.virtual_write(3, " ON")
        my_read_handler.lastSW = SW
        
      else:
        blynk.virtual_write(3, "OFF")
        my_read_handler.lastSW = SW

  # 최초 1회 변수 선언
  except AttributeError:
    my_read_handler.lastSW = False


# 설정해 둔 시간마다 실행됨
def my_user_task():
  # do any non-blocking operations
  
  try:
    if(my_user_task.LED_flag):
      blynk.virtual_write(4, 255)
      my_user_task.LED_flag = False
    else:
      blynk.virtual_write(4, 0)
      my_user_task.LED_flag = True

  # 최초 1회 변수 선언
  except AttributeError:
    my_user_task.LED_flag = True
    blynk.virtual_write(4, 255)



# my_user_task / 2000ms
blynk.set_user_task(my_user_task, 2000)


# Start Blynk (this call should never return)
blynk.run()