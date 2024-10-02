import os
import git

repo_path = "/Alliyah101014/IOSXE/"

repo = git.Repo(repo_path)

repo.git.pull()

os.system('cp /Alliyah101014/IOSXE/running-config.py /Alliyah101014/IOSXE/')
repo.index.add(['running-config.py'])
repo.index.commit('Updated running config')

repo.git.push()
