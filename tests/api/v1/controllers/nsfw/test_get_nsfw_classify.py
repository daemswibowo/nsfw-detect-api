# GET /v1/nsfw/classify test
def test_should_get_nsfw_classify_successfully_when_client_hit_nsfw_classify_endpoint(
    client,
):
    # arrange
    image_url = "https://assets.karyakarsa.com/picture-64d4696b89205.jpg"

    # action
    response = client.get(f"/v1/nsfw/classify?image_url={image_url}")

    # assert
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "image_url": image_url,
            "is_nsfw": False,
            "classification": "drawings",
            "predictions": [
                {"classification": "drawings", "probability": 0.59213787317276},
                {"classification": "neutral", "probability": 0.39928144216537476},
                {"classification": "hentai", "probability": 0.006825175601989031},
                {"classification": "porn", "probability": 0.0010271375067532063},
                {"classification": "sexy", "probability": 0.0007283256272785366},
            ],
        }
    }


# should return 422 when image_url is not provided
def test_should_return_422_when_image_url_is_not_provided(client):
    # action
    response = client.get(f"/v1/nsfw/classify")

    # assert
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "image_url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
