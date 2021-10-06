### Git 명령어 정리

1. 로컬에서 원격 브랜치를 삭제하고 싶을때
~~~
git push -d origin <branch-name>
~~~

2. gitignore 설정
- 최상위 디렉토리에서 .gitignore 파일을 생성한다.
- 원하는 파일 및 디렉토리를 설정하여 제외시킨다.
- 이때, https://www.toptal.com/developers/gitignore 와 같은 사이트를 참고하면 쉽다.
- 이미 remote에 올라간 파일에 대해서 gitignore을 소급 적용하고 싶을때는 아래와 같은 코드를 실행한다.
~~~
git rm -r --cached .
git add .
commit 메세지 작성 후 push
~~~