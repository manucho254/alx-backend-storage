#!/usr/bin/env python3
""" module to list all documents in collection
"""

if __name__ == "__main__":
    from pymongo.collection import Collection

    def list_all(mongo_collection):
        """ lists all documents in a collection
            Args:
              mongo_collection: mongo collection
            Return:
                 list of documents
        """
        if not isinstance(mongo_collection, Collection):
            return []

        documents = dict(mongo_collection.find())
        if len(documents):
            return []

        return documents
