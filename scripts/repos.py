import re
import yaml
import time
import requests


# Helpers

def sync_repos():
    repos = get_repos()
    with open('scripts/repos.yml', 'w') as file:
        yaml.dump(repos, file)


def get_repos():
    repos = {}
    for page in range(1, 4):
        url = 'https://api.github.com/orgs/frictionlessdata/repos?page=%s' % page
        for repo in requests.get(url).json():
            repo['maintainer'] = get_maintainer(repo)
            repos[repo['name']] = repo
            print('Collected: %s' % repo['name'])
    return repos


def get_maintainer(repo):
    time.sleep(0.1)
    url = 'https://raw.githubusercontent.com/%s/master/MAINTAINER.md' % repo['full_name']
    res = requests.get(url)
    maintainer = res.text.strip() if res.status_code == 200 else None
    if not maintainer:

        # specifications
        if repo['name'] == 'specs':
            maintainer = 'rufuspollock'

        # software-broad/datapackge-pipelines
        if repo['name'].startswith('datapackage-pipelines') or repo['name'].startswith('dataflows'):
            maintainer = 'akariv'

        # software-broad/datapackage-render
        if repo['name'] == 'datapackage-render-js':
            maintainer = 'anuveyatsu'

        # software-broad/datapackage-googlesheets
        if repo['name'] == 'googlesheets-datapackage-tools':
            maintainer = 'stephanmax'

        # software-broad/datapackage-darwin-core
        if repo['name'] == 'FrictionlessDarwinCore':
            maintainer = 'andrejjh'

        # software-broad/delimiter
        if repo['name'] == 'delimiter':
            maintainer = 'timwis'

    return maintainer


# Main

if __name__ == '__main__':
    sync_repos()
