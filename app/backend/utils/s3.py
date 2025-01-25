from PIL import Image
import io
import boto3
from botocore.config import Config

def upload_photo(file_obj, filename):
    # Using local storage instead of S3 to stay free
    img = Image.open(file_obj)
    img.thumbnail((800, 800))
    
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=85)
    
    # Save to local storage
    with open(f"static/uploads/{filename}", 'wb') as f:
        f.write(output.getvalue())
    
    return f"/static/uploads/{filename}"
