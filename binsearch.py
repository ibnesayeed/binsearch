def _compare(key, target, **kw):
    """Return 0 if match, 1 if the key is lexicographically greater than the target, -1 otherwise"""
    pass


def _binsearch(fh, key, **kw):
    """Find any match using binary search, raise an exception if not found"""
    pass


def _dig_first(fh, key, **kw):
    """Find the first match after finding any match"""
    pass


def _dig_last(fh, key, **kw):
    """Find the last match after finding any match"""
    pass


def find(fh, key, **kw):
    """Return any matching line using binary search, None if not found"""
    pass


def find_first(fh, key, **kw):
    """Return the first matching line using binary search, None if not found"""
    pass


def find_last(fh, key, **kw):
    """Return the last matching line using binary search, None if not found"""
    pass


def find_all(fh, key, **kw):
    """Return an interator over all the matching lines"""
    pass
