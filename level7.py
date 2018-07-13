from PIL import Image
image = Image.open("oxygen.png")

data = [chr(image.getpixel((i, 43))[0]) for i in range(0,609,7)]
print("".join(data))

msg = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(i) for i in msg]))