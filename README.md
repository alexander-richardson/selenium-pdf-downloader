# 🚀 Selenium PDF Downloader

Easily automate the process of logging into a website, downloading multiple PDF files, and clearing browser cache with Selenium and Chrome WebDriver.


## ✨ Features

- ✅ **Automated Login**: Navigate to the login page and pause for manual login.
- 📂 **Bulk PDF Downloading**: Download multiple PDFs from a predefined list of URLs.
- ⚙️ **Auto-Configuration**: Chrome is pre-configured to download PDFs without opening them in the browser.
- 🧹 **Clear Browser Cache**: Automatically clear Chrome's cache for "All Time" after completing the downloads.

## 🚀 Quickstart

### 1. Requirements

- Python 3.x
- [Chrome Browser](https://www.google.com/chrome/) (ensure that the Chrome version matches ChromeDriver)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### 2. Install Dependencies

First, install the required Python package:

```bash
pip install selenium
```
3. Set Up ChromeDriver
Download ChromeDriver for your specific version of Chrome.
Place chromedriver.exe in the same directory as this script (or adjust the script to point to its location).

4. Configure PDF URLs
Inside pdf_urls.py, list the URLs of the PDFs you want to download like this:

```bash
pdf_urls = [
    "https://csr.opensesame.com/completion_certificate/your_first_pdf_url",
    "https://csr.opensesame.com/completion_certificate/your_second_pdf_url",
    # Add more URLs as needed
]
```

5. Run the Script
Once everything is set up, run the following command in your terminal:
```python app.py```
- **Login Prompt**: The script will navigate to the login page and pause. You need to log in manually and then press `Enter` in the terminal to continue the process.
- **Download Directory**: PDFs will be saved to a folder called `downloads/` in the project root. This folder is automatically created if it doesn’t exist.

## ⚠️ Troubleshooting

## Drupal Login Error
The first times this run I will usuall encounter the following drupal error {"message":"An exception occurred login user: Error on login user in Drupal: Admin user alexander.richardson@opensesame.com attempted to log into cached site."}. 

Clearing the cache and running again will resolve this.

### ChromeDriver Version Mismatch

If you encounter issues related to ChromeDriver, ensure your ChromeDriver version matches your Chrome browser version. Check your Chrome version by navigating to `chrome://settings/help`, and download the corresponding [ChromeDriver version](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### PDF Download Delays

If the PDFs are large or you have a slow connection, you might need to increase the wait time in the script. Adjust the following line to increase the delay between downloads:

```python
time.sleep(5)  # Increase this value if downloads take longer





