from pdfjin_powerpoint_to_pdf.core import convert_pptx_to_pdf


def test_import():
    assert callable(convert_pptx_to_pdf)
