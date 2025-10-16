images ={"Img_01.png","Pic.jpeg","Avatar.mp4"}

for image in images.copy():
    if image.endswith(".png") or image.endswith(".jpeg"):
        images.discard(image)
        continue
print(images)