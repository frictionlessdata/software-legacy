.PHONY: all readme

all: list

readme:
	pip install md-toc
	md_toc -p README.md github --header-levels 3
	sed -i '/(#frictionless-data-implementations)/,+1d' README.md
