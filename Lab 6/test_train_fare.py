import pytest
from train_fare import base_fare, concession, tatkal_charge


# ---------------- BASE FARE TESTS ----------------

def test_sleeper_fare():
    assert base_fare("SL", 500) == 500


def test_ac3_fare():
    assert base_fare("3A", 500) == 1000


def test_ac2_fare():
    assert base_fare("2A", 500) == 1500


def test_first_ac_fare():
    assert base_fare("1A", 500) == 2500


def test_minimum_fare():
    assert base_fare("SL", 10) == 50


def test_unknown_class():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("CC", 500)


def test_zero_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)


def test_negative_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", -100)


# ---------------- CONCESSION TESTS ----------------

def test_tatkal_no_concession():
    assert concession(30, "M", True) == 0


def test_child_below_five():
    assert concession(4, "M", False) == 100


def test_child_age_five():
    assert concession(5, "M", False) == 50


def test_child_age_twelve():
    assert concession(12, "F", False) == 50


def test_adult_no_concession():
    assert concession(30, "M", False) == 0


def test_senior_male_concession():
    assert concession(60, "M", False) == 40


def test_senior_female_concession():
    assert concession(60, "F", False) == 50


def test_senior_above_sixty():
    assert concession(75, "M", False) == 40


def test_age_fifty_nine():
    assert concession(59, "F", False) == 0


# ---------------- TATKAL CHARGE TESTS ----------------

def test_sleeper_tatkal_minimum_charge():
    assert tatkal_charge("SL", 500) == 100


def test_sleeper_tatkal_middle_charge():
    assert tatkal_charge("SL", 2000) == 200


def test_sleeper_tatkal_maximum_charge():
    assert tatkal_charge("SL", 5000) == 400


def test_ac_tatkal_minimum_charge():
    assert tatkal_charge("3A", 100) == 100


def test_ac_tatkal_middle_charge():
    assert tatkal_charge("3A", 1000) == 300


def test_ac_tatkal_maximum_charge():
    assert tatkal_charge("3A", 2000) == 400
