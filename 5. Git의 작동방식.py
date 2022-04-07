from cgitb import reset
from types import resolve_bases


Git의 작동원리

1. 파일의 삭제와 이동
git rm : 파일의 삭제가 working directory 안에서 존재
git mv (파일명) (바꿀파일명)
# git reset --hard로 복원
# git add . 를통해 stage에 올리지 않아도 자동으로 올라가는 명령어

git restore --stgaed (파일명) : staged 된 파일을 다시 working directiry에 돌려놓기
# git restore : working directoty 에서도 뺀다 (저장한 상태를 다시 되롤린다)

2. HEAD
해당 branch의 최신 커밋을 HEAD라도 부른다.
# checkout으로 되돌아간 bracnch의 커밋은 익명(커밋해시로 표기)의 branch로 보여짐
# git switch로 돌아간 원래 branch로 돌아가기
# 되돌아간 commit에서 새로운 branch 분기가능

git checkout - : 한 단계 되돌리기

git checkout HEAD^
# ^ , ~ 의 개수 만큼 전으로 이동
# HEAD^ ^^ ^^^ / HEAD~5

git checkout (commit hash) : 특정 커밋해시로 이동

HEAD를 사용하여 reset
git reset --hard HEAD()
git reset HEAD(특정단계) (옵션)

3. fetch and pull
fetch :원격의 최신 커밋을 로컬로 가쟈옴
pull : 원격의 최신 커밋을 로컬로 가쟈온 후 merge or rebase
# pull은 fetch를 포함하는 더 큰 개념

# 변화된 코드를 확인만 하고 싶을 때
로컬의 branch로 이동 후 / git fetch

원격의 branch로 이동 : git checkout (원격이름)/(branch)
# 반영사항 확인하기

다시 로컬의 branch로 이동 후 merge or pull

# 새로운 branch와 변경내역 확인만 하고 싶을 때
git fetch 후 변경사항 확인

git branch -a : 모든 브랜치확인 / 로컬, 원격

git checkout origin/new-branch
git switch -t origin/(브랜치명)
# 변경사항 확인 후 원격의 변경사항을 그대로 받아오겠다
