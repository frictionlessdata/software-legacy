# Teams

List of teams and maintainers for FrictionlessData repositories.

## Repositories

Name  |  Lead
----- |  -----
{% for team, names in teams.items() -%}
{% set team_short = team.split('/')|reverse|list|first -%}
**{{ team }}** | [![Github](https://img.shields.io/badge/github-{{ team_short|urlencode|replace('-', '--') }}-blue)](https://github.com/orgs/frictionlessdata/teams/{{ team_short }})
{% for name in names -%}
{% set repo = repos[name] -%}
**<a href="https://github.com/frictionlessdata/{{ repo.name }}">`{{ repo.name }}`</a>** | {% if repo.maintainer %}[![Github](https://img.shields.io/badge/github-{{ repo.maintainer }}-brightgreen)](https://github.com/{{ repo.maintainer }}){% endif %}
{% endfor -%}
{% endfor -%}
