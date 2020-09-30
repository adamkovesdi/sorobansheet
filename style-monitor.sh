#!/bin/bash

echo "Starting pycodestyle monitor"
watchmedo shell-command \
  --patterns="*.py;*.txt" \
  --recursive \
  --command='clear; pycodestyle "${watch_src_path}"; echo "\n[pycodestyle]"' \
  .
