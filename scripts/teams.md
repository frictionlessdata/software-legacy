# Teams

List of teams and maintainers for FrictionlessData repositories.

## Repositories

Name  |  Maintainer
----- |  ----------
{% for team, names in teams.items() -%}
{% set team_short = team.split('/')|reverse|list|first -%}
**{{ team }}** | [![Team](https://img.shields.io/badge/team-{{ team_short|urlencode|replace('-', '--') }}-blue)](https://github.com/orgs/frictionlessdata/teams/{{ team_short }})
{% for name in names -%}
{% set repo = repos[name] -%}
**<a href="https://github.com/frictionlessdata/{{ repo.name }}">`{{ repo.name }}`</a>** | {% if repo.maintainer %}[![User](https://img.shields.io/badge/user-{{ repo.maintainer }}-brightgreen)](https://github.com/{{ repo.maintainer }}){% endif %}
{% endfor -%}
{% endfor -%}
