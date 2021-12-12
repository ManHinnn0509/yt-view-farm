import time
import traceback

from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config import *

def main():

    # Testing
    url = "https://www.youtube.com/watch?v=8SbUC-UaAxE"

    url = input("Video URL: ")

    # Use pytube to check if the input url is a valid YouTube video link
    # + Checks if its publicly viewable
    # Then we can use the "length" attrible in the YouTube class to determine how often to refresh the page

    videoLen = getVideoLen(url)
    # Unable to get video's info, just exit the program in here
    if (videoLen == -1):
        print("Invalid video URL!")
        return

    # Required since selenium's v4 update
    service = Service(CHROME_DRIVER_PATH)
    
    # Init ChromeDriver's options
    options = webdriver.ChromeOptions()
    options.add_extension(EXT_UBLOCK_ORIGIN_PATH)   # Add needed extenstions
    options.add_argument("--mute-audio")            # Add needed arguments (Mute)

    # Init ChromeDriver
    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    # Wait for driver to load
    time.sleep(1)

    driver.get(url)
    time.sleep(5)      # Wait for page to load

    # Find the play button and click it to make the video starts playing
    playButton = driver.find_element_by_class_name('ytp-large-play-button')
    playButton.click()

    # Refresh rate could be fixed / the video's length
    # refreshRate = videoLen
    refreshRate = 30
    
    # Add 3 seconds buffer to it
    refreshRate += 3

    # Auto refresh after eveny N seconds
    while (True):
        try:
            print("Press CTRL+C to exit...")
            time.sleep(refreshRate)
            driver.refresh()
        
        except KeyboardInterrupt:
            print("CTRL+C detected. Now exiting program...")
            break

    driver.close()
    print("--- End of Program ---")
    
def getVideoLen(url: str):
    try:
        video = YouTube(url)
        return video.length
    
    # Unable to get video's info
    # -1 will be returned
    except Exception as e:
        # tb = traceback.format_exc()
        # s = f"Exception caught with follow traceback:\n\n{tb}"
        # print(s)

        return -1

if (__name__ == "__main__"):
    main()