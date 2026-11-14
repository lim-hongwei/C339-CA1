import pytest
from src.parcel_acceptance import is_parcel_accepted


# Accepted only when weight is 1 to 20000 g and length is 1 to 200 cm
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (1, 100),  # weight at lower limit
        (20000, 100),  # weight at upper limit
        (1000, 1),  # length at lower limit
        (1000, 200),  # length at upper limit
        (1000, 100),  # typical values within both limits
    ],
)
def test_parcel_within_limits_returns_true(weight_grams, length_cm):
    # Arrange: weight_grams and length_cm are provided by parametrize

    # Act
    result = is_parcel_accepted(weight_grams, length_cm)

    # Assert: "is True" checks for the actual Boolean True, not just a truthy value
    assert result is True


# A zero measurement or a measurement above a limit returns False
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (0, 100),  # zero weight
        (1000, 0),  # zero length
        (20001, 100),  # weight above limit
        (1000, 201),  # length above limit
    ],
)
def test_parcel_outside_limits_returns_false(weight_grams, length_cm):
    # Arrange: weight_grams and length_cm are provided by parametrize

    # Act
    result = is_parcel_accepted(weight_grams, length_cm)

    # Assert
    assert result is False


# Negative measurements must raise ValueError
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (-1, 100),  # negative weight
        (1000, -1),  # negative length
    ],
)
def test_negative_measurement_raises_value_error(weight_grams, length_cm):
    # Arrange: weight_grams and length_cm are provided by parametrize

    # Act and Assert
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)


# Measurements that are not Python integers must raise TypeError
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (1000.0, 100),  # float weight
        ("1000", 100),  # string weight
        (None, 100),  # missing weight
        (True, 100),  # boolean weight is not a valid integer
        (1000, 100.0),  # float length
        (1000, "100"),  # string length
        (1000, None),  # missing length
        (1000, False),  # boolean length is not a valid integer
    ],
)
def test_invalid_measurement_type_raises_type_error(weight_grams, length_cm):
    # Arrange: weight_grams and length_cm are provided by parametrize

    # Act and Assert
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)
