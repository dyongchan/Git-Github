
branch의 활용 및 심화 내용
# 각각의 branch 속 잔가지들을 다양하게 이어붙이는 실습

1. git cherry-pick (체리의 해시): 다른 브랜치의 원하는 커밋 가져오기

2. git rebase --onto (도착 브랜치) (출발 브랜치) (이동할 브랜치)
# main에서 파생된 브랜치 속 또다시 파생된 브랜치를 main에 붙일 수 있음 - 실습 해보기

- gt rebase --onto 되돌리기
1. 모든 적용된 브랜치를 하나하나 reset 진행
# main 브랜치 : 붙여진 브랜치 이전으로 reset --hard 명령어
# 붙여진 브랜치 : 옮겨지기 이전으로 reset --hard 명령어

2. 다시 옮겨 붙이기
# main에 붙여진 브랜치를 다시 rebase --onto로 기존 브랜치로 붙이기