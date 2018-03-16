# Deep Merge

This library contains a simple utility for deep-merging dictionaries and the
data structures they contain.

* **Installation:** ``pip install deep_merge``
* **Documentation:** https://pythonhosted.org/deep_merge
* **Repositiory:** https://github.com/halfak/deep_merge
* **License:** MIT

## Example

    >>> import deep_merge
    >>>
    >>> print(deep_merge.merge({'a': {'b': 10}}, {'a': {'c': 5}}))
    {'a': {'b': 10, 'c': 5}}


## Author
* Aaron Halfaker -- https://github.com/halfak
