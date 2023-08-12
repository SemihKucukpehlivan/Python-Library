
from PIL import Image


image_path_list = ["dog-1.jpg","dog-2.jpg","dog-3.jpg"]

image_list = [Image.open(file) for file in image_path_list]

image_list[0].save(
    "animation.gif",
    save_all=True,
    append_images = image_list[1:],
    duration = 1000,
    loop=0
)