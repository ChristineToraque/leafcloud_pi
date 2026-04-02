1. do not staged or commit conductor
2. before performing a git operation such as push, commit either using gitbutler or git do the following:
    1. eval "$(ssh-agent -s)"
    2. ssh-add ~/.ssh/miming