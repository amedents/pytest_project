import pytest

from parsers import names_parser, price_threshold_parser


# Test 1
def test_names_parser():
    """Tests names_parser function."""
    assert names_parser('example_1') == ['Pizza', 'Sushi', 'Burger', 'Pad Thai']


# Test 2
@pytest.mark.parametrize(
    "file_name, threshold, expected",
    [
        ('example_1', '8.99', [{'id': 1, 'name': 'Pizza', 'category': 'Italian', 'price': 12.99},
                               {'id': 2, 'name': 'Sushi', 'category': 'Japanese', 'price': 24.99},
                               {'id': 3, 'name': 'Burger', 'category': 'American', 'price': 8.99},
                               {'id': 4, 'name': 'Pad Thai', 'category': 'Thai', 'price': 14.99}]),
        ('example_1.json', 24.98, [{'id': 2, 'name': 'Sushi', 'category': 'Japanese', 'price': 24.99}]),
        ('example_1.json', 25, []),
        ('example_1.son', 25, None)
    ]
)
def test_threshold_parser(file_name, threshold, expected):
    """Tests price_threshold_parser function."""
    assert price_threshold_parser(threshold, file_name) == expected
