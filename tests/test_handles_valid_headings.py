from toc_py.utils import get_heading_level

def test_handles_valid_headings():
    assert get_heading_level("# Introduction") == 1
    assert get_heading_level("## Installation") == 2
    assert get_heading_level("### Configuration") == 3
    assert get_heading_level("#### Usage") == 4
    assert get_heading_level("##### Help") == 5
    assert get_heading_level("###### Details") == 6
    assert get_heading_level("## Section #") == 2
