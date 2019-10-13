# Teams

List of teams and maintainers for FrictionlessData repositories.

## Repositories

Name  |  Maintainer
----- |  ----------
{% for team, names in teams.items() -%}
**<a href="https://github.com/orgs/frictionlessdata/teams/{{ team.split('/')|reverse|list|first }}" style="color:black">{{ team }}</a>** |
{% for name in names -%}
{% set repo = repos[name] -%}
**<a href="https://github.com/frictionlessdata/{{ repo.name }}">`{{ repo.name }}`</a>** | {% if repo.maintainer %}[![User](https://img.shields.io/badge/user-{{ repo.maintainer|urlencode }}-brightgreen)](https://github.com/{{ repo.maintainer }}){% endif %}
{% endfor -%}
{% endfor -%}
