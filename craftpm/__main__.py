# SPDX-License-Identifier: GPL-3.0-or-later
import dataclasses
import json
import sys

from .get_dl_links import Paper
from .structs import Component, CraftProject


def init() -> None:
    example_server = CraftProject(
        project_type="server",
        server_engine="paper",
        server_version="1.20.2",
        components=[
            Component(
                name="paper",
                version="280",
                component_type="server_engine",
                location="server.jar",
            )
        ],
    )
    with open("craftpm.json", "w") as f:
        json.dump(dataclasses.asdict(example_server), f, indent=4)


def update() -> None:
    print(Paper.get_download_link("1.20.2"))


def main() -> int:
    args: list = sys.argv[1:]

    if len(args) == 0:
        print("No args")
        return 255

    if args[0] == "init":
        init()
    elif args[0] == "update":
        update()
    else:
        print("Invalid arg")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
