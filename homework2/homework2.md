## Task: 1. Create merge conflict and resolve it

### Main steps to reproduce merge conflict:

1.  nvim file_with_merge_conflict.txt
2.  git checkout homework2
3.  nvim file_with_merge_conflict.txt 
4.  git add .
5.  git commit -m "Edited 'file_with_merge_conflict.txt' on homework2 branch"
6.  git checkout main
7.  nvim file_with_merge_conflict.txt
8.  git add .
9.  git commit -m "Edited 'file_with_merge_conflict.txt' on main branch"
10.  git merge homework2
11.  nvim file_with_merge_conflict.txt 
12.  git add .
13.  git commit -m "Fixed merge conflict"
14.  git push --all

### Workflow from terminal
```shell
➜  homework2 git:(main) ls
file_with_merge_conflict.txt
➜  homework2 git:(main) nvim file_with_merge_conflict.txt 
➜  homework2 git:(main) git checkout homework2 
Switched to branch 'homework2'
➜  homework2 git:(homework2) ls
file_with_merge_conflict.txt
➜  homework2 git:(homework2) nvim file_with_merge_conflict.txt 
➜  homework2 git:(homework2) ✗ git add .
➜  homework2 git:(homework2) ✗ git commit -m "Edited 'file_with_merge_conflict.txt' on homework2 branch"
[homework2 75a62bf] Edited 'file_with_merge_conflict.txt' on homework2 branch
 1 file changed, 1 insertion(+), 1 deletion(-)
➜  homework2 git:(homework2) git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
➜  homework2 git:(main) ls
file_with_merge_conflict.txt
➜  homework2 git:(main) nvim file_with_merge_conflict.txt 
➜  homework2 git:(main) ✗ git add .
➜  homework2 git:(main) ✗ git commit -m "Edited 'file_with_merge_conflict.txt' on main branch"
[main 9c724c7] Edited 'file_with_merge_conflict.txt' on main branch
 1 file changed, 1 insertion(+), 1 deletion(-)
➜  homework2 git:(main) git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
➜  homework2 git:(main) git merge homework2
Auto-merging homework2/file_with_merge_conflict.txt
CONFLICT (content): Merge conflict in homework2/file_with_merge_conflict.txt
Automatic merge failed; fix conflicts and then commit the result.
➜  homework2 git:(main) ✗ nvim file_with_merge_conflict.txt 
➜  homework2 git:(main) ✗ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   file_with_merge_conflict.txt

no changes added to commit (use "git add" and/or "git commit -a")
➜  homework2 git:(main) ✗ git add .
➜  homework2 git:(main) ✗ git commit -m "Fixed merge conflict"
[main 06345ab] Fixed merge conflict
➜  homework2 git:(main) git status
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
➜  homework2 git:(main) git push --all
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 4 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (16/16), 1.32 KiB | 192.00 KiB/s, done.
Total 16 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), done.
To github.com:201dreamers/gl-base-camp.git
   b95f6d8..06345ab  main -> main
 * [new branch]      homework2 -> homework2
```