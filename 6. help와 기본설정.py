from distutils.command.config import config


git help and git config

1. git help
# git 사용 중 모르는 기능에 대하여 도움받을 수 있다.

2. git help -a 
# git의 모든 명령어 확인가능

3. git (명령어) -h 
# 해당 명령어의 설명 및 옵션 확인하기

4. 웹사이트에서 도움받기
git help (명령어)
git (명령어) --help
# 명령어의 설명과 옵션을 웹사이트에서 확인하기

5. git config(git의 설정값 확인)
# -global과 함께 사용시 전역으로 설정
# 특정 프로젝트 만의 user.name과 email 지정가능

현재의 모든 설정 확인하기
git config (global) --list

에디터에서 보기 (기본 : vi)
git config (global) -e

기본에디터 수정 (vs code로 수정)
git config --global core.editor "code --wait"
# 원하는 편집 프로그램 설정 시 .exe파일 로 경로연결한기
# --wait : 에디터에서 수정하는 동안 CLI 정지함

confi 속 유용한 설정 하기

git config --global core.autocrlf (윈도우 : true) / 맥 : input)
# 줄바꿈 호환 문제해결

git config pull.rebase false - 기본 : merge
git config pull.rebase true - 기본 : rebase
# pull의 기본적략 확인 후 대처

기본 브랜치명
git config --global init.defualtBranch main

push 시 로컬과 동일한 브랜치명 설정
git config --global push.default current

단축키 설정
git config --global alias.(단축키) "명령어"
