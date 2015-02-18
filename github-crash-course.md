GitHub Crash Course
===================

To add to this repository, you will need to clone this GitHub repository to your local computer. To do that, open up your command line, then navigate to a directory where you want to save this repository's files on your local machine.  Then, run:

`git clone https://github.com/PyLadiesTC/Dcubed-installfest-2015.git`

This will download all of the files to your computer so you can work on and edit them locally using your favorite text editor.

You can edit this README.md file with any information we need to share for the Installfest.  You can use the following markdown syntax to style this doc: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

When you are done making changes, you first need to:
1. 'commit' these changes to the git repository on your local computer, then
2. 'push' a copy of these changes to the remote repository on GitHub...

## Commit changes locally
First, add any files you've changed to your local git repository so they're being tracked:

`git add --all`

Then commit the changes to your local repository, along with a brief message of what you've changed:

`git commit -m "This is a description of the changes I made"`

At this point, you've still only made changes on your *local* computer.  None of these will be available publicly, and the changes are not yet pushed to the public GitHub repository.
Note: People sometimes assume that GitHub repositories do some magic "auto-syncing" from your local computer into GitHub.  This is false!  Files you change and commit on you local computer will *not* automatically make their way up into GitHub until you do the following...

## Push changes to remote repository on GitHub
Now, push the changes from your local computer into GitHub so they're available to everyone publicly on the PyLadies/Dcubed-installfest-2015 repository:

`git push origin master`
