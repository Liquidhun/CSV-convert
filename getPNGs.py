import os
import requests
import io
from PIL import Image
from io import StringIO

# Define the URLs and output file paths
urls = ["http://localhost/kokeny/index.php?act=getWorkflow&filter=KAT-KEPZO-001", "http://localhost/kokeny/index.php?act=getWorkflow&filter=KAT-KEPZO-002"]
output_paths = ["output/image1.png", "output/image2.png"]

# Loop through each URL and save the image to the output path
for url, output_path in zip(urls, output_paths):
    # Make a request to the URL and get the image data
    response = requests.get(url)
    response_text = response.text

    # Load the image from the data and save it as a PNG file
    with open(output_path, "w") as f:
        f.write(response_text)