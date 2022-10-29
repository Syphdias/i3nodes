#!/usr/bin/env python3
from i3ipc import Connection


def print_or_nodes(o, depth=0):
    name = o.name or ""
    print(f"{'  '*depth}{o.type}: {name} ({o.layout})")
    if o.nodes:
        for n in o.nodes:
            print_or_nodes(n, depth + 1)


if __name__ == "__main__":
    i3 = Connection()
    print_or_nodes(i3.get_tree())
