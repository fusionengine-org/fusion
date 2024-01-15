import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        return encoded_image.decode("utf-8")


image_path = "src/fusionengine/debugfiles/fe.png"
base64_image = image_to_base64(image_path)

print(base64_image)
