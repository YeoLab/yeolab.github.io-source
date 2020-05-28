from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

def collectstatic():
    if os.path.isdir(DEPLOY_PATH):
        # import sys
        # sys.stderr.write('copying files from \t {}'.format(os.path.getwd()))
        local('mkdir -p {deploy_path}/css/ {deploy_path}/js/ {deploy_path}/fonts/ {deploy_path}/images/ {deploy_path}/singarna-symposium-2016'.format(**env))
        local('mkdir -p {deploy_path}/css/ {deploy_path}/js/ {deploy_path}/fonts/ {deploy_path}/images/ {deploy_path}/TSCC_Onboarding'.format(**env))
        local('cp -rf twenty-pelican-html5up/static/css/* {deploy_path}/css/'.format(**env))
        local('cp -rf twenty-pelican-html5up/static/js/* {deploy_path}/js/'.format(**env))
        local('cp -rf twenty-pelican-html5up/static/fonts/* {deploy_path}/fonts/'.format(**env))
        local('cp -rf twenty-pelican-html5up/static/images/* {deploy_path}/images/'.format(**env))
        local('cp -rf extras/* {deploy_path}/'.format(**env))
        local('cp -rf content/papers/* {deploy_path}/papers/'.format(**env))
        local('cp -rf content/pages/singarna-symposium-2016/* {deploy_path}/TSCC_Onboarding/'.format(**env))
        local('cp -rf content/pages/singarna-symposium-2016/* {deploy_path}/singarna-symposium-2016/'.format(**env))

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('make html')
    collectstatic()

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
