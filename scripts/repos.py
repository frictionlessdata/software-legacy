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
    url = 'https://raw.githubusercontent.com/%s/master/.github/issue_template.md' % repo['full_name']
    match = re.findall(r'\@(\w*)', requests.get(url).text)
    maintainer = match[0] if match else None
    # TODO: rebase on the in-repo style
    if not maintainer:
        if repo['name'] == 'specs':
            maintainer = 'rufuspollock'
        if repo['name'].startswith('datapackage-pipelines'):
            maintainer = 'akariv'
        if repo['name'].startswith('dataflows'):
            maintainer = 'akariv'
        if repo['name'] == 'datapackage-render-js':
            maintainer = 'anuveyatsu'
        if repo['name'] == 'googlesheets-datapackage-tools':
            maintainer = 'stephanmax'
        if repo['name'] == 'FrictionlessDarwinCore':
            maintainer = 'andrejjh'
        if repo['name'] == 'delimiter':
            maintainer = 'timwis'
    return maintainer


# Main

if __name__ == '__main__':
    sync_repos()
