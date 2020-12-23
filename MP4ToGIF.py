from moviepy.editor import VideoFileClip

videoName = input("Enter the name of the video (Must be in the same directory and do not include extention name): ")
gifName = input("Enter the name of the new file: ")
frames = int(input("Enter the amount of frames you want (Less frames will take up less memory): "))
clip = VideoFileClip(videoName + ".mp4")
clip.write_gif(gifName + ".gif", fps=frames)