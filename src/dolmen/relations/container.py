# -*- coding: utf-8 -*-

from BTrees.OOBTree import OOBTree
from cromlech.container.contained import Contained
from cromlech.container.constraints import checkObject
from zope.location.interfaces import IContained
from dolmen.relations import events, IRelationsContainer
from zope.event import notify
from zope.interface import implements, alsoProvides


class RelationsContainer(Contained, OOBTree):
    """A rough implementation of a relation storage.
    """
    implements(IRelationsContainer)

    def __setitem__(self, key, value):
        checkObject(self, key, value)
        value.__parent__ = self
        value.__name__ = key
        alsoProvides(value, IContained)
        OOBTree.__setitem__(self, key, value)
        notify(events.RelationAddedEvent(value))

    def __delitem__(self, key):
        relation = self.get(key, None)
        if relation is not None:
            # If the key doesn't exists, nothing should happens. This
            # case can be triggered if you set a subscribers to
            # IRelationTargetDeletedEvent that end-up somehow deleting
            # the relation
            notify(events.RelationDeletedEvent(self.get(key)))
            OOBTree.__delitem__(self, key)
        else:
            KeyError(key)
