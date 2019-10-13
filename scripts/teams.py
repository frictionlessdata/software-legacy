import yaml
from jinja2 import Template


# Helpers

def render_teams():
    repos = read_data('repos')
    teams = read_data('teams')
    with open('scripts/teams.md') as file:
        template = Template(file.read())
        document = template.render(repos=repos, teams=teams)
        print(document)


def read_data(name):
    with open('scripts/%s.yml' % name) as file:
        return list(yaml.safe_load_all(file))[0]



# Extract

if __name__ == '__main__':
    render_teams()
