"""
* blynk GPIO 제어 프로그램
* 수정 : 2019. 07. 19
* 제작 : eleparts 부설연구소
* SW ver. 2.0.0

2.0.0 변경사항
> blynk.io 홈페이지에 업로드된 라이브러리로 대체되었습니다. 
>기존 버전은 old_version 디렉터리로 이동됨

기반 코드 및 필수 라이브러리 - blynk / python (Blynk Python Library V0.2.4)
https://github.com/blynkkk/lib-python
"""

import blynklib
import blynktimer
import RPi.GPIO as GPIO 

#이메일로 받은 토큰을 여기에 추가
BLYNK_AUTH = 'YourAuthToken'


# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = blynktimer.Timer()

# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.IN, GPIO.PUD_DOWN)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"


# Register Virtual Pins
# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 1)
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
  print(WRITE_EVENT_PRINT_MSG.format(pin,value))

  if(value == ['1']):
    GPIO.output(21, 1)
  else:
    GPIO.output(21, 0)

# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 2)
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
  print(WRITE_EVENT_PRINT_MSG.format(pin,value))

  if(value == ['1']):
    GPIO.output(20, 1)
  else:
    GPIO.output(20, 0)


# blynk앱에서 주기적으로 호출하도록 설정 - Read (Virtual Pins 3)
@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin):
  
  SW = GPIO.input(16)

  try:  
    if(SW != read_virtual_pin_handler.lastSW):
      print(READ_PRINT_MSG.format(pin))
      print("SW GPIO value : %d "% (SW))

      if(SW):
        blynk.virtual_write(3, " ON")
        read_virtual_pin_handler.lastSW = SW
        
      else:
        blynk.virtual_write(3, "OFF")
        read_virtual_pin_handler.lastSW = SW

  # 최초 1회 - 스위치 기존 value값 저장용 변수 선언
  except AttributeError:
    read_virtual_pin_handler.lastSW = False



# Add Timers
# timer : 설정해 둔 시간마다 실행됨
@timer.register(interval=1, run_once=True) # 최초 1회, 1초후 실행
def hello_world():
  print("Hello World!")


@timer.register(interval=2, run_once=False) # 2초마다 반복실행
def my_user_task():

  try:
    if(my_user_task.LED_flag):
      blynk.virtual_write(4, 255)   # Vpin =  V4, value = 255
      my_user_task.LED_flag = False
      #print("V4 LED ON")
    else:
      blynk.virtual_write(4, 0)     # Vpin =  V4, value = 0
      my_user_task.LED_flag = True
      #print("V4 LED OFF")

  # 최초 1회 변수 선언
  except AttributeError:
    my_user_task.LED_flag = True
    blynk.virtual_write(4, 255)
    #print("V4 LED ON")


# Start Blynk, Start timer
while True:
  blynk.run()
  timer.run()
