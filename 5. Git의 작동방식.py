Git의 작동원리

1. 파일의 삭제와 이동
git rm : 파일의 삭제가 working directory 안에서 존재
git mv (파일명) (바꿀파일명)
# git reset --hard로 복원
# git add . 를통해 stage에 올리지 않아도 자동으로 올라가는 명령어

git restore --stgaed (파일명) : staged 된 파일을 다시 working directiry에 돌려놓기
# git restore : working directoty 에서도 뺀다 (저장한 상태를 다시 되롤린다)



