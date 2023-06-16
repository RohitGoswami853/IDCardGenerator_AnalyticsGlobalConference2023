from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os

# Path to the HTML folder and JPG folder
html_folder = 'html'
jpg_folder = 'jpg'

# Set up the Selenium web driver with headless option
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Loop over the HTML files in the HTML folder
for filename in os.listdir(html_folder):
    if filename.endswith('.html'):
        html_path = os.path.join(html_folder, filename)
        jpg_path = os.path.join(jpg_folder, filename[:-5] + '.jpg')

        # Load the HTML file in the web driver and take a screenshot
        driver.get('file:///' + os.path.abspath(html_path))
        driver.save_screenshot(jpg_path)

        # Convert the screenshot to JPG using Pillow
        with Image.open(jpg_path) as img:
            img.convert('RGB').save(jpg_path)

# Quit the web driver
driver.quit()
