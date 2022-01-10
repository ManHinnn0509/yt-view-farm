import re
from typing import Union

from pytube import YouTube, Playlist
from pytube.streams import Stream

def __intExtract(s: str):
    # return int(re.sub("[^0-9]", "", s))
    return int(re.sub("\D", "", s))

def getMaxResolutionStream(video: YouTube) -> Union[Stream, None]:
    """
        Returns the best quality stream of the video.
        None will be returned when no match found.
    """
    # This is actually a Json and we can know what's the maximum resolution of the video via it
    # maxResolution = video.vid_info["playerConfig"]["decodeQualityConfig"]["maximumVideoDecodeVerticalResolution"]

    try:
        # Filter out video streams only
        streams = video.streams
        videoStreams = set(streams) - set(streams.filter(only_audio=True))

        best = -1
        bestStream = None

        # Returns the correct stream
        for s in videoStreams:
            res = __intExtract(s.resolution)
            if (res > best):
                best = res
                bestStream = s
        
        return bestStream
    except Exception as e:
        return None

def getMaxQualityAudioStream(video: YouTube) -> Union[Stream, None]:
    """
        Returns the best quality audio stream.
        None will be returned if nothing were found.
    """
    try:
        audioStreams = video.streams.filter(only_audio=True)

        bestStream = None
        best = -1
        # Find the best quality audio stream
        for s in audioStreams:
            # Convert the abr (quality) into int using regex
            # See: https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python
            quality = __intExtract(s.abr)
            if (quality > best):
                best = quality
                bestStream = s
        
        return bestStream
    except Exception as e:
        return None

def downloadLogging(stream, chunk, bytes_remaining):
    """
        Just a logging fucntion (callback function?) for downloading streams.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100

    s = f"Downloading ... {percentage:.1f}%"
    print(s)

def downloadComplete(stream, file_path):
    # Keep this function simple first
    print("Done!")