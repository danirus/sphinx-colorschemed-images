.DEFAULT_GOAL := help

.PHONY: coverage help

py-tests:  ## Run Python tests with coverage.
	coverage erase
	coverage run --source=sphinx_colorschemed_images \
		--omit=*migrations*,*tests* -m pytest -ra
	coverage report -m
	@sh ./ccsvg.sh ||:

js-tests:  ## Run JavaScript tests.
	npm run test

build-ext:  ## Build Sphinx extension.
	rm sphinx_colorschemed_images/static/*
	npm run build-script
	npm run build-module
	cp dist/js/sphinx-colorschemed-images.js sphinx_colorschemed_images/static/
	python -m build

build-docs:  ## Create sphinx-colorschemed-images documentation.
	make -C docs clean
	make -C docs html

serve-lcov:  js-tests  ## Web server for content from lcov-report directory.
	python -m http.server -d js/coverage/lcov-report 8193

serve-docs:  build-docs  ## Web server for the sphinx-nefertiti documentation.
	python -m http.server -d docs/build/html 8194

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done