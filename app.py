import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

# Import the list of PDF URLs
# Maybe TODO extract from activity report? DB also works well
from pdf_urls import pdf_urls


# Path to ChromeDriver (assuming it's in the same directory as this script)
# TODO make an env variable so chromedrive can live anywhere
chrome_driver_path = os.path.join(
    os.getcwd(), "chromedriver.exe"
)  # Make sure chromedriver mathces your Chrome version!

# Set up Chrome options
chrome_options = Options()

# Configure Chrome to automatically download PDF files instead of opening them
download_dir = os.path.join(os.getcwd(), "downloads")
prefs = {
    "download.default_directory": download_dir,  # Directory to save the PDFs
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,  # Bypass the PDF viewer and download the file
}

# add prefs from above
chrome_options.add_experimental_option("prefs", prefs)


# Set up the Chrome WebDriver service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Clear all cookies before navigating to the login page
driver.delete_all_cookies()

# Navigate to the login page
driver.get("http://csr.opensesame.com/login")

# Wait  to manually log in
input("Please log in manually, then press Enter to continue...")


# Create download directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Initialize the counter for downloaded certificates so comapre against activity report, DB or where you got them from.
downloaded_count = 0

# Navigate to each PDF URL to download the file
for pdf_url in pdf_urls:
    print(f"Downloading: {pdf_url}")
    driver.get(pdf_url)  # This will trigger the download
    # time.sleep(2)  # Wait for 5 seconds to ensure the download completes
    downloaded_count += 1

# Print the number of downloaded certificates
print(f"Total certificates downloaded: {downloaded_count}")

# Before logout, clear browser cache for all time
print("Clearing browser cache for all time...")
driver.get(
    "chrome://settings/clearBrowserData"
)  # Navigate to Chrome's Clear Browsing Data page
time.sleep(2)

# Simulate the process of clearing the cache using Selenium
# Selenium will need to interact with the "Clear data" button in the settings
actions = webdriver.ActionChains(driver)
actions.send_keys(
    Keys.TAB * 3
)  # Move to the 'Time range' dropdown (assuming it's at the right position)
actions.send_keys(
    Keys.DOWN
)  # Select 'All time' (you may need to adjust if it's different)
actions.send_keys(Keys.TAB * 4)  # Move to the 'Clear data' button
actions.send_keys(Keys.ENTER)  # Hit 'Enter' to confirm clearing data
actions.perform()

# Give the browser time to clear the data
time.sleep(5)

# Close the browser window after all downloads are complete
driver.quit()
