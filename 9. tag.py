
Git의 tag 및 명령어
# 특정 시점을 키워드로 저장 및 버전 정보를 붙일 때 사용

커밋에 tag 달기
- lightweight : 특정 커밋을 가리키는 용도
- annotated : 작성자 정보, 날짜, 메시지, GPg 서명 포함 

lightweight
1. git tag (태그명 - 버전 등)

2. git tag : 현재 존재하는 태그 확인

3. git show (태그명) : 원하는 태그의 내용 확인

4. git tag -d (태그명) : 특정 태그 삭제


annotated
1. git tag -a (태그명) : 마지막 커밋에 태그 작성 # 추가로 메시지 작성가능

2. git tag (태그명) -m '메시지'

3. git tag (태그명) (커밋 해시) -m (메시지) : 원하는 커밋에 태그추가 기능

필터링 및 체크아웃
1. git tag -l 'ex) v1.*' # 필터링

2. git checkout (태그명) # 체크아웃

동기화 및 원격의 tag
1. git push (원격이름) (태그명) # Github에서 확인가능

2. guit push --delete (원격이름) (태그명) : 특정 태그 원격 삭제

3. git push --tags : 로컬의 모든 태그 원격 업로드

