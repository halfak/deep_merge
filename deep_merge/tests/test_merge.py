from ..merge import merge


def test_default_behaviors():
    a = {'foo': 5}
    b = {'foo': False}
    assert merge(a, b) == {'foo': False}

    a = {'foo': 5}
    b = {'foo': 10}
    assert merge(a, b, merge_ints=lambda a, b, **kwargs: a+b) == {'foo': 15}

    a = {'foo': 5}
    b = {'bar': 10}
    assert merge(a, b) == {'foo': 5, 'bar': 10}


def test_big_merge():
    a = {
        'foo': {
            'bar': {
                'foo': 5,
                'bar': 7
            }
        },
        'l': [1, 5, 'foo']
    }
    b = {
        'foo': {
            'bar': {
                'foo': 6
            }
        },
        'bar': 5,
        's': "I'm a string",
        'l': [1, 2, 3],
        'herpa_derpa': 5
    }
    c = {
        'foo': {
            'bar': {
                'foobar': 10
            }
        },
        'herpa_derpa': None
    }
    expected = {
        'foo': {
            'bar': {
                'foo': 6,
                'bar': 7,
                'foobar': 10
            }
        },
        'bar': 5,
        's': "I'm a string",
        'l': [1, 5, 'foo', 1, 2, 3],
        'herpa_derpa': None
    }
    assert merge(a, b, c) == expected


def test_no_references():
    """
    Ensure that read-only parameters aren't being modified.
    """
    d1 = {}
    d2 = {"key1": {"key1a": "1"}, "key2": [3, 4]}
    d3 = {"key1": {"key1a": "2"}, "key2": [4, 5]}

    output = merge(d1, d2, d3)
    # Is correct.
    assert output == {"key1": {"key1a": "2"}, "key2": [3, 4, 4, 5]}
    # Destructive to parameter 1.
    assert d1 == {"key1": {"key1a": "2"}, "key2": [3, 4, 4, 5]}
    # Not destructive to parameter 2.
    assert d2 == {"key1": {"key1a": "1"}, "key2": [3, 4]}
