# SPDX-License-Identifier: GPL-3.0-or-later
import requests
from rich.progress import Progress

from .structs import Download


class Downloader:
    def __init__(self, downloads: list) -> None:
        for download in downloads:
            self.download_file(download)

    def download_file(self, download: Download) -> None:
        dl_stream = requests.get(download.link, stream=True)
        file_size: int = int(dl_stream.headers.get("Content-Length"))
        chunk_size: int = 1024
        with open(download.filename, "wb") as f:
            with Progress() as progress:
                dl_task = progress.add_task(download.filename, total=file_size)
                for chunk in dl_stream.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    progress.update(dl_task, advance=chunk_size)
