from .base_schema import WebResponse
from pydantic import BaseModel


class NsfwPrediction(BaseModel):
    classification: str
    probability: float


class NsfwClassification(BaseModel):
    image_url: str
    is_nsfw: bool
    classification: str
    predictions: list[NsfwPrediction]


class NsfwClassifyResponse(WebResponse):
    data: NsfwClassification
