
# Blynk python GPIO예제 for 라즈베리파이

**라즈베리파이**에서 사용되는 **Blynk python 버전**의 예제 소스입니다.  
Blynk python 구성품 키트 정보는 아래 페이지를 참고 해 주세요  

라즈베리파이 IOT 키트 V2.0  
https://www.eleparts.co.kr/EPXMVGDB  

**위 IOT 키트와 관련된 전체 예제는 아래 페이지에서 확인 가능합니다.**  
https://github.com/eleparts/iotkit  


## 사용 전 필수 라이브러리  
  
[**blynk - Python 라이브러리**](https://github.com/vshymanskyy/blynk-library-python)를 설치 후 파일을 실행해 주면 됩니다.  
라즈베리파이에서 아래 명령을 차례대로 입력해 주시면 라이브러리를 간단하게 설치할 수 있습니다.  

```bash
# 복제된 lynk-library-python 라이브러리
git clone https://github.com/eleparts/blynk-library-python
cd blynk-library-python
sudo python setup.py install
```
  
> - 라즈베리파이5를 사용한다면 추가로 pi5용 lgpio 라이브러리를 설치해 줍니다.  
> ```bash
> # 반드시 라즈베리파이 5 사용시에만 설치
> pip install --break-system-packages rpi-lgpio
> ```
  
## blynk_python_GPIO.py  

  예제는 아래 명령어로 실행할 수 있습니다.  
  
``python blynk_python_GPIO.py``  

## Blynk 위젯 배치  

- PI - GPIO 디바이스 설정 

|가상핀|가상핀 설정|위젯|모드|
|:----:|:-:|:-:| :-:|
|V0 | integer 0/1 | Button | MODE : SWITCH | 
|V1 | integer 0/1 | Button | MODE : SWITCH |  
|V2 | string| Value Display | |  
|V4 | integer 0/255|LED | |  
  
## blynk_GPIO.fzz  
fritzing 확장자 파일입니다.  
fritzing이 설치되어 있다면 열어보실 수 있습니다.  
http://fritzing.org/home/  


## blynk_GPIO.png  
회로 구성 이미지 파일입니다.  
![blynk_GPIO](https://raw.githubusercontent.com/eleparts/blynk_python_GPIO/master/blynk_GPIO.png)  
> LED 저항 : 100 ~ 220옴  
> SW 저항 : 1K ~ 10K옴 (풀다운 저항)  

예제코드 동작 전에 해당 회로를 동일하게 구성해 주셔야 합니다.  

## 소스코드 폴더  

**소스 코드**가 버전별로  **.py** 파일로 저장되어 있습니다.  


### 버전별 변경 내역  

- blynk_python_GPIO_v3.0.0  
blynk 2.0 대응 라이브러리 사용을 위해 업데이트 된 기존 저장소를 이용합니다.  
pip로 설치 시 구버전이 설치되어(0.2.6) 해당 저장소를 직접 받아 설치해야 합니다.(1.0.0)  

- blynk_python_GPIO_v3.1.0  
Vpin 순서 변경, 안내 추가  
  
## old_version  

구버전(1.x.x / 2.x.x) 파일이 정리되어 있습니다.  