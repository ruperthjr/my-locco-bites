"""Database migration utilities."""

import logging
from typing import List, Optional
from alembic import command
from alembic.config import Config
from pathlib import Path

logger = logging.getLogger(__name__)


def get_alembic_config() -> Config:
    """
    Get Alembic configuration.
    
    Returns:
        Alembic Config object
    """
    alembic_ini_path = Path(__file__).parent.parent.parent / "alembic.ini"
    config = Config(str(alembic_ini_path))
    return config


def create_migration(message: str, autogenerate: bool = True) -> None:
    """
    Create a new migration.
    
    Args:
        message: Migration message/description
        autogenerate: Whether to autogenerate migration from models
    """
    try:
        config = get_alembic_config()
        command.revision(
            config,
            message=message,
            autogenerate=autogenerate
        )
        logger.info(f"Migration created: {message}")
    except Exception as e:
        logger.error(f"Error creating migration: {str(e)}")
        raise


def upgrade_database(revision: str = "head") -> None:
    """
    Upgrade database to a specific revision.
    
    Args:
        revision: Target revision (default: 'head' for latest)
    """
    try:
        config = get_alembic_config()
        command.upgrade(config, revision)
        logger.info(f"Database upgraded to: {revision}")
    except Exception as e:
        logger.error(f"Error upgrading database: {str(e)}")
        raise


def downgrade_database(revision: str = "-1") -> None:
    """
    Downgrade database to a specific revision.
    
    Args:
        revision: Target revision (default: '-1' for previous)
    """
    try:
        config = get_alembic_config()
        command.downgrade(config, revision)
        logger.info(f"Database downgraded to: {revision}")
    except Exception as e:
        logger.error(f"Error downgrading database: {str(e)}")
        raise


def get_current_revision() -> Optional[str]:
    """
    Get current database revision.
    
    Returns:
        Current revision identifier or None
    """
    try:
        config = get_alembic_config()
        command.current(config)
        return None
    except Exception as e:
        logger.error(f"Error getting current revision: {str(e)}")
        return None


def get_migration_history() -> List[str]:
    """
    Get migration history.
    
    Returns:
        List of migration revisions
    """
    try:
        config = get_alembic_config()
        command.history(config)
        return []
    except Exception as e:
        logger.error(f"Error getting migration history: {str(e)}")
        return []


def stamp_database(revision: str = "head") -> None:
    """
    Stamp database with a specific revision without running migrations.
    
    Args:
        revision: Revision to stamp with
    """
    try:
        config = get_alembic_config()
        command.stamp(config, revision)
        logger.info(f"Database stamped with revision: {revision}")
    except Exception as e:
        logger.error(f"Error stamping database: {str(e)}")
        raise


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    upgrade_database()