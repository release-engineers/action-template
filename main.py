#!/usr/bin/env python
import jinja2
import json
import sys
import markupsafe

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <template> <json file 1> ... <json file N>', file=sys.stderr)
    exit(1)

jinja_loader = jinja2.FileSystemLoader('./')
jinja_environment = jinja2.Environment(loader=jinja_loader)
jinja_environment.globals['include_file'] = lambda name: markupsafe.Markup(jinja_loader.get_source(jinja_environment, name)[0])
jinja_template = jinja_environment.get_or_select_template(sys.argv[1])

data = {}
for i in range(2, len(sys.argv)):
    file_path = sys.argv[i]
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        file_name_ext = file_path.split('/')[-1]
        if file_name_ext.endswith('.json'):
            file_name = file_name_ext.split('.')[0]
            file_data = json.loads(file_content)
            data[file_name] = file_data

rendered = jinja_template.render(data)
print(rendered)
