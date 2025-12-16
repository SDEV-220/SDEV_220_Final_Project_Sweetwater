from .base import *
from config.env import env

# IMPORTANT: Turn off debug for production!
DEBUG = env.bool('DEBUG', default=False)