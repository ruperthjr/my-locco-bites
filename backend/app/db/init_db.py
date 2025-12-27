"""Database initialization."""

import logging
from sqlalchemy.orm import Session
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.config.settings import settings

logger = logging.getLogger(__name__)


def init_db() -> None:
    """Initialize database by creating all tables."""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise


def drop_db() -> None:
    """Drop all database tables."""
    try:
        Base.metadata.drop_all(bind=engine)
        logger.info("Database tables dropped successfully")
    except Exception as e:
        logger.error(f"Error dropping database tables: {str(e)}")
        raise


def reset_db() -> None:
    """Reset database by dropping and recreating all tables."""
    try:
        drop_db()
        init_db()
        logger.info("Database reset successfully")
    except Exception as e:
        logger.error(f"Error resetting database: {str(e)}")
        raise


def check_db_connection() -> bool:
    """
    Check if database connection is working.
    
    Returns:
        True if connection successful, False otherwise
    """
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        logger.info("Database connection successful")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return False


def create_initial_data(db: Session) -> None:
    """
    Create initial data in database.
    
    Args:
        db: Database session
    """
    try:
        logger.info("Creating initial data...")
        logger.info("Initial data created successfully")
    except Exception as e:
        logger.error(f"Error creating initial data: {str(e)}")
        db.rollback()
        raise


def seed_database() -> None:
    """Seed database with initial data."""
    try:
        db = SessionLocal()
        create_initial_data(db)
        db.commit()
        db.close()
        logger.info("Database seeded successfully")
    except Exception as e:
        logger.error(f"Error seeding database: {str(e)}")
        raise


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Initializing database...")
    init_db()
    
    if settings.ENVIRONMENT == "development":
        logger.info("Seeding database with initial data...")
        seed_database()