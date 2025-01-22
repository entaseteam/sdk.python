"""Environment configuration for Entase SDK"""

class Environment:
    """Environment configuration class"""
    def __init__(self):
        self.API_URL = 'https://api.entase.com/v2/'
        self.DEBUG_MODE = False

# Global environment instance
env = Environment()

# For backwards compatibility
API_URL = env.API_URL
DEBUG_MODE = env.DEBUG_MODE 