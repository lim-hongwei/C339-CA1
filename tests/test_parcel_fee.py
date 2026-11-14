import pytest
from src.parcel_fee import delivery_fee


# Valid weights: 1 to 1000 g costs 500 cents, 1001 to 20000 g costs 1000 cents
@pytest.mark.parametrize(
    "weight_grams, expected_fee",
    [
        (1, 500),  # lower boundary of 500-cent band
        (500, 500),  # typical value in 500-cent band
        (1000, 500),  # upper boundary of 500-cent band
        (1001, 1000),  # lower boundary of 1000-cent band
        (5000, 1000),  # typical value in 1000-cent band
        (20000, 1000),  # upper boundary of 1000-cent band
    ],
)
def test_valid_weight_returns_correct_fee(weight_grams, expected_fee):
    # Arrange: weight_grams and expected_fee are provided by parametrize

    # Act
    result = delivery_fee(weight_grams)

    # Assert
    assert result == expected_fee


# Weights outside 1 to 20000 g must raise ValueError
@pytest.mark.parametrize(
    "weight_grams",
    [
        0,  # below the minimum weight
        20001,  # above the maximum weight
        -1,  # negative weight
    ],
)
def test_weight_outside_permitted_range_raises_value_error(weight_grams):
    # Arrange: weight_grams is provided by parametrize

    # Act and Assert
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)


# Weights that are not Python integers must raise TypeError
@pytest.mark.parametrize(
    "weight_grams",
    [
        1000.0,  # float
        "1000",  # string
        None,  # missing value
        True,  # boolean is not a valid integer
    ],
)
def test_invalid_weight_type_raises_type_error(weight_grams):
    # Arrange: weight_grams is provided by parametrize

    # Act and Assert
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)
