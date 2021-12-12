import time
import traceback

from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config import *

def main():

    # Testing
    url = "https://www.youtube.com/watch?v=JmGgN6WVyZ4"

    url = input("Video URL: ")

    # Use pytube to check if the input url is a valid YouTube video link
    # + Checks if its publicly viewable
    # Then we can use the "length" attrible in the YouTube class to determine how often to refresh the page

    video = None
    try:
        video = YouTube(url)

    except Exception as e:
        tb = traceback.format_exc()
        s = f"Exception caught with follow traceback:\n\n{tb}"
        
        print(s)
        return

    # Required since selenium's v4 update
    service = Service(CHROME_DRIVER_PATH)
    
    options = webdriver.ChromeOptions()
    options.add_extension(EXT_UBLOCK_ORIGIN_PATH)   # Add needed extenstions
    options.add_argument("--mute-audio")            # Add needed arguments (Mute)

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    # Wait for driver to load
    time.sleep(1)

    driver.get(url)
    time.sleep(10)      # Wait for page to load

    # Find the play button and click it to make the video starts playing
    playButton = driver.find_element_by_class_name('ytp-large-play-button')
    playButton.click()

    # Refresh rate could be fixed / the video's length
    # refreshRate = video.length
    refreshRate = 30
    
    # Add 5 seconds buffer to it
    refreshRate += 5

    # Auto refresh any N seconds
    while (True):
        print("Press CTRL+C to exit...")
        time.sleep(refreshRate)
        driver.refresh()

    # --- Unreachable ---
    # Keep the driver opened
    # ignored = input("Press any key to exit...")
    # driver.close()
    
if (__name__ == "__main__"):
    main()