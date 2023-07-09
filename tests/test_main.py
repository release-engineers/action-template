import os
from action_template.main import CLI


def test_render(tmp_path):
    tmp_path = tmp_path / "merge"
    tmp_path.mkdir()
    source_dir = os.path.join(os.path.dirname(__file__), "data")
    source_path_github_json = os.path.join(source_dir, "github.json")
    with open(source_path_github_json, "r") as f:
        source_github_json = f.read()

    cli = CLI(template_search_path=source_dir)
    answer = cli.render("sample.md.template", source_github_json)
    assert answer == "Hello from release-engineers"
