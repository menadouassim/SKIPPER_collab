import zipfile
import os
zip_path = "Training_database_float16.zip"

extraction_path = "Training_database_float16/"
os.makedirs(extraction_path, exist_ok=True)
with zipfile.ZipFile(zip_path, "r") as zip_object:
  zip_object.extractall(extraction_path)