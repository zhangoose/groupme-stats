from fabric.api import *


env.use_ssh_config = True

def production():
    env.hosts = ['gmstats']

def deploy(branch="master"):
    with cd('~/groupme-stats/'):
        run('git checkout %s' % branch)
        run('git pull origin %s' % branch)
        run('sudo systemctl restart nginx')

