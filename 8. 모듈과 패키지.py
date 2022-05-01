모듈(module) : 미리 만들어 놓은.py file을 불러와서 사용하는 구조 (함수, 변수, 클래스)
# import : 가져온다 / 같은경로(같은폴더)내에 존재 시 바로 사용가능

1. 함수 가져와서 적용

다른 파일 속 함수
'''
# mod1.py
def add(a,b):
    return a + b
'''

from tkinter import E
import mod1
print(mod1.add(1,2)) # 3 출력

2. 여러 함수가 포함 될 시

다른 파일 속 함수
'''
# mod1.py
def add(a,b):
    return a + b
def aasdasdasd(a,b):
    return a + b
'''

from mod1 import add # mod1.py 속 add의 함수만 사용
print(add(1,2)) # 3 출력

3. print가 포함된 mod1.py import

다른 파일 속 함수
'''
# mod1.py
def add(a,b):
    return a + b

def sub(a,b):
    retirn a - b
'''
if __name__ == "__main__" 
# name = 가져올 함수가 존재하는 파일
# main = 함수가 실행될 현재 파일의 이름
    print(add(1,4))
    print(add(4,2))
# name과 main과 일치할 때 만 print를 실행하라는 조건문

4. 경로가 다를 시(ex-불러오는 파일이 다른 폴더에 있는경우) 사용하는 명령어
sys.path.append("경로")

ex)
import sys
sys.path.append("C:\\jocoding\\subFolder") # 경로를 작성해야 다른 경로 속 파일 가져오기 가능
import mod1
print*mod1.add(3,4)

패키지(package) : 모듈 여러 개를 모아놓은 구조

가상의 game 패키지 예시)
패키지 기본 구조 : 폴더 속 init 생성 / # 3.3 version 이후로는 안써도 되긴 함
gmae/
    __init__.py # 패키지의 표현 파이썬 파일 : 패키지관련 설정하는 곳
    sound/
        __init__.py
        echo.py
    graphic/
        __init__.py
        render.py

# echo.py / game 폴더 속 sound 폴더 속 파일
def echo_test():
    print("echo")

# render.py / 
def rrender_test():
    print('render')

패키지 안의 함수 실행하기
1. import game.sound.echo # 폴더 속 파일을 불러오기 위해 하나씩 들어가야함
game.sound.echo.echo_test()

2. from game.sound import echo # game 패키지 속 echo의 모듈만 불러오겠다.
echo.echo_test()

3. from game.sound.echo import echo_test # game 패키지 속 폴더 안에 있는 echo_test라는 함수만 불러오겠다.
echo_test()

4. from game.sound.echo import echo_test as e # echo_test를 e라고 사용하겠다.
e()

5. from game.sound import * # game.sound 속 폴더의 모든 파일을 불러와라
echo.echo_test()

# init.py
C:/jocoding/gmae/sound/__init__.py
__all__ = ['echo'] # init.p 파일에 기록할 시 가져올 수 있음

# echo2 라는 파일을 추가적으로 생성했을 시 init.py 파일에서 추가해줘야 *(all) 로 불러올 수 있다.
__all__ = ['echo', 'echo2', 'aaaa'...] # 계속적으로 추가할 수 있음

