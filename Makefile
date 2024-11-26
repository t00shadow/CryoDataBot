.PHONY: install clear uninstall

install:
	pip install .
	make clear

clear:
	rm -rf build dist *.egg-info

uninstall:
	pip uninstall cryodatabot