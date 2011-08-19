# -*- coding: utf-8 -*-

import os
import pytest
import transaction
import cStringIO
import zope.component
import dolmen.relations

from BTrees.OOBTree import OOBTree
from ZODB.DB import DB
from ZODB.DemoStorage import DemoStorage
from ZODB.interfaces import IConnection
from cromlech.configuration.utils import load_zcml
from cromlech.container.contained import Contained
from dolmen.container.components import BTreeContainer
from dolmen.relations import RelationCatalog, ICatalog, RelationsContainer
from dolmen.relations import values, any
from grokcore.component import testing
from persistent import Persistent, IPersistent
from zope import component
from zope.component import eventtesting
from zope.interface import Interface, implements, verify
from zope.intid import IntIds
from zope.intid.interfaces import IIntIds
from zope.keyreference.interfaces import IKeyReference
from zope.keyreference.persistent import KeyReferenceToPersistent
from zope.keyreference.persistent import connectionOfPersistent


class Mammoth(Contained, Persistent):
    """A test pachyderm.
    """
    def __repr__(self):
        return "<Mammoth %s>" % self.__name__


class Storage(object):

    def __init__(self):
        """Prepares for a functional test case.
        """
        # we prevent any craziness here
        transaction.abort()
        
        storage = DemoStorage("Demo Storage")
        self.db = DB(storage)
        self.connection = None

    def clean(self):
        """Cleans up after a functional test case.
        """
        transaction.abort()
        if self.connection:
            self.connection.close()
            self.connection = None
        self.db.close()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
        self.db.close()

    def open(self):
        if self.connection:
            self.close()
        self.connection = self.db.open()
        return self.connection.root()


def setup_test():
    eventtesting.setUp()
    load_zcml(os.path.join(
        os.path.dirname(dolmen.relations.__file__), 'configure.zcml'))
    sm = component.getGlobalSiteManager()
    sm.registerUtility(IntIds(), IIntIds)
    sm.registerAdapter(connectionOfPersistent, (IPersistent,), IConnection)
    sm.registerAdapter(KeyReferenceToPersistent, (IPersistent,), IKeyReference)
