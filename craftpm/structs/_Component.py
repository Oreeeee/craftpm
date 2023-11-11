# SPDX-License-Identifier: GPL-3.0-or-later
from dataclasses import dataclass


@dataclass
class Component:
    component_type: str
    version: str
    name: str
    location: str
