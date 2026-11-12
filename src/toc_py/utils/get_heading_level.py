import re

def get_heading_level(line: str) -> int | None:
    hashes = re.match(r"(#{1,6}) .+", line)
    if not hashes:
        return None
    return len(hashes.group(1))
