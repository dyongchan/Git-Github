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

