# Status

## General

Name | Python | Javascript | Ruby
----------| ------ | ---------- | ----
**`testsuite-basic`** | [![Python](https://img.shields.io/travis/frictionlessdata/testsuite-basic/python.svg?label=Python)](https://travis-ci.org/frictionlessdata/testsuite-basic/branches) | [![JavaScript](https://img.shields.io/travis/frictionlessdata/testsuite-basic/javascript.svg?label=JavaScript)](https://travis-ci.org/frictionlessdata/testsuite-basic/branches) | [![Ruby](https://img.shields.io/travis/frictionlessdata/testsuite-basic/ruby.svg?label=Ruby)](https://travis-ci.org/frictionlessdata/testsuite-basic/branches)
**`testsuite-extended`** | [![Python](https://img.shields.io/travis/frictionlessdata/testsuite-extended/master.svg?label=Python)](https://travis-ci.org/frictionlessdata/testsuite-extended)

## Packages

Name | Build | Coverage | Package | Codebase | Chat
------- | ----- | -------- | ------- | -------- | ---
{% for platform in platforms -%}
**{{ platform|capitalize }}** |
{% for package in packages[platform] -%}
**`{{ package.name }}`** | [![Travis](https://img.shields.io/travis/frictionlessdata/{{ package.repo }}/master.svg)](https://travis-ci.org/frictionlessdata/{{ package.repo }}) | [![Coveralls](http://img.shields.io/coveralls/frictionlessdata/{{ package.repo }}.svg?branch=master)](https://coveralls.io/r/frictionlessdata/{{ package.repo }}?branch=master) | {% if platform == 'python' %}[![PyPi](https://img.shields.io/pypi/v/{{ package.name }}.svg)](https://pypi.python.org/pypi/{{ package.name }}){% else %}[![NPM](https://img.shields.io/npm/v/{{ package.name }}.svg)](https://www.npmjs.com/package/{{ package.name }}){% endif %} | [![Github](https://img.shields.io/badge/github-master-brightgreen)](https://github.com/frictionlessdata/{{ package.repo }}) | [![Gitter](https://img.shields.io/gitter/room/frictionlessdata/chat.svg)](https://gitter.im/frictionlessdata/chat)
{% endfor -%}
{% endfor -%}
