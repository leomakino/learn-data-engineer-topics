# Introduction
Git is a software for tracking changes in any set of files. In other words, it’s a version control software.

It is usually used for coordinating work among programmers collaboratively during software development.

# Git repositories
A Git repository (or repo for short) contains all of the project files and the entire revision history. You’ll take an ordinary folder of files (such as a website’s root folder), and tell Git to make it a repository. This creates a .git subfolder, which contains all of the Git metadata for tracking changes.

# Stage & Commit Files
How do we tell Git to record our changes?
> Each recorded change to a file or set of files is called a commit.

Before we make a commit, we must tell Git what files we want to commit. This is called staging and uses the add command.

# Remote Repositories
Storing a copy of your Git repo with an online host gives you a centrally located place where you can upload your changes and download changes from others, letting you collaborate more easily with other developers.

After you have a remote repository set up, you upload (push) your files and revision history to it. After someone else makes changes to a remote repo, you can download (pull) their changes into your local repo.
![](https://www.nobledesktop.com/image/blog/git-distributed-workflow-diagram.png)

# Branches & Merging
Git lets you branch out from the original code base. This lets you more easily work with other developers, and gives you a lot of flexibility in your workflow.

Let’s say you need to work on a new feature for a website. You create a new branch and start working.
You haven’t finished your new feature, but you get a request to make a rush change that needs to go live on the site today. You switch back to the master branch, make the change, and push it live. Then you can switch back to your new feature branch and finish your work. 

When you merge two branches (or merge a local and remote branch) you can sometimes get into a conflict. You and another developer unknowingly both work on the same part of a file. The other developer pushes their changes to the remote repo.When you then pull them to your local repo you’ll get a merge conflict. Git has a way to handle conflicts, so you can see both sets of changes and decide which you want to keep.

# Pull Request
Pull requests are a way to discuss changes before merging them into your codebase.

A developer makes changes on a new branch and would like to merge that branch into the master. They can create a pull request to notify you to review their code.
You can discuss the changes, and decide if you want to merge it or not.

# Git commands examples
| **Working with local repositories** |      |                                                            |
|---------------------------------|------|------------------------------------------------------------|
| Git command                     | Flag | Description                                                |
| git init                        |      | It turns a directory into an empty Git repository          |
| git add                         |      | Adds files to the staging area                             |
| git status                      |      | shows the file is in the staging area, but not committed   |
| git commit                      | -m   | Record the changes made to the files to a local repository |
| git branch                      | -a   | List all remote or local branches                          |
| git branch                      | -d   | delete a branch                                            |
| git checkout                    |      | to switch branches                                         |
| git checkout                    | -b   | Checkout and create a new branch with that name            |
| git merge                       |      | Merge changes into current branch                          |
| git branch                      |      | lista branches                                             |

| **Working with remote repositories** | |                                 |
|--------------------------------------|------|---------------------------------------|
| Git command                          | Flag | Description                           |
| git clone                            |      | copy of an existing remote repo       |
| git pull                             |      | Get the latest version of a repo      |
| git push                             |      | Send local commits to the remote repo |


| **Advanced git commands** |  |                                                                     |
|---------------------------|------------|--------------------------------------------------------------------------|
| Git command               | Flag       | Description                                                              |
| git stash                 |            | Save changes made when they’re not in a state to commit                  |
| git log                   |            | Show the chronological commit history                                    |
| git rm                    |            | Removes files or directories from the staging area                       |
| git reset                 | –soft      | volta para a versão anterior e com as modificações atuais não commitadas |
| git reset                 | –mixed     |                                                                          |
| git reset                 | –hard      | Ignora tudo que existia nas outras versões mais atuais                   |
| git diff                  |            | See the unstaged changes on the current branch                           |
| git diff                  | –name-only | Mostra o nome do arquivo modificado                                      |
| git revert                |            | Desalterar mudanças do último commit                                     |


## Other topics
Ignorar/Ocultar determinados arquivos -> .gitignore

Fork -> Para contribuir como terceiro em um projeto

# References
[What is Git and Why should you use it?](https://www.nobledesktop.com/learn/git/what-is-git)

