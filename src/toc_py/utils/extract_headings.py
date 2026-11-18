from toc_py.utils import get_heading_level


def extract_headings(markdown: str) -> list[tuple[int, str]]:
    headings = []
    lines = markdown.splitlines()
    for line in lines:
        level = get_heading_level(line)
        if level is None:
            continue
        headings.append((level, line.removeprefix("#" * level).strip()))
    return headings
