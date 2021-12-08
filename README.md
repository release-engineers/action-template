<!-- README.md is auto-generated from README.md.template -->

# EffortGames/action-template

This repository is a GitHub action managed by [EffortGames](https://github.com/EffortGames).

## Usage

This README.md itself is generated from [a template](README.md.template).

The [example workflow](.github/workflows/example.yml) showcases its functionality;

```yml
name: Example
on:
  workflow_dispatch:

jobs:
  run-templating:
    runs-on: ubuntu-latest
    steps:
      - name: Generate token
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.APP_ID }}
          private_key: ${{ secrets.APP_PRIVATE_KEY }}
      - name: Checkout action
        uses: actions/checkout@v2
        with:
          repository: EffortGames/action-template
          token: ${{ steps.generate_token.outputs.token }}
          path: ./action
      - name: Run action
        # this action's directory
        uses: ./action
        with:
          # your project's directory
          working_directory: './action'
          source: 'README.md.template'
          target: 'README.md'
      - run: |
          # your project's directory
          cd ./action
          git config --global user.email "automation@effortgames.nl"
          git config --global user.name "EffortGames Automation"
          git add README.md
          git commit -am"Update README.md"
          git push origin master

```
