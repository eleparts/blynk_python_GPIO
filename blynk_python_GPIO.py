"""
* blynk GPIO 제어 프로그램 blynk 2.0 대응
* 수정 : 2024. 01. 31
* 제작 : eleparts 부설연구소
* SW ver. 3.0.0

3.0.0 변경사항
> blynk 2.0 대응 업데이트
blynk-library-python 최신버전 v1.0.0 을 직접 받아 설치해야 합니다.

기반 코드 및 필수 라이브러리 - blynk / python (Blynk Python Library V1.0.0)
https://github.com/vshymanskyy/blynk-library-python
> 공식 저장소(2.x.x 라이브러리)에서 기존 라이브러리로 변경(1.x.x 라이브러리) 
"""

import BlynkLib
import RPi.GPIO as GPIO 
from BlynkTimer import BlynkTimer

#이메일로 받은 토큰을 여기에 추가
BLYNK_AUTH = 'YourAuthToken'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()

# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.IN, GPIO.PUD_DOWN)


# 부팅 시 서버 데이터 받아와 동기화 - LED 상태 동기화
@blynk.on("connected")
def blynk_connected():
    print("Updating V1,V2 values from the server...")
    blynk.sync_virtual(1,2)

# Virtual 핀 변경사항 터미널에 출력 - 디버그
@blynk.on("V*")
def blynk_handle_vpins(pin, value):
    print("V{} value: {}".format(pin, value))



# Register Virtual Pins
# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 1)
@blynk.on("V1")
def handler_V1(value):
    if(value == ['1']):
        GPIO.output(21, 1)
    else:
        GPIO.output(21, 0)

# blynk앱에서 버튼 누를경우 동작 - write (Virtual Pins 2)
@blynk.on("V2")
def handler_V2(value):
    if(value == ['1']):
        GPIO.output(20, 1)
    else:
        GPIO.output(20, 0)



# 타이머 테스트용 함수 - 최초 1회
def hello_world():
    print("Hello World!")

# 타이머 사용해 주기적으로 GPIO 읽어 변경 시 blynk앱으로 전송 - (Virtual Pins 3)
@blynk.on("V3")
def handler_V3():
    SW = GPIO.input(16)

    try:  
        if(SW != handler_V3.lastSW):
            print("SW GPIO value : %d "% (SW))

            if(SW):
                blynk.virtual_write(3, " ON")
                handler_V3.lastSW = SW
                
            else:
                blynk.virtual_write(3, "OFF")
                handler_V3.lastSW = SW

    # 최초 1회 - 스위치 기존 value값 저장용 변수 선언
    except AttributeError:
        handler_V3.lastSW = False

# 타이머 테스트용 함수 - LED ON/OFF (Virtual Pins 4)
@blynk.on("V4")
def LED_task():

    try:
        if(LED_task.LED_flag):
            blynk.virtual_write(4, 255)   # Vpin =  4, value = 255
            LED_task.LED_flag = False
            #print("V4 LED ON")
        else:
            blynk.virtual_write(4, 0)     # Vpin =  4, value = 0
            LED_task.LED_flag = True
            #print("V4 LED OFF")

    # 최초 1회 변수 선언
    except AttributeError:
        LED_task.LED_flag = True
        blynk.virtual_write(4, 255)
        #print("V4 LED ON")

# Add Timers
# timer : 설정해 둔 시간마다 실행됨
timer.set_timeout(1, hello_world) # 최초 1회, 1초후 실행
timer.set_interval(1, handler_V3) # 1초마다 반복실행
timer.set_interval(3, LED_task) # 3초마다 반복실행


# Start Blynk, Start timer
while True:
    blynk.run()
    timer.run() 
