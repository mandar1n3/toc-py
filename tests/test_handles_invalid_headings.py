from toc_py.utils import get_heading_level

def test_handles_invalid_headings():
    assert get_heading_level("####### Invalid") is None
    assert get_heading_level("#No space") is None
    assert get_heading_level("") is None
    assert get_heading_level("This is a text") is None
    assert get_heading_level("###") is None
    assert get_heading_level(" # Introduction") is None
    assert get_heading_level("#") is None
    assert get_heading_level("# ") is None
