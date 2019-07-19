
# Blynk python GPIO예제 for 라즈베리파이  

**라즈베리파이**에서 사용되는 **Blynk python 버전**의 예제 소스입니다.  

https://github.com/vshymanskyy/blynk-library-python  

위 베타 버전 라이브러리를 사용한 예제 파일로 blynk.io에 업로드 된 python 라이브러리와 호환이 되지 않습니다.  
  

## blynk_python_GPIO.py  

https://github.com/vshymanskyy/blynk-library-python

위 라이브러리를 설치 후 파일을 실행해 주면 됩니다.  
``sudo puthon3 blynk_python_GPIO.py``

라즈베리파이에서 위 라이브러리 설치 시 아래 명령으로 실행해야 합니다.  
>(python3 사용)  
>``pip3 install blynk-library-python``  
>다운로드 실패 시 앞에 ``sudo`` 를 붙이거나, ``pip install blynk-library-python`` 등으로 시도  


타이머 라이브러리를 다운로드하는 스크립트를 실행해야 합니다.  
>``chmod +x start.sh``  
>``./start.sh``  


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
blynk.io에서 파이썬을 새로 지원하게 되면서 기존 사용되던 베타 라이브러리 대신 새로 추가된 공식 라이브러리를 사용하도록 변경되었습니다.  
  