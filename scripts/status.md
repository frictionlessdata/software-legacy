# Status

[![Python (extended)](https://img.shields.io/travis/frictionlessdata/testsuite-extended/master.svg?label=Python%20(extended))](https://travis-ci.org/frictionlessdata/testsuite-basic)
[![Python (basic)](https://img.shields.io/travis/frictionlessdata/testsuite-basic/python.svg?label=Python%20(basic))](https://travis-ci.org/frictionlessdata/testsuite-basic/branches)
[![JavaScript](https://img.shields.io/travis/frictionlessdata/testsuite-basic/javascript.svg?label=JavaScript)](https://travis-ci.org/frictionlessdata/testsuite-basic/branches)
[![Ruby](https://img.shields.io/travis/frictionlessdata/testsuite-basic/ruby.svg?label=Ruby)](https://travis-ci.org/frictionlessdata/testsuite-basic/branches)

Status of the core FrictionlessData software. See the test suites status above and packages information below.

## Packages

{% macro registry(platform, package) %}
{%- if platform == 'python' -%}
  [![PyPi](https://img.shields.io/pypi/v/{{ package.name }}.svg)](https://pypi.python.org/pypi/{{ package.name }})
{%- elif platform == 'javascript' -%}
  [![NPM](https://img.shields.io/npm/v/{{ package.name }}.svg)](https://www.npmjs.com/package/{{ package.name }})
{%- elif platform == 'ruby' -%}
  [![Gem](http://img.shields.io/gem/v/{{ package.name }}.svg)](https://rubygems.org/gems/{{ package.name }})
{%- elif platform == 'php' -%}
  [![Packagist](https://img.shields.io/packagist/v/frictionlessdata/{{ package.name }}.svg)](https://packagist.org/packages/frictionlessdata/{{ package.name }})
{%- elif platform == 'java' -%}
  [![Maven](https://img.shields.io/maven-central/v/frictionlessdata/{{ package.name }}?label=maven)](https://search.maven.org/search?q=a:{{ package.name }})
{%- elif platform in ['go', 'julia'] -%}
  [![Github](https://img.shields.io/github/v/release/frictionlessdata/{{ package.name }}?sort=semver&label=github)](https://github.com/frictionlessdata/{{ package.name }}/releases)
{%- elif platform == 'clojure' -%}
  [![Clojars](https://img.shields.io/clojars/v/{{ package.name }}.svg)](https://clojars.org/{{ package.name }})
{%- elif platform == 'r' -%}
  [![CRAN](https://img.shields.io/cran/v/{{ package.name }}.svg)](https://cran.rstudio.com/web/packages/{{ package.name }}/index.html)
{%- endif -%}
{% endmacro %}

Name  | Build | Coverage | Registry
----- | ----- | -------- | --------
{% for platform, packages in status.items() -%}
**{{ platform|capitalize }}** |
{% for package in packages -%}
**<a href="https://github.com/frictionlessdata/{{ package.repo }}">`{{ package.name }}`</a>** | [![Travis](https://img.shields.io/travis/frictionlessdata/{{ package.repo }}/master.svg)](https://travis-ci.org/frictionlessdata/{{ package.repo }}) | [![Coveralls](http://img.shields.io/coveralls/frictionlessdata/{{ package.repo }}.svg?branch=master)](https://coveralls.io/r/frictionlessdata/{{ package.repo }}?branch=master) | {{ registry(platform, package) }}
{% endfor -%}
{% endfor -%}
