import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_age",
        "before_first_year",
        "exactly_one_year",
        "before_second_year",
        "exactly_two_years",
        "before_third_year",
        "cat_third_year_dog_second",
        "senior_ages"
    ]
)
def test_get_human_age_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected_cat_human_age",
    [
        (15, 1),
        (24, 2),
        (28, 3),
        (32, 4),
    ],
    ids=["cat_15_to_1", "cat_24_to_2", "cat_28_to_3", "cat_32_to_4"]
)
def test_cat_age_conversion(
    cat_age: int,
    expected_cat_human_age: int
) -> None:
    assert get_human_age(cat_age, 0)[0] == expected_cat_human_age


@pytest.mark.parametrize(
    "dog_age, expected_dog_human_age",
    [
        (15, 1),
        (24, 2),
        (29, 3),
        (34, 4),
    ],
    ids=["dog_15_to_1", "dog_24_to_2", "dog_29_to_3", "dog_34_to_4"]
)
def test_dog_age_conversion(
    dog_age: int,
    expected_dog_human_age: int
) -> None:
    assert get_human_age(0, dog_age)[1] == expected_dog_human_age
