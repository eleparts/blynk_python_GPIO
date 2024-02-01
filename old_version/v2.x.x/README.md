
# Blynk python GPIO예제 for 라즈베리파이

**라즈베리파이**에서 사용되는 **Blynk python 버전**의 예제 소스입니다.  
Blynk python 구성품 키트 정보는 아래 페이지를 참고 해 주세요  

라즈베리파이 IOT 키트 V2.0  
https://www.eleparts.co.kr/EPXMVGDB  

**위 IOT 키트와 관련된 전체 예제는 아래 페이지에서 확인 가능합니다.**  
https://github.com/eleparts/iotkit  


## blynk_python_GPIO.py  

https://github.com/blynkkk/lib-python  

위 라이브러리를 설치 후 파일을 실행해 주면 됩니다.  
``sudo puthon3 blynk_python_GPIO.py``  

라즈베리파이에서 위 라이브러리 설치 시 아래 명령으로 실행해야 합니다.  
>(python3 사용)  
>``pip3 install blynklib``  
>다운로드 실패 시 앞에 ``sudo``를 붙여 실행해 줍니다.  


타이머 라이브러리를 다운로드하는 스크립트를 실행해야 합니다.  
>``chmod +x start.sh``  
>``./start.sh``  


## blynk_GPIO.fzz
fritzing 확장자 파일입니다.  
fritzing이 설치되어 있다면 열어보실 수 있습니다.  
http://fritzing.org/home/  


## blynk_GPIO.png
회로 구성 이미지 파일입니다.  
![blynk_GPIO](https://raw.githubusercontent.com/eleparts/blynk_python_GPIO/master/blynk_GPIO.png)  
> LED 저항 : 100 ~ 220옴  
> SW 저항 : 1K ~ 10K옴 (풀다운 저항)  

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

- blynk_python_GPIO_v1.10  
blynk.set_user_task 함수가 삭제되고 타이머 라이브러리가 추가되었습니다.  
타이머 라이브러리를 다운로드 하기 위하여 start.sh 스크립트가 추가되었습니다.  

- blynk_python_GPIO_v2.0.0  
blynk가 공식 python 예제를 지원하게 되면서 기존 베타 버전 라이브러리와 다른 라이브러리를 사용하게 되었습니다.  
이에 따라 해당 공식 라이브러리를 사용하도록 수정되었습니다.  
  
## old_version  

Blynk python GPIO 1.x.x (구버전) 파일이 정리되어 있습니다.

Blynk로 라즈베리파이 GPIO원격 제어하기(Python 버전)  
https://blog.naver.com/elepartsblog/221343615682  

위 블로그 예제와 호환됩니다.  
  