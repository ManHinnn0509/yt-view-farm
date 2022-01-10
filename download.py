from pytube import YouTube
from util.yt_utils import getMaxQualityAudioStream, getMaxResolutionStream

def downloadHighestResolution(v: YouTube):
    try:
        output = v.streams.get_highest_resolution().download()
        return output

    except:
        return None

def downloadBestResolutionVideo(v: YouTube):
    s = getMaxResolutionStream(v)
    if (s == None):
        return None
    
    try:
        output = s.download()
        return output

    except:
        return None

def downloadBestQualityAudio(v: YouTube):
    s = getMaxQualityAudioStream(v)
    if (s == None):
        return None
    
    try:
        output = s.download()
        return output

    except:
        return None