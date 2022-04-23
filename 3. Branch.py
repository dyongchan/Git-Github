from email.headerregistry import ContentTransferEncodingHeader
from sre_constants import BRANCH


BRANCH : 프로젝트를 여러 저장소를 통해서 관리하는 시스템
# 여러 작업이 각각 독립적으로 진행될 때 사용한다.
# 협업에서 매우 중요하고 유용하게 사용됨.

branch 생성 관련 git bash 명령어

1. branch 생성 : git branch (브랜치명)

2. branch 목록 확인 : git branch
- 맨앞 * 붙은 branch가 현재 속한 branch

3. 해당 branch로 이동 : git switch (브랜치명) 

4. branch 생성과 동시에 이동 : git switch -c (브랜치명)

5. branch 삭제 : git branch -d (삭제할 브랜치명)

6. branch 강제 삭제 : git branch -D (삭제할 브랜치명) # 다른 브랜치에 적용되지 않는 내용의 커밋 존재 시

7. branch 이름 변경 : git brabch -m (바꾸는 브랜치명) (바꿀 브랜치명)

8. branch 내역보기 : git log - 해당 브랜치의 내역만 볼 수 있다.

9. 여러 branch 내역 편리하게 보기 : git log --decorate --oneline --graph

branch 병합 관련 git bash 명령어
Merge  vs Rebase
# Merge : 브랜치의 사용 내역을 남길 필요가 있다.
# Rebase : 브랜치의 내역을 메인 브랜치에 이어 붙이며 히스토리를 깔끔하게 만든다.
# 이미 팀원들과 공유된 commit에 관해서는 rebase를 사용하지 않는 것이 좋다.
# 협업과 진행하는 프로젝트에 따라 방식이 다르다.

1. merge 관련 명령어
# 병합하기 위한 main 브랜치로 이동 후 진행

git merge (브랜치명) : main 브랜치와 끝이 이어짐으로 병합되는 브랜치의 커밋내용이 main에 반영
# git branch -d (병합된 브랜치명)을 통하여 사용된 브랜치 제거

2. rebase 관련 명령어
# 병합할 브랜치로 이동 후 진행 (main으로 가는 것이 아님)

git rebase (병합할 브랜치명)
# 병합될 브랜치가 main 브랜치와 이어지게됨
# 추가적으로 main 브랜치를 병합된 브랜치의 끝으로 merge를 통해 옮겨야 함. (자동적으로 반영되지 않음)

branch 병합 시 충돌 관련 명령어
merge 충돌 해결
충돌 발생 시 작성자에게 conflict를 해결하는 선택지를 줌
# commit 한번에 해결 가능

1. git merge --abort : merge 초기화 

2. conflict 해결 후 git add . , git commit 을 통하여 병합 완료

rebase 충돌 해결 

1. git rebase --abort : rebase 초기화

2. conflict 해결 가능 시 git add . 후 git rebase --continue 
# merge와 다르게 여러번의 해결과정이 나올 수 있기 떄문에 continue 사용
# main branch의 해결과정을 선택하면 추가적인 commit은 하지 않게 됨 = rebase의 과정 불필요 : 커밋 1회 감소
