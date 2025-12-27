"""WSGI configuration for Gunicorn deployment."""

import os
import sys
from pathlib import Path

root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

from app.main import app

application = app