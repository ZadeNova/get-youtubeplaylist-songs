import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Change path to your chrome driver path.
s = Service(r"C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=s, options=options)

# Make sure youtube playlist is set to public or unlisted. No private youtube playlists.


url = input("Type youtube playlist link here: ")
# Go to your youtube playlist and copy the url and paste it when prompted.

# Scrolling function
def scroll(numberofsongs):
    Variable = math.ceil(numberofsongs / 100)
    for i in range(Variable):
        elem.send_keys(Keys.END)  # Code to scroll down the page
        time.sleep(2)

try:
    driver.get(url)
    driver.implicitly_wait(3)

    elem = driver.find_element(By.TAG_NAME, 'html')

    # Get number of songs in your playlist
    TotalNoOfSongs = driver.find_element(By.XPATH, "//*[@id='stats']/yt-formatted-string[1]/span[1]").text
    first_number = int(TotalNoOfSongs[0])
    noOfsongs = int(TotalNoOfSongs)

    scroll(noOfsongs)  # Execute scrolling function
    time.sleep(3)

    TitleOfSongs = driver.find_elements(By.XPATH, '//*[@id="contents"]/ytd-playlist-video-renderer')
    for songs in TitleOfSongs:
        listofsongs = songs.find_elements(By.XPATH, '//*[@id="video-title"]')

    for songname in listofsongs:
        print(songname.text)

    driver.close()
except Exception as exc:
    print(exc)
