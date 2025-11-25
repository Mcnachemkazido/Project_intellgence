# import requests

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





# @app.post("/upload-csv")
# def upload_csv(file: UploadFile):
#     """
#     Endpoint that extracts and processes a CSV file from the request.
#     Uses Python's csv library to read and parse the CSV data.
#     """
    # Validate that the uploaded file is a CSV
    # if file.content_type != "text/csv":
    #      return {"error": "File must be a CSV"}
    #
    #
    # # Read file bytes
    # content = file.file.read().decode("utf-8")
    #
    # # Parse CSV
    # reader = csv.reader(io.StringIO(content))
    # header = next(reader)
    # rows = list(reader)
    #
    # for line in rows:
    #     print(line)
    #
    # return {
    #     "filename": file.filename,
    #     "content_type": file.content_type,
    #     "total_rows": len(rows),
    #     "columns": header,
    #     "data": rows[0:5],
    #     "message": f"Successfully processed CSV with {len(rows)} rows"
    # }