from nsfw_detector import predict
import requests
import tempfile
import os
import imghdr


class NsfwDetector:
    def __init__(self):
        self.model = predict.load_model(
            "app/data/tensorflow_models/nsfw_mobilenet2.224x224.h5"
        )

    def _load_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Invalid image URL or unable to fetch image")

        try:
            image_data = response.content

            # Determine the image format from content-type using imghdr
            image_format = imghdr.what(None, h=image_data)

            if not image_format:
                raise ValueError("Invalid image format")

            # Create a temporary file to save the image
            temp_image = tempfile.NamedTemporaryFile(
                suffix="." + image_format, delete=False
            )
            temp_image_path = temp_image.name

            with open(temp_image_path, "wb") as f:
                f.write(image_data)

            return temp_image_path
        except Exception as e:
            raise ValueError("Error loading image: " + str(e))

    def classify(self, image_url):
        try:
            image_path = self._load_image_from_url(image_url)
        except ValueError as e:
            raise ValueError(f"Error loading image from URL: {e}")

        try:
            result = predict.classify(self.model, image_path)[image_path]

            # transform result to list of {classification: key, probability: value}
            result = [
                {"classification": key, "probability": value}
                for key, value in result.items()
            ]

            # sort result by probability desc
            result = sorted(result, key=lambda x: x["probability"], reverse=True)

            return result
        finally:
            # Delete the temporary image file
            os.remove(image_path)
