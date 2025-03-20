from db import mongo_db

counters = mongo_db.counters

def get_next_sequence(collection_name):
    """
    Increment and retrieve the next sequence value for the given collection.
    """
    result = counters.find_one_and_update(
        {"_id": collection_name},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=True
    )
    return result["sequence_value"]