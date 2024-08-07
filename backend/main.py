from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

# Set up the Chrome driver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://it.pracuj.pl/praca/warszawa;wp?rd=30&cc=5016%2C5015&et=17&tc=0%2C3&ws=0&wm=hybrid%2Chome-office&its=frontend")

time.sleep(5)

job_offers = driver.find_elements(By.CSS_SELECTOR, "div[data-test='default-offer']")

# Extract the relevant information from each job offer
job_data = []
for offer in job_offers:
    # Extract title
    try:
        title = offer.find_element(By.CSS_SELECTOR, "h2[data-test='offer-title']").text
    except:
        title = None

    try:
        technologies = [tech.text for tech in offer.find_elements(By.CSS_SELECTOR, "span[data-test='technologies-item']")]
    except:
        technologies = []

    job_data.append({
        "title": title,
        "technologies": technologies
    })

with open("job_offers.json", "w", encoding='utf-8') as f:
    json.dump(job_data, f, ensure_ascii=False, indent=4)

driver.quit()
