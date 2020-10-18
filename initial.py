import json
import os
import datetime
from datetime import datetime
import csv

data = json.load(open("message_1.json", encoding="utf-8"))
for message in data["messages"]:
    try:
        date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
        sender = message["sender_name"]
        content = message["content"]
        try:
            call_duration = message["call_duration"]
            with open("output2.csv", 'a') as csv_file:
                try:
                    
                    writer = csv.writer(csv_file)
                    writer.writerow([date,sender,content, call_duration])
                except:
                    pass
        except:
            pass
    except KeyError:
        pass
