# Py-Ubuntu
saurjya@Saurjya:~/Desktop/Github$ git init
Reinitialized existing Git repository in /home/saurjya/Desktop/Github/.git/
saurjya@Saurjya:~/Desktop/Github$ git commit -m "First Commit"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'saurjya@Saurjya.(none)')
saurjya@Saurjya:~/Desktop/Github$ git config --global user.email "saurjya.sankar.chatterjee.cse.2020@tint.edu.in"
saurjya@Saurjya:~/Desktop/Github$ git config -- global user.name "Saurjy"
error: key does not contain a section: global
saurjya@Saurjya:~/Desktop/Github$ git config --global user.name "Saurjy"
saurjya@Saurjya:~/Desktop/Github$ git commit -m "First Commit"
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Add.py

nothing added to commit but untracked files present (use "git add" to track)
saurjya@Saurjya:~/Desktop/Github$ git add Add.py
saurjya@Saurjya:~/Desktop/Github$ git commit -m "First Commit"
[master (root-commit) 49d57f0] First Commit
 1 file changed, 4 insertions(+)
 create mode 100644 Add.py
saurjya@Saurjya:~/Desktop/Github$ git branch -M main
saurjya@Saurjya:~/Desktop/Github$ git remote add origin https://github.com/Saurjy/Py-Ubuntu.git
fatal: remote origin already exists.
saurjya@Saurjya:~/Desktop/Github$ git remote add origin https://github.com/Saurjy/Py-Ubuntu.gitgithub
fatal: remote origin already exists.
saurjya@Saurjya:~/Desktop/Github$ git remote add github https://github.com/Saurjy/Py-Ubuntu.git
fatal: remote github already exists.
saurjya@Saurjya:~/Desktop/Github$ git push
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main

saurjya@Saurjya:~/Desktop/Github$ git push --set-upstream origin main
Username for 'https://github.com': Saurjy
Password for 'https://Saurjy@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Saurjy/PY.git/'
saurjya@Saurjya:~/Desktop/Github$ git remote set-url --add --push origin https://github.com/Saurjy/Py-Ubuntu
saurjya@Saurjya:~/Desktop/Github$ git push
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main

saurjya@Saurjya:~/Desktop/Github$ git push --set-upstream origin main
Username for 'https://github.com': Saurjy
Password for 'https://Saurjy@github.com': 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 6 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 280 bytes | 280.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Saurjy/Py-Ubuntu
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
