"""Teste les fonctions de nastran_utils."""

import pytest

from app.core.adapters.nastran_adapter import split_by_8


@pytest.mark.parametrize(
    "input_line, result_expected",
    [
        (
            "GRID     2000000        -0.03      0.0  0.0\n",
            ["GRID", "2000000", "", "-0.03", "0.0", "0.0"],
        ),
        (
            "GRID    4               0.655   -0.549880.01147\n",
            ["GRID", "4", "", "0.655", "-0.54988", "0.01147"],
        ),
        (
            "GRID    3               0.655   -0.54988-0.01147\n",
            ["GRID", "3", "", "0.655", "-0.54988", "-0.01147"],
        ),
    ],
)
def test_split_by_8(input_line, result_expected):
    """Teste la fonction split_by_8."""

    result_to_test = split_by_8(input_line)

    assert result_to_test == result_expected
