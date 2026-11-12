"""Unit tests for dialog_utils size formatting and reduction text."""

from ui.components.dialog_utils import format_size
from ui.i18n import t


def test_format_size_units():
    assert format_size(0) == "0 B"
    assert format_size(512) == "512 B"
    assert format_size(1536) == "1.5 KB"  # 1.5 * 1024
    assert format_size(5 * 1024 * 1024) == "5.00 MB"
    assert format_size(3 * 1024 * 1024 * 1024) == "3.00 GB"


def test_reduction_text_positive_and_negative():
    # Positive reduction (size decreased) should show + or no extra minus
    pos = t("log_reduction_stat", pct=35.2)
    assert "35.2%" in pos
    assert "--" not in pos

    # Negative (size increased) should show a single minus
    neg = t("log_reduction_stat", pct=-35.2)
    assert "-35.2%" in neg
    assert "--" not in neg
