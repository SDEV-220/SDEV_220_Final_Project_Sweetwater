from .base import *
from config.env import env

# Important to see debug messages in local development.
DEBUG = env.bool('DEBUG', default=True)