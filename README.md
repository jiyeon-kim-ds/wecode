# 기초 git 명령어
1. `git add` : git에서 commit할 파일들을 추가하는 명령어로 `git add .`를 하면 폴더 내 모든 파일(`.gitignore`있는 파일 제외)을 추가한다.
2. `git commit` : `git add`로 추가한 파일들을 저장소에 올리겠다고 선언하는 명령어이다. `git commit`만으로는 github과 같은 저장소에 올라가지 않는다. `git commit -m ' '`로 commit 메세지를 남길 수 있다.
3. `git push` : `git commit`한 것들을 실제로 저장소에 올리는(push) 하는 명령어이다.
4. `git log` : commit 내역들을 확인할 수 있는 명령어이다.
5. `git branch branch_name` : 새로운 브랜치를 만들 수 있는 명렁어이다.
6. `git checkout branch_name` : 해당 브랜치로 이동할 수 있는 명령어이다.