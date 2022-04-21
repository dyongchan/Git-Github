
from distutils.command.clean import clean


취소와 되돌리는 여러 명령어

1. git clean
# git clean -df 자주사용함

'''
git claen + @
-n : 삭제될 파일들 보여주기
-i : interactive mode 시작
-d : 폴더 포함
-f : 강제로 지우기
-x : .gitignore에 등록된 파일도 삭제
'''

2. git restore (파일명)
# working directory 속 특정 파일 복구

- git restore . : 모든 파일 복구

- git restore --staged (파일명)
# 변경상태를 stage에서 working directory로 되돌리기

- git restore --source=(head or commit hasg) 파일명
# 파일을 특정 commit 상태로 되돌리기

3. git reflog # reset으로 사라진 commit을 복구할 수 있음
- 해당 프로젝트가 위치한 commit이 바뀔 때 마다 기록되는 내역 호출
- 기록을 사용하여 reset전의 시점으로 프로젝트 복구가능