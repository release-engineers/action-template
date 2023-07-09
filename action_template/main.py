#!/usr/bin/env python
import jinja2
import json
import sys
import markupsafe
import yaml
import markdown


class CLI(object):
    def __init__(self, template_search_path='./'):
        def load_markdown_toc(text):
            md = markdown.Markdown(extensions=['toc'])
            md.convert(text)
            return md.toc

        def load_markdown_toc_tokens(text):
            md = markdown.Markdown(extensions=['toc'])
            md.convert(text)
            return md.toc_tokens

        j2loader = jinja2.FileSystemLoader(template_search_path)
        self.j2environment = jinja2.Environment(loader=j2loader)
        self.j2environment.globals['load'] = lambda name: markupsafe.Markup(j2loader.get_source(self.j2environment, name)[0])
        self.j2environment.globals['load_json'] = lambda name: json.loads(j2loader.get_source(self.j2environment, name)[0])
        self.j2environment.globals['load_yaml'] = lambda name: yaml.safe_load(j2loader.get_source(self.j2environment, name)[0])
        self.j2environment.globals['load_markdown_toc'] = lambda text: load_markdown_toc(j2loader.get_source(self.j2environment, text)[0])
        self.j2environment.globals['load_markdown_toc_tokens'] = lambda text: load_markdown_toc_tokens(j2loader.get_source(self.j2environment, text)[0])

    def render(self, template_path: str, github_context_json: str | dict):
        try:
            j2template = self.j2environment.get_or_select_template(template_path)
            if isinstance(github_context_json, str):
                github = json.loads(github_context_json)
            elif isinstance(github_context_json, dict):
                github = github_context_json
            else:
                raise Exception(f"Unknown type for github_context_json: {type(github_context_json)}")

            return j2template.render(github=github)
        except Exception as e:
            print(f"Erred with configuration:", file=sys.stderr)
            print(f"  template_path: {template_path}", file=sys.stderr)
            print(f"  github_context_json: {github_context_json}", file=sys.stderr)
            import os
            print(f"  cwd: {os.getcwd()}", file=sys.stderr)
            print(f"  ls: {os.listdir('.')}", file=sys.stderr)
            raise e
