import email


{
"terminal.integrated.profiles.windows": {
    "GitBash": {
      "path": "C:\\Program Files\\Git\\bin\\bash.exe",
      "icon": "terminal-bash"
    },
    "PowerShell": {
      "source": "PowerShell",
      "icon": "terminal-powershell"
    },
    "Command Prompt": {
      "path": "C:\\WINDOWS\\System32\\cmd.exe",
      "icon": "terminal-cmd"
    }
  },
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "workbench.colorTheme": "Beard Theme Monokai Stone",
  "workbench.iconTheme": "material-icon-theme"
}
# VS Code settings.json file : Git Bash의 기본 터미널 적용 명령어
# Git Bash를 이용하여 Linux체제의 명령어도 실행가능

1. 설치 및 버전확인, 기초 폴더 생성
git --vsesion : git의 설치여부를 알 수 있으며 버전확인 가능
git init : 로컬 작업폴더 내의 git 관리 및 정보폴더 (.git) 생성

2. 협업 시 윈도우와 맥의 엔터 방식 차이에 의한 오류 방지
git config --global core.autocrlf input

3. 사용자 이름 및 이메일 주소 설정 브랜치명 변경
git config --global user.name "(본인 이름)"
git config --global user.email "(본인 이메일)"
# 이름 및 주소 확인
git config --global (user.name)
git config --global (user.email)
# 기본 브랜치명 변경
git config --global init.defaultBranch (bracnch name)