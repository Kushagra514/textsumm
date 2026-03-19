
#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: bash scripts/analyse.sh path/to/file.txt"
  exit 1
fi

echo "Running textsumm on $1..."
poetry run textsumm "$1"