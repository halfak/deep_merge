from ..merge import merge


def test_default_behaviors():
    a = {'foo': 5}
    b = {'foo': False}
    assert merge(a, b) == {'foo': False}

    a = {'foo': 5}
    b = {'foo': 10}
    assert merge(a, b, merge_ints=lambda a, b, **kwargs: a+b) == {'foo': 15}


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
