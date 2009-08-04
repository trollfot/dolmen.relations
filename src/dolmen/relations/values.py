# -*- coding: utf-8 -*-

from persistent import Persistent
from zope.component import getUtility
from zope.interface import implements
from zope.app.intid.interfaces import IIntIds
from zope.container.contained import Contained
from zope.interface import implements, providedBy, Declaration
from dolmen.relations.interfaces import *


class RelationValue(Contained, Persistent):
    implements(IRelationValue)
    
    def __init__(self, target_id, source_id):
        self.target_id = target_id
        self.source_id = source_id
        
    @property
    def source(self):
        intids = getUtility(IIntIds)
        return intids.queryObject(self.source_id)

    @property
    def target(self):
        intids = getUtility(IIntIds)
        return intids.queryObject(self.target_id)


class StatefulRelationValue(RelationValue):
    implements(IStatefulRelationValue)

    def __init__(self, target_id, source_id, state=u""):
        RelationValue.__init__(self, target_id, source_id)
        self.state = state


class TaggedRelationValue(RelationValue):
    implements(ITaggedRelationValue)

    def __init__(self, target_id, source_id, tags=[]):
        RelationValue.__init__(self, target_id, source_id)
        self.tags = tags


__all__ = ['RelationValue',
           'StatefulRelationValue',
           'TaggedRelationValue']
