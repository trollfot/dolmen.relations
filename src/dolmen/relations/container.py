# -*- coding: utf-8 -*-

from persistent import Persistent
from BTrees.OOBTree import OOBTree
from BTrees.Length import Length

from zope.event import notify
from zope.interface import implements
from zope.cachedescriptors.property import Lazy
from zope.app.container.constraints import checkObject

from dolmen.relations import events
from dolmen.relations import IRelations


class Relations(Persistent):
    """A rough implementation of a relation storage.
    """
    implements(IRelations)

    def __init__(self):
        self._data = OOBTree()
        self.__len = Length()

    def __contains__(self, key):
        return key in self._data

    @Lazy
    def _Relations__len(self):
        l = Length()
        ol = len(self._data)
        if ol > 0:
            l.change(ol)
        self._p_changed = True
        return l

    def __len__(self):
        return self.__len()

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        '''See interface `IReadContainer`'''
        return self._data[key]

    def get(self, key, default=None):
        '''See interface `IReadContainer`'''
        return self._data.get(key, default)
        
    def __setitem__(self, key, value):
        checkObject(self, key, value)
        l = self.__len
        value.__parent__ = self
        value.__name__ = key
        self._data[key] = value
        l.change(1)
        notify(events.RelationAddedEvent(value))

    def __delitem__(self, key):
        notify(events.RelationDeletedEvent(self.get(key)))
        l = self.__len
        del self._data[key]
        l.change(-1)

    has_key = __contains__

    def items(self, key=None):
        return self._data.items(key)

    def keys(self, key=None):
        return self._data.keys(key)

    def values(self, key=None):
        return self._data.values(key)
