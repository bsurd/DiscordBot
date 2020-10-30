import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    print('We are in debug')
    from pathlib import Path
    from dotenv import load_dotenv

    env_path = Path('.') / '.env_debug'
    load_dotenv(dotenv_path=env_path)
    from settings_files.dev import *
else:
    print('We are in production')
    from settings_files.prod import *

DEFAULT_USER_ROLE_NAME = 'SoftVisioner'
MODERATOR_ROLE_NAME = 'Moderator'
