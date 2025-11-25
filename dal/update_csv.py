import csv
import io

def extract_csv(file):

    # Validate that the uploaded file is a CSV
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}


    # Read file bytes
    content = file.file.read().decode("utf-8")

    # Parse CSV
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)

    return rows
