import os
import os.path
import pathlib
import time
import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

ua = UserAgent()


def collect_data_daily():
    data_daily = []
    date_daily = []

    r = requests.get(
        url='http://eetk.ru/78-2/2953-2/3115-2/',
        headers={'user-agent': f'{ua.random}'})

    soup = BeautifulSoup(r.text, "lxml")
    changes = soup.find_all("article", class_="post-3115 page type-page status-publish hentry")
    changes_names = changes

    for change in changes:
        data_daily += [link.get("href") for link in change.find_all("a")]
    for changes_name in changes_names:
        date_daily += [link.text for link in changes_name.find_all("a")]

    with open("texts/changes.txt", "w") as file:
        for item in data_daily:
            print(item, file=file)
    with open("texts/changes_names.txt", "w") as file:
        for item in date_daily:
            print(item, file=file)

    download_file(data_daily, date_daily)


def download_file(ids, names):
    check_file = []
    counter = -1
    for i in range(len(names)):
        check_file.append(os.path.exists(f'pdfs/{ids[i].rpartition("/")[-1]}.pdf'))
    if all(check_file):
        print('vse norm')
        return

    path = "/home/ubuntu/eetk/downloads/"
    glob_path = pathlib.Path("/home/ubuntu/eetk/downloads/")

    profile = webdriver.FirefoxOptions()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", path)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    driver = webdriver.Firefox(profile)

    for id in ids:
        counter += 1
        if 'cloud.mail.ru' in id:
            try:
                driver.get(f'{id}')
                driver.find_element(By.XPATH, '//div [@data-qa-id="download"]').click()
                time.sleep(2)
                for i, path in enumerate(glob_path.glob('*.pdf')):
                    new_name = id.rpartition('/')[-1] + '.pdf'
                    path.rename(f'pdfs/{new_name}')
            except:
                driver.quit()

        else:
            response = requests.get(id)
            with open(file=f'pdfs/{names[counter]}.pdf', mode='wb') as file:
                file.write(response.content)

    files = glob_path.glob('*.pdf')
    for f in files:
        os.remove(f)


def main():
    collect_data_daily()


if __name__ == '__main__':
    main()
