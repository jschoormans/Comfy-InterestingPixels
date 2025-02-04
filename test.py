#%%
import io
import requests
from PIL import Image

# Create a simple white image (100x100)
img = Image.new("RGB", (100, 100), color="white")
buf = io.BytesIO()
img.save(buf, format="PNG")
buf.seek(0)

# Endpoint URL
url = "https://us-central1-redecorely.cloudfunctions.net/upload-interesting-pixels"

# Send POST request with the image file
files = {'image': ('test.png', buf.getvalue(), 'image/png')}
response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response:", response.text)
