from inspect import _SourceObjectType
from subprocess import STARTF_USESHOWWINDOW


commit의 다양한 사용 # 팀적으로 합의된 방식의 표현방식 사용이 중요하다.

1. commit massage convention

가장 많이 사용되는 commit message 작성 방식

# vi 에서 입력하여 사용
type : subject # 커밋 내용을 간햑히 설명함 / Gitmoji도 비슷한 방식으로 사용가능
#추가적인 설명이 필요 할 때, 아래 내용 추가
body (optional)
...
...
...

footer (optional) # 중요한 변경사항 및 특정이슈에 관한 해결 이슈일 때, 해당 이슈의 번호를 적음

'''
다양한 type의 사용
feat : 새로운 기능 추가
fix : 버그 수정
docs : 문서 수정
style : 공백, 세미콜론등의 스타일 수정
refactor : 코드 리팩토링
perf : 성능개선
test : 테스트 추가
chore : 빌드 과정 또는 보조 기능(문서 생성기능 등) 수정
'''

2. 내용 확인 및 hunk 별 스테이징
# 같은 파일에 담긴 변경사항을 분할해서 commit 가능

변경된 수정사항 확인 및 커밋
git add -p
# ? 입력 : 각각 옵션에 대한 섦여
# y , n : 각각의 hunk별로 부분적으로 add 할 것 인지에 대한 선택가능
# 파일 내에서도 부분적으로 add가 가능함 : git status로 확인가능

git commit -v 
# 상황에 맞추어 기본 에디터 설정 후 사용
# add로 추가된 모든 변경사항을 확인하고 commit 할 수 있음
# git diff --staged : 커밋에 해당될 변화학인 / commit -v 는 커밋까지 동시에 진행

3. stash
# 급한 변경사항 및 처리 발생 할 시 git에서 잠시 다른공간에 저장해주는 기능

git stash : 특정 공간으로 현재 작업 이동

git stash pop : 현재 내가 원하는 공간에 적용

git stash -p : 원하는 것만 stash 가능

git stash -m '(메세지)' : 어떤 부분이 

git stash apply : 치워둔 마지막 항목(번호 없을 시) 적용 # 번호로 항목 지정 가능

git stash drop : 치워둔 마지막 항목(번호 없을 시) 삭제 # 번호로 항목 지정 가능

git stash pop :  치워둔 마지막 항목(번호 없을 시) 적용 및 삭제 # apply + drop

git stash branch (브랜치명) : 새 브랜치를 생성하여 pop # 충돌사항 있을 경우 유용하다.

git stash clear : 치워둔 모든 항목들 비우기

4. commit 수정하기

git commit --amend : commit message 변경 # 다른 파일 변경 후 입력 시 commit에 포함시키기 가능

git commit --amend -a : add 명령어 없이 한번에 수행

git commit --amend -m : 메시지 한 줄로 변경

5. 과거 commit을 수정 삭제, 병합, 분할

git rebase -i # 대상의 바로 이전 커밋