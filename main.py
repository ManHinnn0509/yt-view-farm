import farm
import download

from pytube import YouTube

from util.yt_utils import downloadLogging, downloadComplete

def main():
    print("(1) View farm")
    print("(2) Download highest resolution (Video + audio)")
    print("(3) Download highest quality (Video)")
    print("(4) Download highest quality (Audio)")

    try:
        option = input(">> ")
        option = int(option)

        if (option < 1 or option > 4):
            raise Exception

    except:
        print("Invalid input. Now returning...")
        return
    
    if (option == 1):
        try:
            farm.main()
        except:
            pass

        print("--- End of Program ---")
        return
    
    # See if the input URL is valid
    try:
        url = input("Video url: ")
        v = YouTube(url, on_progress_callback=downloadLogging, on_complete_callback=downloadComplete)

        # For testing if the input url is valid video URL
        _ = v.title
        _ = v.length
    except:
        print("Invalid input. Now returning...")
        return

    if (option == 2):
        output = download.downloadHighestResolution(v)
    
    elif (option == 3):
        output = download.downloadBestResolutionVideo(v)
    
    elif (option == 4):
        output = download.downloadBestQualityAudio(v)
    
    else:
        print("Invalid input. Now returning...")
        return
    
    output = output.replace("\\", "/")
    print(f"Output file path: {output}")

    print("--- End of Program ---")

if (__name__ == "__main__"):
    main()