
# Blynk python GPIO예제 for 라즈베리파이

**라즈베리파이**에서 사용되는 **Blynk python 버전**의 예제 소스입니다.
Blynk python 구성품 키트 정보는 아래 페이지를 참고 해 주세요
-준비 중


## menual

사용자  매뉴얼 입니다.

- 제품 구성 및 조립 방법 등이 자세히 설명되어 있습니다.
-준비 중


## blynk_python_GPIO.py

https://github.com/vshymanskyy/blynk-library-python

위 라이브러리를 설치 후 파일을 실행해 주면 됩니다.  
``sudo puthon3 blynk_python_GPIO.py``

>라즈베리파이에서 위 라이브러리 설치 시 아래 명령으로 실행해야 합니다.  
>(python3 사용)  
>``sudo pip3 install blynk-library-python``



## blynk_GPIO.fzz
fritzing 확장자 파일입니다.  
fritzing이 설치되어 있다면 열어보실 수 있습니다.  
http://fritzing.org/home/  


## blynk_GPIO.png
회로 구성 이미지 파일입니다.  
예제코드 동작 전에 해당 회로를 똑같이 구성해 주셔야 합니다.


## 소스코드 폴더

**소스 코드**가 버전별로  **.py** 파일로 저장되어 있습니다.


### 버전별 기능 추가 내역

- blynk_python_GPIO_v1.00  
기본 예제 코드입니다.  
> 2개의 VIRTUAL_WRITE  
> 1개의 VIRTUAL_READ  
> my_user_task 작업으로 구성되어 있습니다.  
 
- blynk_python_GPIO_v1.01  
VIRTUAL_READ 에서 **호출될 때마다 GPIO값을 터미널로 출력**하는 부분을 **변경되는 시점에서 1회 출력**으로 수정하였습니다.


