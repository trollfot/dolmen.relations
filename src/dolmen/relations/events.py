# -*- coding: utf-8 -*-

from zope.component.interfaces import ObjectEvent, IObjectEvent
from zope.lifecycleevent.interfaces import (
    IObjectAddedEvent, IObjectRemovedEvent, IObjectModifiedEvent)
from zope.lifecycleevent import ObjectAddedEvent, ObjectRemovedEvent
from zope.interface import implements, Attribute


class IRelationAddedEvent(IObjectAddedEvent):
    """A relation has been added.
    """


class IRelationModifiedEvent(IObjectModifiedEvent):
    """A relation has been modified.
    """


class IRelationDeletedEvent(IObjectRemovedEvent):
    """A relation has been deleted.
    """


class IRelationSourceDeletedEvent(IObjectEvent):
    """The source of a relation has been deleted.
    """
    relation = Attribute(u"Relation")


class IRelationTargetDeletedEvent(IObjectEvent):
    """The target of a relation has been deleted.
    """
    relation = Attribute(u"Relation")


class RelationAddedEvent(ObjectAddedEvent):
    implements(IRelationAddedEvent)


class RelationModifiedEvent(ObjectEvent):
    implements(IRelationModifiedEvent)


class RelationDeletedEvent(ObjectRemovedEvent):
    implements(IRelationDeletedEvent)


class RelationSourceDeletedEvent(ObjectEvent):
    implements(IRelationSourceDeletedEvent)

    def __init__(self, object, relation):
        self.object = object
        self.relation = relation


class RelationTargetDeletedEvent(ObjectEvent):
    implements(IRelationTargetDeletedEvent)

    def __init__(self, object, relation):
        self.object = object
        self.relation = relation
