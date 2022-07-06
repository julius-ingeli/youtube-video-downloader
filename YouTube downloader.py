
from pytube import YouTube
import os
import platform

#getting login
def getPlatform():
    user = os.getlogin()

    windir = windir = "C:/Users/" + user + "/Desktop"
    windir = os.path.normpath(windir)

    lindir = "/home/" + user + "/Desktop/"
    #changing default dir to desktop
    osType = (platform.system())
    if osType == "Windows":
        os.chdir(windir)
    if osType == "Linux":
        os.chdir(lindir)


def loop():
    while True:
        try:
            yt = YouTube(str(input("URL: \n>>")))
        except(BaseException):
            print("Wrong URL format. Try again.")
            continue

        print("Download as: \n1.MP4\n2.MP3")
        a = input(">>")
        match a:
            case "1":
                video = yt.streams.filter().get_highest_resolution()
                fileext = ".mp4"
            case "2":
                video = yt.streams.filter(only_audio=True).first()
                fileext = ".mp3"
            case _:
                print("Invalid selection.")
                continue


        print("Enter destination for download:")
        destination = str(input(">> ")) or "."


        out_file = video.download(output_path=destination)

        base,ext = os.path.splitext(out_file)
        new_file = base + fileext
        try:
            os.rename(out_file, new_file)
        except(FileExistsError):
            print("File already exists within this directory.\nDo you want to download another video or close the program?(Y/N)\n>>")
            b = input()
            b.lower()
            if b == "y":
                continue
            if b == "n":
                "Exiting..."
                break
            


        print(yt.title, "by", yt.author , "downloaded successfully.")
        print("Video is saved in the directory:",str(new_file) )
        
        b = input("Download another video?(Y/N)\n>>")
        b.lower()
        if b == "y":
            continue
        if b == "n":
            "Exiting..."
            break
 
    
if __name__ == "__main__":
    try:
        getPlatform()
        loop()
    except(KeyboardInterrupt):
        exit()