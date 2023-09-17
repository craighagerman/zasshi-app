import json
import os

from dev.data_path import DevData

def load_channel_list(channel_id):
    path = os.path.join(DevData().dev_data_dir(), "channel_list.json")
    d = json.loads(open(path).read())
    data = d.get(channel_id, None)
    item_keys_to_return = {"title", "xmlUrl"}    
    
    if data:
      items = [{k: item[k] for k in item_keys_to_return} for item in data["items"]]
      print(f"Loaded {len(items)} rows for channel id: {channel_id}")
      data["items"] = items
      return data
    return {"Error": "Key not found"}



def load_channels(path, channel_id):
    # path = os.path.join(DevData().dev_data_dir(), "channel_list.json")
    d = json.loads(open(path).read())
    data = d.get(channel_id, None)
    item_keys_to_return = {"title", "xmlUrl"}    
    
    if data:
      items = [{k: item[k] for k in item_keys_to_return} for item in data["items"]]
      print(f"Loaded {len(items)} rows for channel id: {channel_id}")
      data["items"] = items
      return data
    return {"Error": "Key not found"}

