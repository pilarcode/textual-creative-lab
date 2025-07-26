import plotext as plt
path = '../data/moonwalk.mp4'
plt.download(plt.test_video_url, path)
plt.play_video(path, from_youtube = True)
plt.delete_file(path)