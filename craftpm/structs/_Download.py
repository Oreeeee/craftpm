# SPDX-License-Identifier: GPL-3.0-or-later
from dataclasses import dataclass


@dataclass
class Download:
    filename: str
    link: str
