import os
from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    """
    BaseConfigクラス
    """

    SECRET_KEY = os.environ["SECRET_KEY"]
    WTF_CSRF_SECRET_KEY = os.environ["WTF_CSRF_SECRET_KEY"]


class LocalConfig(BaseConfig):
    """
    BaseConfigクラスを継承してLocalConfigクラスを作成する
    """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'db/local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class StagingConfig(BaseConfig):
    """
    BaseConfigクラスを継承してStagingConfigクラスを作成する
    """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'db/stg.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    """
    BaseConfigクラスを継承してProductionConfigクラスを作成する
    """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'db/prd.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestingConfig(BaseConfig):
    """
    BaseConfigクラスを継承してTestingConfigクラスを作成する
    """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'db/testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CSRFトークンチェックを無効にする
    WTF_CSRF_ENABLED = False


# config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
    "stg": StagingConfig,
    "prd": ProductionConfig,
}