from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import TimeoutException
import csv

# Set up the Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use raw string to specify the path
service = Service(executable_path=r'C:\Users\Lyndon Crasto\Documents\Python\Python Projects\Web_Scraper\chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = "https://www.linkedin.com/jobs/search?keywords=Production%20Manager&location=New%20York%2C%20New%20York%2C%20United%20States&geoId=102571732&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    driver.get(url)

    # Increase the wait time to 30 seconds
    wait = WebDriverWait(driver, 30)
    try:
        job_listings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-search-card")))  # Updated class name
    except TimeoutException as e:
        print("TimeoutException: Job listings did not load in time or the CSS selector is incorrect.")
        driver.quit()
        raise e

    print("Number of job listings found:", len(job_listings))

    # Extract information from each job listing
    jobs = []
    for job in job_listings:
        try:
            job_title = job.find_element(By.CLASS_NAME, "base-search-card__title").text  # Updated class name
        except:
            job_title = "N/A"
        try:
            company = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text  # Updated class name
        except:
            company = "N/A"
        try:
            location = job.find_element(By.CLASS_NAME, "job-search-card__location").text  # Updated class name
        except:
            location = "N/A"
        try:
            posted_date = job.find_element(By.CLASS_NAME, "job-search-card__listdate").text  # Updated class name
        except:
            posted_date = "N/A"

        jobs.append({
            "Job Title": job_title,
            "Company": company,
            "Location": location,
            "Posted Date": posted_date
        })

    # Save job listings to a CSV file
    with open("linkedin_job_listings.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Job Title", "Company", "Location", "Posted Date"])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)

    print("Job listings saved to 'linkedin_job_listings.csv'")

finally:
    driver.quit()
