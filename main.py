import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
def send_to_slack(message):
    client.chat_postMessage(channel='#testchannel', text=message)

s=Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
urls = ['https://appfollow.io/featured/today#country=all&ext_id=1440385758',
        'https://appfollow.io/featured/today#country=all&ext_id=1202240058']
def main(urls):
    filename = ""
    for url in range(len(urls)):
        fileid = urls[url].split('=')[len(urls[url].split('='))-1]

        if (fileid == '1440385758'):
            filename = 'sandship'
        if (fileid == '1202240058'):
            filename = 'deeptown'
        driver.execute_script(f'window.open("{urls[url]}","_self")')
        driver.get(urls[url])
        time.sleep(15)
        elements = driver.find_elements(by=By.CLASS_NAME, value='aso-today-list__date')
        send_to_slack(f"last Featured for {filename} was in " + elements[-1].text)
    driver.close()

def read_txt_files(filename):
    with open(f'{filename}.txt') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    main(urls)

