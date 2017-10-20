from typing import Tuple

import aiohttp

from .types import Urls


def get_aiohttp_version() -> Tuple[int, int]:
    """Return tuple of current aiohttp MAJOR.MINOR version."""
    return tuple(  # type: ignore
        int(item) for item in aiohttp.__version__.split('.')[:2])


def match_request(urls: Urls, method: str, path: str) -> bool:
    """Check whether request method and path matches given URLs or not."""
    found = [item for item in urls if item == path]
    if not found:
        return False

    if not isinstance(urls, dict):
        return True

    found_item = urls[found[0]]
    method = method.lower()
    if isinstance(found_item, str):
        return found_item.lower() == method

    return any(True for item in found_item if item.lower() == method)
