import json
from bot.utils.filenames import database


with open(database.telnyx, "r", encoding="utf-8") as _file:
    data = json.load(_file)

api_key = data['api_key']
from_number = data['from_number']
