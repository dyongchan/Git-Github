
branch의 활용 및 심화 내용
# 각각의 branch 속 잔가지들을 다양하게 이어붙이는 실습

1. git cherry-pick (체리의 해시): 다른 브랜치의 원하는 커밋 가져오기

2. git rebase --onto (도착 브랜치) (출발 브랜치) (이동할 브랜치)
# main에서 파생된 브랜치 속 또다시 파생된 브랜치를 main에 붙일 수 있음 - 실습 해보기

gt rebase --onto 되돌리기
- 모든 적용된 브랜치를 하나하나 reset 진행
# main 브랜치 : 붙여진 브랜치 이전으로 reset --hard 명령어
# 붙여진 브랜치 : 옮겨지기 이전으로 reset --hard 명령어

- 다시 옮겨 붙이기
# main에 붙여진 브랜치를 다시 rebase --onto로 기존 브랜치로 붙이기

3. git merge --squash (대상 브랜치) : 다른 커밋들을 하나로 묶어 가져오기
# 변경사항들 on stage / 메시지 입력
# 일반 merge와의 차이 : 브랜치의 마디들을 복사 후 한마디로 모아 해당 브랜치에 붙인다

'''
협업을 위해 많이 사용되는 브랜치들
main : 제품 출시/배포
develop : 다음 출시/배포를 위한 개발
release : 출시/배포 전 테승트 진행(QA)
featur : 기능 개발
hotfix : 긴급한 버그 수정
'''