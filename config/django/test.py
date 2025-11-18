from .base import *
from config.env import env

DEBUG = env.bool('DEBUG', default=True)