from dependency_injector import containers, providers

from app.data.sources.database import Database
from app.data.sources.nsfw_detector import NsfwDetector
from app.commons.config import settings
from app.repositories.todo_repository import TodoRepository
from app.repositories.nsfw_repository import NsfwRepository
from app.api.v1.services.todo_service import TodoService
from app.api.v1.services.nsfw_service import NsfwService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.controllers.todo_controller",
            "app.api.v1.controllers.nsfw_controller",
        ]
    )

    # data sources
    db = providers.Singleton(Database, url=settings.DATABASE_URI_MAPPER)
    nsfw_detector = providers.Singleton(NsfwDetector)

    # repositories
    todo_repository = providers.Factory(TodoRepository, db=db.provided.session)
    nsfw_repository = providers.Factory(NsfwRepository, nsfw_detector=nsfw_detector)

    # services
    todo_service = providers.Factory(TodoService, repository=todo_repository)
    nsfw_service = providers.Factory(NsfwService, repository=nsfw_repository)
