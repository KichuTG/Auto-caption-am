# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5398056049"))
API_ID = int(getenv("API_ID", "28714959"))
API_HASH = str(getenv("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "8032865598:AAGA9Zetpv7jkJyaPsHu07N2gykNYXRVbzs"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>{file_caption} \n\n Ask it on @Tgmoviespro1bot</b>",
    )
)
