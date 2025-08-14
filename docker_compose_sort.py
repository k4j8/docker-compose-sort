from __future__ import annotations

import argparse
import os
import sys
from typing import Any

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

yaml = YAML(typ="rt")
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)


def reorder_yaml_by_template(template_path: str, data_path: str) -> None:
    """
    Reorder the keys of a YAML file (data_path) to match the order of keys
    in a template YAML file (template_path), preserving parent hierarchy
    and comments.

    Any keys in the data file that are not in the template will be placed
    after the template keys in their original order.
    """
    with open(template_path, "r") as f:
        template = yaml.load(f)
    with open(data_path, "r") as f:
        data = yaml.load(f)

    def reorder_in_place(template_node: Any, data_node: CommentedMap) -> None:
        # If parent is not defined in template, do not sort
        if not isinstance(template_node, CommentedMap):
            return

        wildcard_template = None
        if "ALL" in template_node:
            wildcard_template = template_node['ALL']

        # For current level, keys in template first, then any extras
        desired_keys = [ k for k in template_node if k != "ALL" and k in data_node ]  
        desired_keys += [ k for k in data_node if k not in desired_keys ]

        # Reorder keys in place without losing comments
        for key in desired_keys:
            if key in data_node:
                val = data_node.pop(key)
                data_node[key] = val  # reinsert at end in correct order
                if isinstance(val, CommentedMap):
                    # If it is a dictionary, sort through its keys (recursion)
                    reorder_in_place(template_node.get(key, wildcard_template), val)

    reorder_in_place(template, data)

    if args.write:
        with open(data_path, "w") as f:
            yaml.dump(data, f)
    else:
        yaml.dump(data, sys.stdout)


def main():
    parser = argparse.ArgumentParser(
        prog="docker-compose-sort",
        description="Opinionated sort for restructuring Docker Compose YAML sections to a standardized order. By default, output is written to stdout.",
    )
    # parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument(
        "filepath",
        nargs="?",
        default="docker-compose.yml",
        help="Path to file to format",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="edit file in-place"
    )

    global args
    args = parser.parse_args()

    reorder_yaml_by_template(
        os.path.join(os.path.dirname(__file__), "template.yaml"), args.filepath
    )


if __name__ == "__main__":
    main()
