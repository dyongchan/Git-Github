commit and workspace

git add (파일명) : stage로 특정 파일 하나 보내기
# 각각의 파일을 각각 다른 버전에 넣고 싶을 때 사용함

git add . : 모든 폴더의 파일 stage로 보내기
# 일반적으로 모든 작업을 마치고 포함돤 모든 변화들을 넣을 때사용하는 명령어

git commit : 변화들을 저장하기 위한 명령어

# add와 commit을 한꺼번에 시행
git commit -m "(메시지)"  # 새로추가된 Utrcaked File이 없을 때만 가능

'''
작업
1. 입력시작 : i - 텍스트 입력모드
2. 입력종료 : ESC - 명령어 입력모드
3. 저장없이 종료 : :q
4. 저장없이 강제종료 : :q! - 입력한 것이 있을 때 사용
5. 저장하고 종료 : :wq - 입력한 것이 있을 때 사용
6. 위로 스크롤 : k - git log등에서 내역일 길 때 사용
7. 아래로 스크롤 : j git log등에서 내역일 길 때 사용
'''

git commit -m "FIRST COMMIT" : 메시지 함께 작성

git log : commit의 일련번호 및 commit의 name 확인 가능

git diff : 변경사항을 구체적으로 알려주는 명령어

commit을 과거로 되돌리기 # .git file 속에는 과거 commit의 히스토리가 담겨있다.

1. reset # 특정 지점으로 되돌린 후 히스토리 삭제
git reset --hard (돌아가고싶은 commit hash) : 특정 commit 지점으로 돌아감 
# .git 폴더 백업 필수

git reset --hard : 마지막 commit으로 돌아가기

2. revert # 특정 commit에서 다른 특정 지점으로 되돌리며 되돌리는 히스토리도 남김
# 협업시 필수로 사용해야함 (히스토리가 남으며 협업 시 유용)

git revert (돌이키고싶은 commit hash)

돌이키고싶은 commit에서 특정 지점으로 되돌릴 때 다른 commit과 충돌이 발생할 수 있다. # REVERTING 오류

REVERTING 오류 발생 시
hint 라는 문구와 함께 충돌 내역이 발생 함

git rm (파일명) : 파일 삭제

git revert --continue : revert 지속

git revert --no-commit : revert와 함께 다른 수정사항도 추가 후 변경자가 commit하겠다는 명령어
