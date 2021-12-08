<!-- README.md is auto-generated from README.md.template -->

# EffortGames/action-template

This action allows you run the Jinja2 templating engine against any files during a GitHub workflow, and makes the GitHub context available to it.

This repository is a GitHub action managed by [EffortGames](https://github.com/EffortGames).

⚠️This action runs setup-python and runs pip install globally. If you care about this, make sure to run the action in a separate job.

## Usage

This README.md itself is generated from [a template](README.md.template).

The [example workflow](.github/workflows/example.yml) showcases how to use the action;

```yml
name: Update README.md

on:
  push:
    branches:
      - master
    paths:
      - 'README.md.template'
      - '.github/workflows/example.yml'

permissions:
  contents: write

jobs:
  run-templating:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          repository: EffortGames/action-template
          path: my-project
      - uses: EffortGames/action-template@v1
        with:
          working_directory: './my-project'
          source: 'README.md.template'
          target: 'README.md'
      - run: |
          cd my-project
          git config --global user.email "automation@effortgames.nl"
          git config --global user.name "EffortGames Automation"
          git add README.md
          if git commit -am"Update README.md"; then
            git push origin master
          fi

```

## Templates

This action runs Jinja2 on templates with a few extra's;

### GitHub Context

The GitHub context available to workflows is also available to templates like so;


```
{{ github.repository }}
```


When evaluated becomes:

```
EffortGames/action-template
```

### Load Files

The example workflow under the Usage paragraph was loaded using;


```yml
{{ load('.github/workflows/example.yml') }}
```


### Load JSON

Load JSON data from files in the working directory like so;


```
{{ load_json('sample/data.json').info.from_json }}
```


When evaluated becomes:

```
This text comes from a JSON file.
```

### Load YAML

Load YAML data from files in the working directory like so;


```
{{ load_yaml('sample/data.yml').info.from_yaml }}
```


When evaluated becomes:

```
This text comes from a YAML file
```

## Development

Try it locally with Python 3.x;

    pip install -r requirements.txt
    ./main.py README.md.template "$(cat sample/github.json)"
