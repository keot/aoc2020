#!/usr/bin/env python3

import pytest

import binary_boarding


@pytest.fixture
def example_boarding_passes():
    return [
        {
            "specification": "FBFBBFFRLR",
            "row": 44,
            "column": 5,
            "seat_id": 357,
        },
        {
            "specification": "BFFFBBFRRR",
            "row": 70,
            "column": 7,
            "seat_id": 567,
        },
        {
            "specification": "FFFBBBFRRR",
            "row": 14,
            "column": 7,
            "seat_id": 119,
        },
        {
            "specification": "BBFFBBFRLL",
            "row": 102,
            "column": 4,
            "seat_id": 820,
        },
    ]


def test_example_boarding_passes(example_boarding_passes):
    for boarding_pass in example_boarding_passes:
        assert boarding_pass == binary_boarding.decode_boarding_pass(
            boarding_pass["specification"]
        )
