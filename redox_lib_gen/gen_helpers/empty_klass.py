# -*- coding: utf-8 -*-

__all__ = ["EMPTY_KLASS_PROPERTY", "EMPTY_KLASS_DEF"]


class EmptyKlassProperty:
    """For comparing KlassPropertySignatureInfo objects with nothing.

    DO NOT instantiate! EMPTY_KLASS_PROPERTY should be the only instance.
    """

    def __call__(self):
        return self

    def __or__(self, other):
        # Try to take an or from the other direction, but only if other isn't also an
        # EmptyKlassProperty, in which case just return self.
        return self if isinstance(other, self.__class__) else other | self


EMPTY_KLASS_PROPERTY = EmptyKlassProperty()


class EmptyKlassDef:
    """For comparing KlassDefinition objects with nothing.

    DO NOT instantiate! EMPTY_KLASS_DEF should be the only instance.
    """

    def __call__(self):
        return self

    def __or__(self, other):
        return other | self


EMPTY_KLASS_DEF = EmptyKlassDef()


# There should only ever be one instance of these
del EmptyKlassProperty
del EmptyKlassDef
