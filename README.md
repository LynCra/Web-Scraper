# LinkedIn Job Scraper

This project is a Python-based web scraper designed to extract job listings from LinkedIn. It uses `BeautifulSoup` and `Selenium` to automate the process of navigating the website and collecting job data based on specified search criteria.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automates the process of searching for jobs on LinkedIn.
- Extracts job titles, companies, locations, and other relevant details.
- Saves the scraped data into a CSV file.
- Supports customizable search criteria such as job title, location, and filters.

## Requirements

- Python 3.x
- `Selenium` for web browser automation
- `BeautifulSoup` for parsing HTML content
- `pandas` for data manipulation and CSV export

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/LynCra/LynCra.github.io.git
    cd LynCra.github.io/projects/linkedin-job-scraper
    ```

2. **Install Dependencies:**
    Make sure you have `pip` installed. Then, run:
    ```sh
    pip install -r requirements.txt
    ```

3. **WebDriver:**
    - Download the WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/), [GeckoDriver](https://github.com/mozilla/geckodriver) for Firefox).
    - Ensure the WebDriver executable is in your PATH or specify its location in the script.

## Usage

1. **Configure the Scraper:**
   - Open the `scraper.py` file.
   - Modify the search criteria in the script as needed (e.g., job title, location).

2. **Run the Scraper:**
    ```sh
    python scraper.py
    ```

3. **Output:**
   - The scraped job data will be saved in a CSV file named `linkedin_jobs.csv` in the same directory.

## Project Structure

```plaintext
linkedin-job-scraper/
├── scraper.py          # The main script for scraping LinkedIn jobs
├── requirements.txt    # List of Python dependencies
├── README.md           # Project documentation
└── example_output.csv  # Example output of the scraper



### Additional Steps

1. **Adding Example Output:**
   - Include an `example_output.csv` file in your project directory to show users what the output looks like.

2. **Ensuring WebDriver Path:**
   - If you don't want users to manually add the WebDriver to their PATH, you can add instructions on how to specify the WebDriver path in the script.

By following this `README.md` template, you'll provide clear instructions and documentation for anyone looking to use or contribute to your LinkedIn job scraper project.
