from loguru import logger
from app.data.sources.nsfw_detector import NsfwDetector


def test_should_classify_nsfw_from_image():
    # arrange
    image = "https://assets.karyakarsa.com/picture-64d4696b89205.jpg"
    nsfw_detector = NsfwDetector()

    # action
    result = nsfw_detector.classify(image)

    logger.info(result)

    # assert
    assert result == [
        {"classification": "drawings", "probability": 0.59213787317276},
        {"classification": "neutral", "probability": 0.39928144216537476},
        {"classification": "hentai", "probability": 0.006825175601989031},
        {"classification": "porn", "probability": 0.0010271375067532063},
        {"classification": "sexy", "probability": 0.0007283256272785366},
    ]
