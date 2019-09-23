.PHONY: all install readme

all: list

install:
	pip install -r requirements.txt

readme:
	pip install md-toc
	md_toc -p README.md github --header-levels 3
	sed -i '/(#frictionless-data-implementations)/,+1d' README.md

status:
	python scripts/status.py > STATUS.md
