from app.repositories.nsfw_repository import NsfwRepository


class NsfwService:
    def __init__(self, repository: NsfwRepository):
        self._repository: NsfwRepository = repository

    def classify(self, image_url: str):
        return self._repository.detectFromImageUrl(image_url)
