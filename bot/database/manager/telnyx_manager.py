import json
from bot.utils.filenames import database
from bot.database.manager import telnyx_data

def update(api_key = None, from_number = None):
    if api_key is None:
        telnyx_data.api_key = api_key
        telnyx_data.data['api_key'] = api_key
    else:
        telnyx_data.data['api_key'] = telnyx_data.api_key
    
    if from_number is None:
        telnyx_data.from_number = from_number
        telnyx_data.data['from_number'] = from_number
    else:
        telnyx_data.data['from_number'] = telnyx_data.from_number

    with open(database.telnyx, "w", encoding="utf-8") as _file:
        json.dump(telnyx_data.data, _file)
