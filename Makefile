default_target: help
.PHONY : default_target upload

# VERSION := $(shell $(PYTHON) setup.py --version)
help:
	@# @ is silent
	@echo ""
	@echo "pycommon makefile"
	@echo ""
	@echo "   help           - this"
	@echo "   build          - build wheel and test"
	@echo "   upload         - push to nexus as 'simonski-pycommon'"
	@echo "   clean          - remove build files"
	@echo ""


clean:
	rm -rf dist
	rm -rf build
	rm -rf target
	rm -rf tests/.cache
	rm -rf .pytest_cache
	rm -rf pycommon.egg-info
	find . -name *.pyc -type f -delete
	find . -name *__pycache__ -delete

	python setup.py clean

test:
	python setup.py test

build: clean test
	python setup.py test bdist
	# python setup.py test bdist_wheel 

upload: clean build
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
