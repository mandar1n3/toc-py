
from toc_py.utils.extract_headings import extract_headings


def test_extracts_multiple_headings():
    markdown = """# Introduction
this is the beginning of the text
## Installation
instructions to install the program
### Contributors
Jone Doe
Jane Doe
"""     
    assert extract_headings(markdown) == [
            (1, "Introduction"),
            (2, "Installation"),
            (3, "Contributors")
            ]

def test_extracts_duplicate_headings():
    markdown = """# Introduction
# Introduction"""
    assert extract_headings(markdown) == [(1, "Introduction"),
                                          (1, "Introduction")
                                          ]

def test_extracts_headings_with_trailing_new_line():
    markdown = """# Hello World\n"""
    assert extract_headings(markdown) == [(1, "Hello World")]

def test_extracts_handles_headings_separated_by_a_newline():
    markdown = """# Contribution

# Sponsors
    """
    assert extract_headings(markdown) == [
            (1, "Contribution"),
            (1, "Sponsors")
            ]

def test_extract_headings_handles_empty_markdown():
    assert extract_headings("") == []

def test_extract_headings_handles_no_headings():
    markdown = """**Hello World** !, this is some makrdown that has no headings
Will it pass the _test_ ?
"""
    assert extract_headings(markdown) == []

def test_extracts_one_heading():
    markdown = "# Introduction"
    assert extract_headings(markdown) == [(1, "Introduction")]
