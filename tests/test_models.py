"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import daily_mean
from inflammation.models import daily_max
from inflammation.models import daily_min
from inflammation.models import daily_mean


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0], [0, 0], [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2], [3, 4], [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max_integers():
    """Test that max function works for an array of positive integers."""

    test_input = np.array([[1, -2], [3, 4], [5, 6]])
    test_result = np.array([5, 6])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


# daily-mean test
def test_daily_mean():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2], [3, 4], [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_min_integers():
    """Test that min function works for an array of positive integers."""

    test_input = np.array([[1, -2], [3, 4], [5, 6]])
    test_result = np.array([1, -2])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_max_string():
    """Test the max function with an array of strings."""
    with pytest.raises(TypeError):
        error_expected = daily_max(["hello", "there", "world"])


@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
    ],
)
def test_daily_mean(test_input, test_result):
    """Test that mean function works both for zeros and integers."""

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


# parametrize daily_max test
@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
    ],
)
def test_daily_max(test_input, test_result):
    """Test that max function works both for zeros and integers."""

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[0, 1, 2], [0, 3, 4]], [0, 1, 2]),  # array containing zeros
        ([[3, 3, 3], [3, 3, 3], [3, 3, 3]], [3, 3, 3]),  # all values the same
    ],
)
def test_daily_min(test_input, test_result):
    """Test that min function works for an array of positive and negative integers."""
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_max_empty_array():
    """Test that daily_max raises ValueError when given an empty array."""
    with pytest.raises(ValueError):
        daily_max([])


def test_daily_max_nan_propagation():
    data = np.array([[1, np.nan], [3, 4]])
    result = daily_max(data)
    assert np.isnan(result[1])  # documents current behavior
