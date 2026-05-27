"""Tests for the Patient model."""

from inflammation.models import Patient
from numpy.testing import npt

def test_create_patient():

    name = 'Alice'
    weight = 68
    height = 1.65
    p = Patient(name=name, weight=weight, height=height)

    assert p.name == name
    assert p.weight == weight
    assert p.height == height


def test_compute_bmi():
    name = 'maria'
    weight =60
    height = 1.6
    maria = Patient(name=name, weight=weight, height=height)
   # use assert_almost_equal from the numpt.testing to compare the computed BMI with the expected value of 23.4375, allowing for a small numerical tolerance.
    expected_bmi = 23.4375
    bmi_maria = maria.get_body_mass_index()
    npt.assert_almost_equal(bmi_maria, expected_bmi, decimal=5)
    