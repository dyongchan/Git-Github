from inspect import _SourceObjectType


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

