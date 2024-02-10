import base64
import fusionengine


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        return encoded_image.decode("utf-8")


base64_image = image_to_base64(fusionengine.DEBUGIMAGE)

print(base64_image)
