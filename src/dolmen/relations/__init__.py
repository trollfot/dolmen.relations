try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)


from zc.relation.interfaces import ICatalog
from dolmen.relations.interfaces import *
from dolmen.relations.values import *
from dolmen.relations.container import Relations
from dolmen.relations.catalog import RelationCatalog
