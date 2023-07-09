<!-- README.md is auto-generated from README.md.template -->

# release-engineers/action-template

[![Status: Production ready](https://img.shields.io/badge/status-production_ready-green)](https://release-engineers.com/open-source-badges/)
[![PyPI version](https://badge.fury.io/py/re-y.svg)](https://badge.fury.io/py/re-action-template)

`action-template` runs the Jinja2 templating engine against any given files during a GitHub workflow, and makes the GitHub context available to it.

## Usage

action-template can be used as a GitHub Action;

```yml
name: Generate README.md

on:
  push:
    branches:
      - master
    paths:
      - 'README.md.template'
  workflow_dispatch:

defaults:
  run:
    shell: bash --login {0}

permissions:
  contents: write

jobs:
  run-templating:
    runs-on: ubuntu-latest
    steps:
      - uses: release-engineers/action-setup-bash@v1
      - uses: actions/checkout@v2
      - uses: release-engineers/action-template@v1
        with:
          source: 'README.md.template'
          target: 'README.md'
      - run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit --no-verify -m "docs: Regenerate README.md"
          
          # rebase and push in a retry loop
          for i in {1..5}; do
            git pull --rebase && git push && break || sleep 1
          done

```

## Features

### GitHub Context

The GitHub context available to workflows is also available to templates like so;


```
{{ github.repository }}
```


When evaluated becomes:

```
release-engineers/action-template
```

### Load Files

The example workflow under the Usage paragraph was loaded using;


```yml
{{ load('.github/workflows/example.yml') }}
```


### Load JSON

Parse and handle JSON data from files in the working directory like so;


```
{{ load_json('tests/data/data.json').info.from_json }}
```


When evaluated becomes:

```
This text is a JSON value in a file.
```

### Load YAML

Parse and handle YAML data from files in the working directory like so;


```
{{ load_yaml('tests/data/data.yml').info.from_yaml }}
```


When evaluated becomes:

```
This text is a YAML value in a file
```

### Load Markdown Table of Contents as HTML

Parse and obtain a Markdown table of contents from files in the working directory like so;


```
{{ load_markdown_toc('tests/data/data.md') }}
```


When evaluated becomes:

```
<div class="toc">
<ul>
<li><a href="#header-one">Header One</a><ul>
<li><a href="#header-two">Header Two</a><ul>
<li><a href="#header-three">Header Three</a></li>
<li><a href="#header-three-two">Header Three, Two</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>

```

### Load Markdown Table of Contents as data

Parse and handle Markdown table of contents data from files in the working directory like so;


```
{{ load_markdown_toc_tokens('tests/data/data.md') }}
```


When evaluated becomes:

```
[{'level': 1, 'id': 'header-one', 'name': 'Header One', 'children': [{'level': 2, 'id': 'header-two', 'name': 'Header Two', 'children': [{'level': 3, 'id': 'header-three', 'name': 'Header Three', 'children': []}, {'level': 3, 'id': 'header-three-two', 'name': 'Header Three, Two', 'children': []}]}]}]
```

## Contributing

This is a Python Poetry project using [Fire](https://github.com/google/python-fire).
See [Poetry](https://python-poetry.org/) for more information.

Development requires:

- Bash
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

See [`app.sh`](./app.sh) for building, running and releasing the application.

## Links

This project was created using [template-poetry](https://github.com/release-engineers/template-poetry).
