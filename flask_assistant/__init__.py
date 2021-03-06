import logging

logger = logging.getLogger('flask_assistant')
logger.addHandler(logging.StreamHandler())
if logger.level == logging.NOTSET:
    logger.setLevel(logging.INFO)


from flask_assistant.core import (
    Assistant,
    context_manager,
    intent,
    request
)

from flask_assistant.response import ask, tell, event, build_item, permission
from flask_assistant.manager import Context

from api_ai.api import ApiAi
