from fabric.api import env, local, cd, run, get, prefix
import datetime

env.hosts = ['cloud']


def deploy():
    local('git push')
    with prefix('source ~/.virtualenvs/bin/activate'):
        with cd('~/code/csi'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('bower install')
            run('supervisorctl restart csi')


def get_assistants(year=datetime.datetime.today().year):
    get('~/csi/data/assistants_{}.csv'.format(year), 'data/')
