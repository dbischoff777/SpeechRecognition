import json
import requests

class NotionClient:

    def __init__(self, token, db_id) -> None:
        self.db_id = db_id
        
        self.heards = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-02-22"
        }

    def create_page(self, description, date, status):
        create_url = 'https://api.notion.com/v1/pages'

        data = {
        "parent": { "database_id": self.db_id },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": status
                        }
                    }
                ]
            }
        }}

        data = json.dumps(data)
        res = requests.post(create_url, headers=self.headers, data=data)
        print(res.status_code)
        return res