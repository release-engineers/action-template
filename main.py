#!/usr/bin/env python
import jinja2
import json
import sys
import markupsafe
import yaml
import markdown

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} <template> <github context>', file=sys.stderr)
    exit(1)


def load_markdown_toc(text):
    md = markdown.Markdown(extensions=['toc'])
    md.convert(text)
    return md.toc


def load_markdown_toc_tokens(text):
    md = markdown.Markdown(extensions=['toc'])
    md.convert(text)
    return md.toc_tokens


j2loader = jinja2.FileSystemLoader('./')
j2environment = jinja2.Environment(loader=j2loader)
j2environment.globals['load'] = lambda name: markupsafe.Markup(j2loader.get_source(j2environment, name)[0])
j2environment.globals['load_json'] = lambda name: json.loads(j2loader.get_source(j2environment, name)[0])
j2environment.globals['load_yaml'] = lambda name: yaml.safe_load(j2loader.get_source(j2environment, name)[0])
j2environment.globals['load_markdown_toc'] = lambda text: load_markdown_toc(j2loader.get_source(j2environment, text)[0])
j2environment.globals['load_markdown_toc_tokens'] = lambda text: \
    load_markdown_toc_tokens(j2loader.get_source(j2environment, text)[0])
j2template = j2environment.get_or_select_template(sys.argv[1])
github = json.loads(sys.argv[2])

rendered = j2template.render(github=github)
print(rendered)
