from dependency_injector import containers, providers

from app.data.sources.database import Database
from app.data.sources.nsfw_detector import NsfwDetector
from app.commons.config import settings
from app.repositories.nsfw_repository import NsfwRepository
from app.api.v1.services.nsfw_service import NsfwService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.controllers.nsfw_controller",
        ]
    )

    # data sources
    db = providers.Singleton(Database, url=settings.DATABASE_URI_MAPPER)
    nsfw_detector = providers.Singleton(NsfwDetector)

    # repositories
    nsfw_repository = providers.Factory(NsfwRepository, nsfw_detector=nsfw_detector)

    # services
    nsfw_service = providers.Factory(NsfwService, repository=nsfw_repository)
