.PHONY: all install readme


MAINTAINER := $(shell head -n 1 MAINTAINER.md)


all: list

install:
	pip install -r requirements.txt

readme:
	pip install md-toc
	md_toc -p README.md github --header-levels 3
	sed -i '/(#frictionless-data-implementations)/,+1d' README.md

templates:
	sed -i -E "s/@(\w*)/@$(MAINTAINER)/" .github/issue_template.md
	sed -i -E "s/@(\w*)/@$(MAINTAINER)/" .github/pull_request_template.md

status:
	python scripts/status.py > STATUS.md

teams:
	python scripts/teams.py > TEAMS.md
