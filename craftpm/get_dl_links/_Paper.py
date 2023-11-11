# SPDX-License-Identifier: GPL-3.0-or-later
import requests


class Paper:
    BUILDS_LINK: str = (
        "https://api.papermc.io/v2/projects/paper/versions/{mc_ver}/builds"
    )
    DOWNLOAD_LOCATION: str = "https://api.papermc.io/v2/projects/paper/versions/{mc_ver}/builds/{build_id}/downloads/{filename}"

    @classmethod
    def get_download_link(cls, mc_ver: str) -> str:
        latest_build: dict = requests.get(cls.BUILDS_LINK.format(mc_ver=mc_ver)).json()[
            "builds"
        ][-1]

        build_id: str = str(latest_build["build"])
        filename: str = latest_build["downloads"]["application"]["name"]
        download_link: str = cls.DOWNLOAD_LOCATION.format(
            mc_ver=mc_ver, build_id=build_id, filename=filename
        )

        return download_link
