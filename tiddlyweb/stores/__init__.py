"""
The base Class and interface for Classes
use to get and put data into a storage
system.
"""

from tiddlyweb.store import StoreMethodNotImplemented


class StorageInterface(object):
    """
    A Store is a collection of methods that
    either store an object or retrieve an object.

    The interface is fairly simple: For the data
    entities that exist in the TiddlyWeb system there
    (optionally) exists <entity_put> and <entity>_get
    methods in each Store.

    There are also four supporting methods, list_recipes(),
    list_bags(), list_users(), and list_tiddler_revisions() that provide
    methods for presenting a collection.

    It is useful to understand the classes in the tiddlyweb.model
    package when implementing new StorageInterface classes.
    """

    def __init__(self, environ=None):
        """
        The WSGI environment is made available to the storage system
        so that decisions can be made based on things like the
        request IP. Care should be taken when using environ related
        data as the environment can change from when Store is
        instantiated to when it is actually used. Configuration
        information pulled from the store should only be used
        during the initialization phase.
        """
        if environ is None:
            environ = {}
        self.environ = environ

    def recipe_delete(self, recipe):
        """
        Remove the recipe from the store,
        with no impact on the tiddlers.
        """
        raise StoreMethodNotImplemented('this store does not handle deleting recipes')

    def recipe_get(self, recipe):
        """
        Get a recipe from the store,
        returning a populated recipe
        object.
        """
        raise StoreMethodNotImplemented('this store does not handle getting recipes')

    def recipe_put(self, recipe):
        """
        Put a recipe into the store.
        """
        raise StoreMethodNotImplemented('this store does not handle putting recipes')

    def bag_delete(self, bag):
        """
        Remove the bag from the store,
        including the tiddlers within
        the bag.
        """
        raise StoreMethodNotImplemented('this store does not handle deleting bags')

    def bag_get(self, bag):
        """
        Get a bag from the store,
        returning a populated  bag
        object.
        """
        raise StoreMethodNotImplemented('this store does not handle getting bags')

    def bag_put(self, recipe):
        """
        Put a bag into the store.
        """
        raise StoreMethodNotImplemented('this store does not handle putting bags')

    def tiddler_delete(self, tiddler):
        """
        Delete a tiddler from the store.
        """
        raise StoreMethodNotImplemented('this store does not handle deleting tiddlers')

    def tiddler_get(self, tiddler):
        """
        Get a tiddler from the store, returning a populated tiddler
        object. tiddler.creator and tiddler.created are based on
        the modifier and modified of the first revision of a tiddler.
        """
        raise StoreMethodNotImplemented('this store does not handle getting tiddlers')

    def tiddler_put(self, tiddler):
        """
        Put a tiddler into the store.
        """
        raise StoreMethodNotImplemented('this store does not handle putting tiddlers')

    def user_delete(self, user):
        """
        Delete a user from the store.
        """
        raise StoreMethodNotImplemented('this store does not handle deleting users')

    def user_get(self, user):
        """
        Get a user from the store,
        returning a populated user
        object.
        """
        raise StoreMethodNotImplemented('this store does not handle getting users')

    def user_put(self, user):
        """
        Put a user into the store.
        """
        raise StoreMethodNotImplemented('this store does not handle putting users')

    def list_recipes(self):
        """
        Retrieve a list of all recipe objects in the system.
        """
        raise StoreMethodNotImplemented('this store does not handle listing recipes')

    def list_bags(self):
        """
        Retrieve a list of all bag objects in the system.
        """
        raise StoreMethodNotImplemented('this store does not handle listing bags')

    def list_users(self):
        """
        Retrieve a list of all the user objects in the system.
        """
        raise StoreMethodNotImplemented('this store does not handle listing users')

    def list_tiddler_revisions(self, tiddler):
        """
        Retrieve a list of all the revision identifiers
        for one tiddler.
        """
        raise StoreMethodNotImplemented('this store does not handle listing tiddler revisions')

    def tiddler_written(self, tiddler):
        """
        Notify the system that a tiddler has been stored.
        This is done to cause search system to update or
        otherwise deal with new content.
        """
        pass

    def search(self, search_query):
        """
        Search the entire tiddler store for
        search_query.
        """
        raise StoreMethodNotImplemented('this store does not provide search')
