import re
import unittest2

__all__ = ('describe', 'should')


def get_name_from_description(description):
    return 'test_%s' % (re.sub('[^a-zA-Z0-9_]', description, '').replace(' ', '_'),)


def describe(obj):
    """
    >>> @describe(MyClass)
    >>> class Test:
    >>>     # ...
    """
    def wrapped(cls):
        cls.__bases__.insert(0, unittest2.TestCase)
        cls.__describes__ = obj
        # TODO: we need to handle functions/etc here to get unique names
        cls.__name__ = '%s_TestCase' % (obj.__name__,)
        return cls
    return wrapped


def should(description):
    """
    >>> @should('set the message')
    >>> def test(self):
    >>>     # ...
    """
    def wrapped(func):
        func.__should__ = description
        func.__name__ = get_name_from_description(description)
        return func
    return wrapped
