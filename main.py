#!/usr/bin/env python
import jinja2
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <template> <data file 1> ... <data file N>', file=sys.stderr)
    exit(1)

with open(sys.argv[1], 'r') as f:
    template = jinja2.Template(f.read())

data = {}
files = {}
for i in range(2, len(sys.argv)):
    file_path = sys.argv[i]
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        files[file_path] = file_content
        file_name_ext = file_path.split('/')[-1]
        if file_name_ext.endswith('.json'):
            file_name = file_name_ext.split('.')[0]
            file_data = json.loads(file_content)
            data[file_name] = file_data

rendered = template.render(data, files=files)
print(rendered)
