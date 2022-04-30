git log 및 diff

git log 관련 명령어
1. git log -p : 커밋마다 변경사항 함께 보기

2. git log -(숫자) : 최근 숫자 만큼의 커밋만 보기

3. git log --start : 통계와 함께 보기
# --shortstat : 더 간략히 보기

4. git log --online : 커밋 내역 한줄로보기
# --pretty=online --abbreb-commit 의 줄임

5. git log -S (검색어) : 변경사항 내 단어 검색

6. git log --grep (검색어) : 커밋 메시지로 검색
'''
--since / --after : 명시 날짜 이후 커밋만 검색
--until, --before : 명시 날짜 이전 커밋만 조회
--author : 입력한 저자의 커밋만 보이기
--committer : 입력한 committer의 커밋만 보이기
--grep 커밋 메시지 안의 텍스트 검색
-S : 커밋 변경(추가 및 삭제) 내용 안의 텍스트를 검색
'''

7. git log / 자주 사용되는 그래프 로그 보기
--all : 모든 브랜치보기
--graph : 그래프 표현
--decorate : 브랜치, 태그 등 모든 레퍼런스 표시
'''
--decorate=no
--decorate=short : 기본
--decorate=full
'''

8. 포맷된 로그 보기
git log --graph --all --pretty=format: ''

''' 포매팅 옵션 - 단축키 등록하여 사용
%H : 커밋 해시
%h : 짧은 길이 커밋 해시
%T : 트리 해시
%t : 짧은 길이 트리 해시
%P : 부모 해시
%p : 짧은 길이 부모 해시
%an : 저자 이름
%ae : 저자 메일
%ad : 저자 시각 (형식주의)
%ar : 저자 상대적 시각
%cn : 커미터 이름
%ce : 커미터 메일
%cd : 커미터 시각
%cr : 커미터 상대적 시각
%s : 요약
'''

git diff 관련 명령어
1. git diff : 워킹 디렉토리의 변경사항 확인

2. git diff --nmae-only : 파일명만 확인

3. git diff --staged : 스테이지의 확인
# --cached와 같다

4. git diff (커밋1) (카밋2) : 커밋간 차이 확인
# 커밋해시 또는 HEAD번호로 가능
# 현재와 비교를 위해선 이전 커밋만 명시

5. git diff (브랜치1) (브랜치2) : 브랜치간 차이 확인

git blame 및 bisect

git blame 관련 명령어
1. git blame (파일명) : 파일의 부분별로 작성자 확인하기

2. git blame -L (시작줄) (끝줄, 또는 +줄수) (파일명)
# VS code Gitlens 확장 사용해보기

git bisect 관련 명령어
1. git bisect start : 이진 탐색 시작

2. git bisect bad : 오류발생 지점 표시

3. git checkout (해당 커밋 해시) : 의심 지정으로 이동

4. git bisect good : 오류 발생 안될 시 양호함 표시
# 원인 찾을 때 까지 반복적 시행 : git biseect good/bad

5. git bisect reset : 이진 탐색 종료