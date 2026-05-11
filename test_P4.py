import pytest
import sys

sys.path.append(r"c:\Users\jaime\OneDrive\Escritorio\Python")  # Ensure the path to Algoritmica is added
from Algoritmica.P4 import Candidato_iterativo


@pytest.mark.parametrize(
    "data, expected",
    [
        ([1, 1, 2, 2, 2, 2], 2),
        ([1, 2, 3, 4, 5, 6], None),
        ([1, 1, 2, 2], None),
        ([1, 1, 1, 2, 2], 1),
        ([1], 1),
        ([3, 3, 4, 4, 4, 4, 4], 4),
        ([5, 5, 5, 5, 1, 2, 3], 5),
        ([7, 8, 8, 8, 8, 8, 9, 9], 8),
        ([12, 12, 12, 12, 12, 13, 13, 13], 12),
    ],
    ids=(
        "majority_element_1",
        "no_majority_element_1",
        "even_elements_1",
        "odd_elements_1",
        "single_element_1",
        "majority_element_2",
        "majority_element_3",
        "majority_element_4",
        "majority_element_5",
    ),
)
def test_candidato_itertativo(data, expected) -> None:
    assert Candidato_iterativo(data, 0, len(data) - 1) == expected, (
        f"Expected {expected} but got {Candidato_iterativo(data, 0, len(data) - 1)}"
    )


if __name__ == "__main__":
    pytest.main([__file__])
