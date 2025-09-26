import os
from dotenv import load_dotenv

def setup_env():
    load_dotenv()
    os.environ['USER_AGENT'] = os.getenv('USER_AGENT')
    return os.getenv('GOOGLE_API_KEY')