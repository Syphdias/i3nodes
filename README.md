## About
Very small script to show the i3 tree in a concise way.

- Documentation (and FAQ – if any) can be found in this README.
- There is currently no package to install the script.
  You need to download it from [here](
  https://raw.githubusercontent.com/Syphdias/i3nodes/main/i3nodes.py)
  or clone the repository.
- Feel free to file issues to report bugs, ask questions,
  or request features.
- Feel free to open a pull request. Please use the [black](
  https://github.com/psf/black) code formatter.

## Requirements
Requires python 3.5+
```
pip install --user -r requirements.txt
```

## Usage
Use script with no argument to show nodes/children of everything (root, all
outputs, all workspaces). Use `./i3nodes.py focused` to only show
nodes/children of the focused workspace.
