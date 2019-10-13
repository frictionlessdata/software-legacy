# Teams

List of teams and maintainers for FrictionlessData repositories.

## Repositories

Name  |  Maintainer
----- |  ----------
{% for team, names in teams.items() -%}
**<a href="https://github.com/orgs/frictionlessdata/teams/{{ team.split('/')|reverse|list|first }}">{{ team }}</a>** |
{% for name in names -%}
{% set repo = repos[name] -%}
**<a href="https://github.com/frictionlessdata/{{ repo.name }}">`{{ repo.name }}`</a>** | {% if repo.maintainer %}[![Github](https://img.shields.io/badge/github-{{ repo.maintainer }}-brightgreen)](https://github.com/{{ repo.maintainer }}){% endif %}
{% endfor -%}
{% endfor -%}
