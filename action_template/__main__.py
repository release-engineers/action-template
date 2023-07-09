import fire
from action_template.main import CLI


def main():
    fire.Fire(component=CLI, name="action-template")


if __name__ == "__main__":
    main()
