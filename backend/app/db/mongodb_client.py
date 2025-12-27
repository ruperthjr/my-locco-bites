"""MongoDB client for document storage."""

import logging
from typing import Any, Dict, List, Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from pymongo import ReturnDocument
from app.config.settings import settings

logger = logging.getLogger(__name__)

mongodb_client: Optional[AsyncIOMotorClient] = None
mongodb_db: Optional[AsyncIOMotorDatabase] = None


async def init_mongodb() -> AsyncIOMotorDatabase:
    """
    Initialize MongoDB connection.
    
    Returns:
        MongoDB database instance
    """
    global mongodb_client, mongodb_db
    try:
        mongodb_client = AsyncIOMotorClient(
            settings.MONGODB_URL,
            maxPoolSize=settings.MONGODB_MAX_POOL_SIZE,
            minPoolSize=settings.MONGODB_MIN_POOL_SIZE,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=5000
        )
        
        await mongodb_client.admin.command('ping')
        mongodb_db = mongodb_client[settings.MONGODB_DB_NAME]
        logger.info(f"MongoDB connection established to database: {settings.MONGODB_DB_NAME}")
        return mongodb_db
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {str(e)}")
        raise


async def close_mongodb() -> None:
    """Close MongoDB connection."""
    global mongodb_client
    if mongodb_client:
        try:
            mongodb_client.close()
            logger.info("MongoDB connection closed")
        except Exception as e:
            logger.error(f"Error closing MongoDB connection: {str(e)}")


async def get_mongodb() -> AsyncIOMotorDatabase:
    """
    Get MongoDB database instance.
    
    Returns:
        MongoDB database
    """
    global mongodb_db
    if mongodb_db is None:
        mongodb_db = await init_mongodb()
    return mongodb_db


async def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    """
    Get a MongoDB collection.
    
    Args:
        collection_name: Name of the collection
    
    Returns:
        MongoDB collection
    """
    db = await get_mongodb()
    return db[collection_name]


async def insert_one(
    collection_name: str,
    document: Dict[str, Any]
) -> Optional[str]:
    """
    Insert a single document into a collection.
    
    Args:
        collection_name: Name of the collection
        document: Document to insert
    
    Returns:
        Inserted document ID or None if failed
    """
    try:
        collection = await get_collection(collection_name)
        result = await collection.insert_one(document)
        return str(result.inserted_id)
    except Exception as e:
        logger.error(f"Error inserting document into {collection_name}: {str(e)}")
        return None


async def insert_many(
    collection_name: str,
    documents: List[Dict[str, Any]]
) -> List[str]:
    """
    Insert multiple documents into a collection.
    
    Args:
        collection_name: Name of the collection
        documents: List of documents to insert
    
    Returns:
        List of inserted document IDs
    """
    try:
        collection = await get_collection(collection_name)
        result = await collection.insert_many(documents)
        return [str(id) for id in result.inserted_ids]
    except Exception as e:
        logger.error(f"Error inserting documents into {collection_name}: {str(e)}")
        return []


async def find_one(
    collection_name: str,
    query: Dict[str, Any],
    projection: Optional[Dict[str, Any]] = None
) -> Optional[Dict[str, Any]]:
    """
    Find a single document in a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter
        projection: Fields to include/exclude
    
    Returns:
        Document or None if not found
    """
    try:
        collection = await get_collection(collection_name)
        return await collection.find_one(query, projection)
    except Exception as e:
        logger.error(f"Error finding document in {collection_name}: {str(e)}")
        return None


async def find_many(
    collection_name: str,
    query: Dict[str, Any],
    projection: Optional[Dict[str, Any]] = None,
    limit: int = 100,
    skip: int = 0,
    sort: Optional[List[tuple]] = None
) -> List[Dict[str, Any]]:
    """
    Find multiple documents in a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter
        projection: Fields to include/exclude
        limit: Maximum number of documents to return
        skip: Number of documents to skip
        sort: Sort specification
    
    Returns:
        List of documents
    """
    try:
        collection = await get_collection(collection_name)
        cursor = collection.find(query, projection).limit(limit).skip(skip)
        
        if sort:
            cursor = cursor.sort(sort)
        
        return await cursor.to_list(length=limit)
    except Exception as e:
        logger.error(f"Error finding documents in {collection_name}: {str(e)}")
        return []


async def update_one(
    collection_name: str,
    query: Dict[str, Any],
    update: Dict[str, Any],
    upsert: bool = False
) -> bool:
    """
    Update a single document in a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter
        update: Update operations
        upsert: Whether to insert if document doesn't exist
    
    Returns:
        True if successful, False otherwise
    """
    try:
        collection = await get_collection(collection_name)
        result = await collection.update_one(query, update, upsert=upsert)
        return result.modified_count > 0 or (upsert and result.upserted_id is not None)
    except Exception as e:
        logger.error(f"Error updating document in {collection_name}: {str(e)}")
        return False


async def update_many(
    collection_name: str,
    query: Dict[str, Any],
    update: Dict[str, Any]
) -> int:
    """
    Update multiple documents in a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter
        update: Update operations
    
    Returns:
        Number of documents modified
    """
    try:
        collection = await get_collection(collection_name)
        result = await collection.update_many(query, update)
        return result.modified_count
    except Exception as e:
        logger.error(f"Error updating documents in {collection_name}: {str(e)}")
        return 0


async def delete_one(
    collection_name: str,
    query: Dict[str, Any]
) -> bool:
    """
    Delete a single document from a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter
    
    Returns:
        True if successful, False otherwise
    """
    try:
        collection = await get_collection(collection_name)
        result = await collection.delete_one(query)
        return result.deleted_count > 0
    except Exception as e:
        logger.error(f"Error deleting document from {collection_name}: {str(e)}")
        return False


async def delete_many(
    collection_name: str,
    query: Dict[str, Any]
) -> int:
    """
    Delete multiple documents from a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter
    
    Returns:
        Number of documents deleted
    """
    try:
        collection = await get_collection(collection_name)
        result = await collection.delete_many(query)
        return result.deleted_count
    except Exception as e:
        logger.error(f"Error deleting documents from {collection_name}: {str(e)}")
        return 0


async def count_documents(
    collection_name: str,
    query: Optional[Dict[str, Any]] = None
) -> int:
    """
    Count documents in a collection.
    
    Args:
        collection_name: Name of the collection
        query: Query filter (optional)
    
    Returns:
        Number of documents matching query
    """
    try:
        collection = await get_collection(collection_name)
        return await collection.count_documents(query or {})
    except Exception as e:
        logger.error(f"Error counting documents in {collection_name}: {str(e)}")
        return 0


async def aggregate(
    collection_name: str,
    pipeline: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Perform aggregation on a collection.
    
    Args:
        collection_name: Name of the collection
        pipeline: Aggregation pipeline
    
    Returns:
        Aggregation results
    """
    try:
        collection = await get_collection(collection_name)
        cursor = collection.aggregate(pipeline)
        return await cursor.to_list(length=None)
    except Exception as e:
        logger.error(f"Error performing aggregation on {collection_name}: {str(e)}")
        return []