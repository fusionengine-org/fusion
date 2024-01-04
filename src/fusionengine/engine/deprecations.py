import functools
import warnings
from fusionengine import __version__ 

def compare_versions(version1, version2):
    components1 = list(map(int, version1.split('.')))
    components2 = list(map(int, version2.split('.')))

    for c1, c2 in zip(components1, components2):
        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1

    return 0

def deprecated(version=None):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """
    def decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            if version is None or compare_versions(__version__, version) >= 0:
                warnings.simplefilter('always', DeprecationWarning)
                warnings.warn(f"Call to deprecated function {func.__name__}.", category=DeprecationWarning, stacklevel=2)
                warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)
        return new_func
    return decorator
