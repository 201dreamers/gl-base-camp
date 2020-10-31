### 1. Move file from untracked to commit and the whole way back. Note: Do not skip any stage.

```shell
➜  gl-base-camp git:(main) ls
➜  gl-base-camp git:(main) mkdir homework1
➜  gl-base-camp git:(main) cd homework1
➜  homework1 git:(main) touch some-file.txt
➜  homework1 git:(main) ✗ ls
some-file.txt
➜  homework1 git:(main) ✗ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	./

nothing added to commit but untracked files present (use "git add" to track)
➜  homework1 git:(main) ✗ git add .
➜  homework1 git:(main) ✗ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   some-file.txt

➜  homework1 git:(main) ✗ git restore --staged some-file.txt
➜  homework1 git:(main) ✗ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	./

nothing added to commit but untracked files present (use "git add" to track)
➜  homework1 git:(main) ✗ ls
some-file.txt
```

### 2. Create a branch from initial commit of master branch

```shell
➜  homework1 git:(main) ✗ git branch hw1-task2-br       
➜  homework1 git:(main) ✗ git checkout hw1-task2-br 
Switched to branch 'hw1-task2-br'
➜  homework1 git:(hw1-task2-br) ✗ 
```

### 3. Remove file from git repository only(leave it on file system)

```shell
➜  homework1 git:(hw1-task2-br) ✗ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
➜  homework1 git:(main) ✗ ls
some-file.txt
➜  homework1 git:(main) ✗ git add .
➜  homework1 git:(main) ✗ git commit -m "Commited some-file.txt"
[main b95f6d8] Commited some-file.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homework1/some-file.txt
➜  homework1 git:(main) ls
some-file.txt
➜  homework1 git:(main) git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
➜  homework1 git:(main) git rm --cached some-file.txt
rm 'homework1/some-file.txt'
➜  homework1 git:(main) ✗ ls
some-file.txt
➜  homework1 git:(main) ✗ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    deleted:    some-file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    ./

➜  homework1 git:(main) ✗ git add .
➜  homework1 git:(main) git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
➜  homework1 git:(main) git push --all
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 334 bytes | 111.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/201dreamers/gl-base-camp
   c108f4b..b95f6d8  main -> main
 * [new branch]      hw1-task2-br -> hw1-task2-br

```