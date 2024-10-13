🚀 Selenium PDF Downloader
Automate the process of logging into a website, downloading multiple PDF files, and clearing browser cache with Selenium and Chrome WebDriver.


✨ Features
✅ Automated Login: Navigate to the login page and pause for manual login.
📂 Bulk PDF Downloading: Download multiple PDFs from a predefined list of URLs.
⚙️ Auto-Configuration: Chrome is pre-configured to download PDFs without opening them in the browser.
🧹 Clear Browser Cache: Automatically clear Chrome's cache for "All Time" after completing the downloads.
🚀 Quickstart
1. Requirements
Python 3.x
Chrome Browser (ensure that the Chrome version matches ChromeDriver)
ChromeDriver
2. Install Dependencies
First, install the required Python package:

bash
Copy code
pip install selenium
3. Set Up ChromeDriver
Download ChromeDriver for your specific version of Chrome.
Place chromedriver.exe in the same directory as this script (or adjust the script to point to its location).
4. Configure PDF URLs
Create a file called pdf_urls.py in the same directory as the script. Inside pdf_urls.py, list the URLs of the PDFs you want to download like this:

python
Copy code
pdf_urls = [
    "https://csr.opensesame.com/completion_certificate/your_first_pdf_url",
    "https://csr.opensesame.com/completion_certificate/your_second_pdf_url",
    # Add more URLs as needed
]
5. Run the Script
Once everything is set up, run the following command in your terminal:

bash
Copy code
python selenium_pdf_downloader.py
Login Prompt: The script will navigate to the login page and pause. You need to log in manually and then press Enter in the terminal to continue the process.
Download Directory: PDFs will be saved to a folder called downloads/ in the project root. This folder is automatically created if it doesn’t exist.
🛠 Project Details
Code Structure
Chrome Options: The script is pre-configured to automatically download PDFs without triggering the Chrome PDF viewer.
Manual Login: The script pauses and waits for you to manually log into the website before proceeding to download the PDFs.
Clearing Cache: After downloading all the PDFs, the script simulates keypresses to clear the browser cache for "All Time."
Example Configuration in pdf_urls.py:
python
Copy code
pdf_urls = [
    "https://csr.opensesame.com/completion_certificate/example_pdf_url_1",
    "https://csr.opensesame.com/completion_certificate/example_pdf_url_2"
]
Clearing Browser Cache
The script will automatically navigate to chrome://settings/clearBrowserData and simulate key presses to clear cache:

Time Range: Clears cache for "All Time"
Automatic Interaction: Simulates interactions using Keys from Selenium to execute the "Clear Data" action.
⚠️ Troubleshooting
ChromeDriver Version Mismatch
If you encounter issues related to ChromeDriver, ensure your ChromeDriver version matches your Chrome browser version. Check your Chrome version by navigating to chrome://settings/help, and download the corresponding ChromeDriver version.

PDF Download Delays
If the PDFs are large or you have a slow connection, you might need to increase the wait time in the script. Adjust the following line to increase the delay between downloads:

python
Copy code
time.sleep(5)  # Increase this value if downloads take longer
Selenium Errors
Ensure you have installed the latest version of selenium and are using the correct ChromeDriver version. You can check if Selenium is installed using:

bash
Copy code
pip show selenium
