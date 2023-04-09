#!/usr/bin/env python3
from i3ipc import Connection
from sys import argv


def print_or_nodes(o, depth=0):
    name = o.name or ""
    print(f"{'  '*depth}{o.type}: {o.id} {name} ({o.layout})")
    if o.nodes:
        for n in o.nodes:
            print_or_nodes(n, depth + 1)


if __name__ == "__main__":
    i3 = Connection()
    tree = i3.get_tree()
    if len(argv) > 1 and (argv[1] or "") == "focused":

        print_or_nodes(tree.find_focused().workspace())
    else:
        print_or_nodes(tree)
