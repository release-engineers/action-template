#!/usr/bin/env python
import jinja2
import json
import sys
import markupsafe
import yaml

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} <template> <github context>', file=sys.stderr)
    exit(1)

j2loader = jinja2.FileSystemLoader('./')
j2environment = jinja2.Environment(loader=j2loader)
j2environment.globals['load'] = lambda name: markupsafe.Markup(j2loader.get_source(j2environment, name)[0])
j2environment.globals['load_json'] = lambda name: json.loads(j2loader.get_source(j2environment, name)[0])
j2environment.globals['load_yaml'] = lambda name: yaml.safe_load(j2loader.get_source(j2environment, name)[0])
j2template = j2environment.get_or_select_template(sys.argv[1])
github = json.loads(sys.argv[2])

rendered = j2template.render(github=github)
print(rendered)
