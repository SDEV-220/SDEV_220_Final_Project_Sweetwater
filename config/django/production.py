from .base import *
from config.env import env

# Try env.read_env(os.path.join(BASE_DIR, '.env')) before everything else

# IMPORTANT: Turn off debug for production!
DEBUG = env.bool('DEBUG', default=False)