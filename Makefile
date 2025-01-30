# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE


# ### INTERNAL SETTINGS

# The absolute path to the repository.
#
# This assumes that this ``Makefile`` is placed in the root of the repository.
# REPO_ROOT does not contain a trailing ``/``
#
# Ref: https://stackoverflow.com/a/324782
# Ref: https://stackoverflow.com/a/2547973
# Ref: https://stackoverflow.com/a/73450593
REPO_ROOT := $(patsubst %/, %, $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

# The name of the application, used throughout this Makefile
APP_NAME := penthouse

APP_DIR := $(REPO_ROOT)/$(APP_NAME)
APP_STATIC_DIR := $(APP_DIR)/static/$(APP_NAME)
APP_AUX_DIR := $(REPO_ROOT)/auxiliary

# Intermediate build targets
APP_STYLESHEET := $(APP_STATIC_DIR)/style.css
APP_SCRIPT := $(APP_STATIC_DIR)/penthouse.js

# The source files for the actual intermediate build targets
APP_STYLE_SRC_DIR := $(APP_AUX_DIR)/style
APP_STYLE_SRC := $(shell find $(APP_STYLE_SRC_DIR) -type f)
APP_SCRIPT_SRC_DIR := $(APP_AUX_DIR)/script
APP_SCRIPT_SRC := $(shell find $(APP_SCRIPT_SRC_DIR) -type f)


# Internal Python environments
#
# Actually this does only handle the setup of ``tox``, while the actual build
# scripts are executed through ``tox``'s environments.
TOX_VENV_DIR := $(REPO_ROOT)/.tox-venv
TOX_VENV_CREATED := $(TOX_VENV_DIR)/pyvenv.cfg
TOX_VENV_INSTALLED := $(TOX_VENV_DIR)/packages.txt
TOX_CMD := $(TOX_VENV_DIR)/bin/tox


# Stamps
#
# Track certain step of the build process with artificial stamps.
STAMP_DIR := $(REPO_ROOT)/.make-stamps
STAMP_NODE_READY := $(STAMP_DIR)/node-ready


## Shortcut
## @category Development
run: $(APP_STYLESHEET) $(APP_SCRIPT) django/runserver
.PHONY : run


# Remove build artifacts
clean :
.PHONY : clean

# Remove build environments
full-clean : clean
	rm -rf $(TOX_VENV_DIR)
	rm -rf $(REPO_ROOT)/.tox
.PHONY : full-clean


# ### Django management commands

django_command ?= "version"
django : $(TOX_VENV_INSTALLED)
	$(TOX_CMD) -q -e django -- $(django_command)
.PHONY : django

## "$ django-admin check"; runs the project's checks
## @category Django
django/check :
	$(MAKE) django django_command="check"
.PHONY : django/check

## "$ django-admin clearsessions"; clears the session from the backend
## @category Django
django/clearsessions :
	$(MAKE) django django_command="clearsessions"
.PHONY : django/clearsessions

## "$ django-admin compilemessages"; compiles the app's *.po files to *.mo
## @category Django
django/compilemessages :
	$(MAKE) django django_command="compilemessages --ignore=.tox --ignore=tests --ignore=docs"
.PHONY : django/compilemessages

## create a superuser account with username: "admin" and password: "foobar"
## @category Django
django/createsuperuser : $(TOX_VENV_INSTALLED)
	$(TOX_CMD) -q -e djangosuperuser
.PHONY : django/createsuperuser

## "$ django-admin makemessages"; collect the app's localizable strings into *.po
## @category Django
django/makemessages :
	$(MAKE) django django_command="makemessages --locale=en --locale=de --ignore=.tox --ignore=tests --ignore=docs"
.PHONY : django/makemessages

# Create the migrations for the app to be developed!
# TODO: The app name is hardcoded here!
## "$ django-admin makemigrations"; create migrations
## @category Django
django/makemigrations :
	$(MAKE) django django_command="makemigrations penthouse"
.PHONY : django/makemigrations

## "$ django-admin migrate"; apply the project's migrations
## @category Django
django/migrate :
	$(MAKE) django django_command="migrate"
.PHONY : django/migrate

host_port ?= "0:8000"
## "django-admin runserver"; runs Django's development server with host = "0"
## and port = "8000".
## Host and port might be specified by "make django/runserver host_port="0:4444"
## to run the server on port "4444".
## @category Django
django/runserver : django/migrate django/clearsessions
	$(MAKE) django django_command="runserver $(host_port)"
.PHONY : django/runserver

## "django-admin shell"; run a REPL with the project's settings
## @category Django
django/shell :
	$(MAKE) django django_command="shell"
.PHONY : django/shell


# ### utility targets

## Run bandit on all files (*.py)
## @category Code Quality
util/bandit :
	$(MAKE) util/pre-commit pre-commit_id="bandit" pre-commit_files="--all-files"
.PHONY : util/bandit

## Run black on all files (*.py)
## @category Code Quality
util/black :
	$(MAKE) util/pre-commit pre-commit_id="black" pre-commit_files="--all-files"
.PHONY : util/black

## Run djlint on all files (*.html)
## @category Code Quality
util/djlint :
	$(MAKE) util/pre-commit pre-commit_id="djlint-django" pre-commit_files="--all-files"
.PHONY : util/djlint

## Run doc8 on all files (*.rst)
## @category Code Quality
util/doc8 :
	$(MAKE) util/pre-commit pre-commit_id="doc8" pre-commit_files="--all-files"
.PHONY : util/doc8

## Run flake8 on all files (*.py)
## @category Code Quality
util/flake8 :
	$(MAKE) util/pre-commit pre-commit_id="flake8" pre-commit_files="--all-files"
.PHONY : util/flake8

## Run isort on all files (*.py)
## @category Code Quality
util/isort :
	$(MAKE) util/pre-commit pre-commit_id="isort" pre-commit_files="--all-files"
.PHONY : util/isort

## Run prettier on all files (*.scss/*.ts)
## @category Code Quality
util/prettier :
	$(MAKE) util/pre-commit pre-commit_id="prettier" pre-commit_files="--all-files"
.PHONY : util/prettier

## Run stylelint on all files (*.scss)
## @category Code Quality
util/stylelint :
	$(MAKE) util/pre-commit pre-commit_id="stylelint" pre-commit_files="--all-files"
.PHONY : util/stylelint

## Run eslint on all files (*.ts)
## @category Code Quality
util/eslint :
	$(MAKE) util/pre-commit pre-commit_id="eslint" pre-commit_files="--all-files"
.PHONY : util/eslint

pre-commit_id ?= ""
pre-commit_files ?= ""
## Run all code quality tools as defined in .pre-commit-config.yaml
## @category Code Quality
util/pre-commit : $(TOX_VENV_INSTALLED)
	$(TOX_CMD) -q -e util -- pre-commit run $(pre-commit_files) $(pre-commit_id)
.PHONY : util/pre-commit

## Install pre-commit hooks to be executed automatically
## @category Code Quality
util/pre-commit/install : $(TOX_VENV_INSTALLED)
	$(TOX_CMD) -q -e util -- pre-commit install
.PHONY : util/pre-commit/install

## Update pre-commit hooks
## @category Code Quality
util/pre-commit/update : $(TOX_VENV_INSTALLED)
	$(TOX_CMD) -q -e util -- pre-commit autoupdate
.PHONY : util/pre-commit/update

# (Re-) Generate the requirements files using pip-tools (``pip-compile``)
#
# ``pip-compile`` is run through a ``tox`` environment. The actual command is
# included in ``tox``'s configuration in ``pyproject.toml``. That's why that
# file is an additional prerequisite. This may lead to additional
# regenerations, but these will most likely not affect the generated files.
requirements/%.txt : requirements/%.in pyproject.toml | $(TOX_VENV_INSTALLED)
	$(TOX_CMD) -q -e pip-tools -- $<

# Compile SCSS sources to an actual stylesheet
$(APP_STATIC_DIR)/%.css : $(APP_STYLE_SRC_DIR)/%.scss $(APP_STYLE_SRC) | $(STAMP_NODE_READY)
	$(create_dir)
	npx sass --embed-sources --embed-source-map --stop-on-error --verbose $< $@

# Compile TS sources to an actual script
$(APP_STATIC_DIR)/%.js : $(APP_SCRIPT_SRC_DIR)/%.ts $(APP_SCRIPT_SRC) | $(STAMP_NODE_READY)
	$(create_dir)
	npx rollup -c rollup.config.js --bundleConfigAsCjs -i $< -o $@


# ##### Internal utility stuff

# Create the virtual environment for running tox
$(TOX_VENV_CREATED) :
	/usr/bin/env python3 -m venv $(TOX_VENV_DIR)

# Install the required packages in tox's virtual environment
$(TOX_VENV_INSTALLED) : $(TOX_VENV_CREATED)
	$(TOX_VENV_DIR)/bin/pip install -r requirements/tox.txt
	$(TOX_VENV_DIR)/bin/pip freeze > $@

# Install the required NodeJS packages
#
# Uses npm's ``ci`` to create the required NodeJS environment. It (re-) uses
# a local cache for npm in order to speed up builds during CI.
#
# https://stackoverflow.com/a/58187176
$(STAMP_NODE_READY) : package.json package-lock.json
	$(create_dir)
	npm ci --cache .npm --prefer-offline
	touch $@

# Create a directory as required by other recipes
create_dir = @mkdir -p $(@D)
