import requests

# url = "http://127.0.0.1:8000/upload-csv"
#
# with open("../dal/agents_data.csv", "rb") as f:
#     files = {
#         "file": ("agents_data.csv", f, "text/csv")
#     }
#     response = requests.post(url,files=files)
# print(response.status_code)
# from fastapi import UploadFile
# import csv
# import io
# pip install python-multipart


data = {"query":"DELETE FROM  agents"}
url = "http://127.0.0.1:8000/free"

rec = requests.post(url=url,json=data)
print(rec.json())
