import pytube

print("Welcome to Oblivion Ghoul's Youtube Video Downloader! Please choose an option below.")
print(
"""
1. Download 1 Youtube Video
2. Download Multiple Youtube Videos
"""
)
try:
    option = int(input())
except: 
    print('Not an int!')
else: 
    if (option == 1):
        try:
            url = input("Enter the URL: ")
            v = pytube.YouTube(url)
            stream = v.streams.get_by_itag(299)
            print("Downloading video...")
            stream.download()
            print("Download Complete!")
        except:
            print('Please Enter a Valid URL')
    elif (option == 2):
        try:
            videoList = []
            print("Enter the video URL. Enter 'STOP' to stop the process.")
            while True:
                url = input("")
                if url == 'STOP':
                    break
                videoList.append(url)

            for x, video in enumerate(videoList):
                v = pytube.YouTube(video)
                stream = v.streams.get_by_itag(299)
                print(f"Downloading video {x}...")
                stream.download()
                print("Download Complete!")
        except:
            print('Please Enter Valid URLs')
    else:
        print("Please enter a valid option.")