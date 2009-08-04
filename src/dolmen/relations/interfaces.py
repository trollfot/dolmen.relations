# -*- coding: utf-8 -*-

from zope.schema import Int, TextLine, List
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from zope.container.interfaces import IContained, IBTreeContainer
from zope.container.constraints import contains, containers

_ = MessageFactory('dolmen.relation')


class IRelationSource(Interface):
    """Market interface.
    """

class IRelationTarget(Interface):
    """Market interface.
    """

class IContainedRelation(IContained):
    """A contained relation.
    """

class IRelationValue(Interface):
    """A simple relation One to One.
    """
    source_id = Int(
        title = _(u"source_intid", default=u"Intid of the source object"),
        required = True,
        )

    target_id = Int(
        title = _(u"target_intid", default=u"Intid of the target object"),
        required = True,
        )


class IRelations(IBTreeContainer):
    """A relation values storage.
    """
    contains(IContainedRelation)


class IStatefulRelationValue(IRelationValue):
    """A relation with a state.
    """
    state = TextLine(
        title = _(u"state", default=u"State of the relation"),
        required = True,
        default = u""
        )


class ITaggedRelationValue(IRelationValue):
    """A relation that handles tags.
    """
    tags = List(
        title = _(u"tags", default=u"Tags of the relation"),
        required = True,
        default = [],
        value_type = TextLine()
        )


__all__ = ["IRelationSource", "IRelationTarget",
           "IRelations", "IContainedRelation",
           "IRelationValue", "IStatefulRelationValue", "ITaggedRelationValue"]
