import subprocess

commitmessage = input("Enter commit message : ")
branchname = subprocess.run(['git', 'branch', '--show-current'])
print(branchname)

addcmd = ['git', 'add', '.']
commitcmd = ['git', 'commit', '-m', commitmessage]
pushcmd = ['git', 'push', 'origin', branchname]

subprocess.run(addcmd)
subprocess.run(commitcmd)
subprocess.run(pushcmd)
