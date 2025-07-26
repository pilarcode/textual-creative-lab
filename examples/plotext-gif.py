import plotext as plt
path = '../data/homer.gif'
plt.download(plt.test_gif_url, path)
plt.play_gif(path)
#plt.delete_file(path)