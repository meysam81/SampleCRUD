import os

from medium.app import create_app
from medium.config import (
    ProductionConfig,
    DevelopmentConfig,
    TestingConfig,
)

choices = {getattr(obj, 'ENV'): obj for obj in [
    ProductionConfig, DevelopmentConfig, TestingConfig]}


app = create_app(choices[os.getenv('ENV', DevelopmentConfig.ENV)])
