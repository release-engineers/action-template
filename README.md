<!-- README.md is auto-generated from README.md.template -->

# [EffortGames/action-template](https://github.com/EffortGames)

`action-template` runs the Jinja2 templating engine against any given files during a GitHub workflow, and makes the GitHub context available to it.

> ⚠️This action runs setup-python and runs pip install globally. If you care about this, make sure to run the action in a separate job.

## Usage

Refer to the [generate-readme workflow](.github/workflows/generate-readme.yml) and [template](./README.md.template);

```yml
name: Update README.md

on:
  push:
    branches:
      - master
    paths:
      - 'README.md.template'
      - '.github/workflows/generate-readme.yml'

permissions:
  contents: write

jobs:
  run-templating:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: EffortGames/action-template@v1
        with:
          source: 'README.md.template'
          target: 'README.md'
      - run: |
          git config --global user.email "automation@effortgames.nl"
          git config --global user.name "EffortGames Automation"
          git add README.md
          if git commit -m"Update README.md"; then
            git push origin master
          fi

```

## Templates

This action runs Jinja2 with a few extra's;

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

Parse and handle JSON data from files in the working directory like so;


```
{{ load_json('sample/data.json').info.from_json }}
```


When evaluated becomes:

```
This text comes from a JSON file.
```

### Load YAML

Parse and handle YAML data from files in the working directory like so;


```
{{ load_yaml('sample/data.yml').info.from_yaml }}
```


When evaluated becomes:

```
This text comes from a YAML file
```

### Load Markdown Table of Contents as HTML

Parse and obtain a Markdown table of contents from files in the working directory like so;


```
{{ load_markdown_toc('sample/data.md') }}
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
{{ load_markdown_toc_tokens('sample/data.md') }}
```


When evaluated becomes:

```
[{'level': 1, 'id': 'header-one', 'name': 'Header One', 'children': [{'level': 2, 'id': 'header-two', 'name': 'Header Two', 'children': [{'level': 3, 'id': 'header-three', 'name': 'Header Three', 'children': []}, {'level': 3, 'id': 'header-three-two', 'name': 'Header Three, Two', 'children': []}]}]}]
```

## Development

Try it locally with Python 3.x;

    pip install -r requirements.txt
    ./main.py README.md.template "$(cat sample/github.json)"
