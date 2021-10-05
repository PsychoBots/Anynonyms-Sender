import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values
    API_ID = 2698821
    API_HASH = "4af625c75eb9e72e1b228411b0c7cd42"
    BOT_TOKEN = "2019628061:AAFFyvV2T5w1qr-LUv59F9qlW5eteeojHWM"
