from fastapi import APIRouter, Depends
from app.schemas.nsfw_schema import NsfwClassifyResponse
from dependency_injector.wiring import Provide, inject
from app.commons.di import Container
from app.api.v1.services.nsfw_service import NsfwService
from app.commons.exceptions import ValidationError

router = APIRouter(prefix="/nsfw", tags=["nsfw"])


@router.get(
    "/classify",
    response_model=NsfwClassifyResponse,
    response_description="Classify NSFW image",
)
@inject
async def get_classify_nsfw_image(
    image_url: str, service: NsfwService = Depends(Provide[Container.nsfw_service])
):
    # raise validation error if image_url is empty
    if not image_url:
        raise ValidationError(detail="image_url is required")

    result = service.classify(image_url)

    return {"data": result}
