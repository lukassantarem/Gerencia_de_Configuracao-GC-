import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from temperature_converter import (
    fahrenheit_to_celsius,
    celsius_to_fahrenheit
)

def test_fahrenheit_to_celsius_boiling():
    assert fahrenheit_to_celsius(212) == 100.0

def test_fahrenheit_to_celsius_freezing():
    assert fahrenheit_to_celsius(32) == 10.0

def test_celsius_to_fahrenheit_body_temp():
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)

def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32.0
