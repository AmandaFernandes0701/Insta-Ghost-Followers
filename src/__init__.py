from .config import APP_NAME, VERSION
from .auth import login_to_instagram
from .analyzer import analyze_profile
from .utils import console, Panel, Status, Table

# Controle de imports
__all__ = ["login_to_instagram", "analyze_profile", "console", "Panel", "Status", "APP_NAME", "VERSION"]