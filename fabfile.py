from fabric.api import env, local, prefix, cd, run, get
import datetime

env.hosts = ["production"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/csi/bin/activate"):
        with cd("~/csi"):
            run("git pull")
            run("pip install -r requirements.txt")
            run("bower install")
            run("supctl restart csi")


def get_assistants(year=datetime.datetime.today().year):
    get("~/csi/data/assistants_{}.csv".format(year), "data/")
