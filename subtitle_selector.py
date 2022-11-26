import ffmpeg 
import json

class SubtitleLanguage:
  def __init__(self, code, index):
    self.code = code
    self.index = index

  def __str__(self):
    return f"{self.code}({self.index})"

def main():

    probe = ffmpeg.probe("/home/mrdasilva/Plex/Ancient.Apocalypse.2022.S01.1080p.NF.WEB-DL.x265.10bit.HDR.DDP5.1-NPMS[rartv]/Ancient.Apocalypse.2022.S01E04.1080p.NF.WEB-DL.DDP5.1.HDR.HEVC-NPMS.mkv")
    
    languages = {}
    index = 0;

    for x in probe['streams']:
        if x['codec_type'] == "subtitle":
            languages[index] =  SubtitleLanguage (x['tags']['language'],x['index'])
            index += 1

    for lang in languages.values():
        print(lang)

if __name__ == "__main__":
    main()