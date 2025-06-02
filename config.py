import os

API_ID = int(os.environ.get("API_ID", "20407127"))  

API_HASH = os.environ.get("API_HASH", "877e7db614293fb2d7c5e4caa79896f7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7863525389:AAF8sXeWW8fZ81xM3wyASEDXGu5SSdc8Qo0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 961916589))

LOG = -1002116155974

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "961916589").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


