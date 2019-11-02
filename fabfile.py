from fabric.api import env, local, cd, run, get
import datetime

env.hosts = ['cloud']


def deploy():
    local('git push')
    with cd('~/csi'):
        run('git pull')
        run('pipenv install')
        run('bower install')
        run('supervisorctl restart csi')


def get_assistants(year=datetime.datetime.today().year):
    get('~/csi/data/assistants_{}.csv'.format(year), 'data/')
