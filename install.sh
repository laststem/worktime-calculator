#!/usr/bin/env bash
path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo "alias worktime='python3 $path/main.py'" >> ~/.zshrc
