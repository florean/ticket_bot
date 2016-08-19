#!/usr/local/virtualenvs/ds-py3/bin/python
import json


SECRETS_FILE = "secrets.json"


def main():
    # Twitter API setup
    with open(SECRETS_FILE) as f:
        secrets = json.load(f)


if __name__ == '__main__':
    main()
