Git과 Github

1. Git에 원격 저장소 사용
git remote add origin(원격 저장소 이름) (원격 저장소 주소) : git에 원격 저장소 추가 
# Github와 같은 서비스가 될 수 있음
# 보통 이름은 origin으로 많이 사용함

git branch -M main : Github 권장 브랜치명 사용 (많이 사용하는 이름)

git push -u origin main : 커밋내역을 업로드 할 원격 저장소, 브랜치 설정
# 원격 저장소의 어느 브랜치에 커밋내역들을 업로드 할 것 인가
# 저장소 및 브랜치 설정 이후에는 git push로 커밋 내역 업로드 가능

2. Github에서 타인의 projects 다운 및 설치

Download ZIP : 협업을 위해서는 사용 못함 # .git 파일이 없음

1. 원하는 폴더 접속 후 Git Bash here 실행

2. 다운로드 받을 양식 선택후(HTTPS, SSH CLI...) repository의 clone 주소 복사

3. git clone (해당주소) 입력
# .git 파일까지 복사가능
# git log 사용

3. Push 와 Pull의 사용

git push : 원격으로 커밋 밀어올리기

git pull : 원격 저장소의 커밋내역 당겨오기

원격 저장소의 commit으로 로컬에서 push가 불가능할 때 push의 방법 2가지
# 로컬은 원격보다 뒤쳐지므로 pull을 먼저 진행해야 한다.

1. git pull --no-rebase : merge 방식
# 로컬과 원격이 분기되어 합쳐지는 방식 (로컬과 원격의 시간선을 한 곳으로 모아준다)

2. git pull --rebase : rebase 방식
# 원격의 시간에 맞추어 원격의 커밋을 먼저 수행한 후 로컬의 커밋을 이어붙인다

1,2 모두 수행 후 git push 해주기

원격 저장소에 저장된 repository 속 커밋의 충돌이 발생할 경우

git pull --no-rebase
# 협의를 통하여 commit이 합쳐지는 구조이기 때문에 한개의 commit 생성

git pull --rebase
# rebase는 어떤 충돌사항을 선택하냐에 따라 추가되는 commit의 수가 달라 질 수 있다
# pull 상황에서의 rebase는 협업시 사용해도 괜찮음

로컬의 내역을 강제로 push
# 원격상의 내용이 잘못되어 로컬의 내용으로 강제로 맞출 때 사용

git push --force # 협업 시 미리 합의 후 사용해야함