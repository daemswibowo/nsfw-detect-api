from ..data.sources.nsfw_detector import NsfwDetector
from app.commons.exceptions import BadRequestError


class NsfwRepository:
    def __init__(self, nsfw_detector: NsfwDetector):
        self._nsfw_detector = nsfw_detector

    def detectFromImageUrl(self, image_url: str):
        try:
            result = self._nsfw_detector.classify(image_url)

            is_nsfw: bool = False

            if result[0]["classification"] in ["sexy", "hentai", "porn"]:
                is_nsfw = True

            return {
                "image_url": image_url,
                "is_nsfw": is_nsfw,
                "classification": result[0]["classification"],
                "predictions": result,
            }
        except Exception as e:
            raise BadRequestError(detail=str(e))
