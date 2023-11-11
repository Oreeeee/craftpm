# SPDX-License-Identifier: GPL-3.0-or-later
from dataclasses import dataclass


@dataclass
class CraftProject:
    project_type: str
    server_engine: str
    server_version: str
    components: list
