import plotext as plt
path = '../data/cat.png'
# Download a test image and save the image in the path
plt.download(plt.test_image_url, path)
# Plot the image
plt.image_plot(path)
# Add a title
plt.title("A very Cute Panda")
# show the image
plt.show()
#plt.delete_file(path)