import os
import datetime

"""
Environment variables:
- FFB_LEAGUE_ID
- FFB_YEAR
- SWID
- ESPN_S2
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_DB
"""


def get_db_uri(user, password, host, port, dbname):
    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    # return f"mysql://{user}:{password}@{host}:{port}/{dbname}"
    # return f"oracle://{user}:{password}@{host}:{port}/{dbname}"


class Config(object):
    LEAGUE_ID = os.getenv('FFB_LEAGUE_ID')
    CURRENT_YEAR = os.getenv('FFB_YEAR', datetime.datetime.now().year)
    DB_URI = ""
    COOKIES = {
        "swid": os.getenv('SWID'),
        "espn_s2": os.getenv('ESPN_S2')
    }

    log_format = "%(asctime)s %(levelname)s %(pathname)s %(lineno)d: %(message)s"
    log_interval = 1
    log_base_dir = ""
    console_level = 20
    rootlogger_level = 10
    filelog_level = 20
    log_backup_count = 90
    log_when = "midnight"


class DevConfig(Config):
    config_dir = "conf"

    user = "your_dev_user"
    password = "your_dev_pw"
    host = "localhost"
    port = "5432"
    dbname = "your_dev_db"

    log_base_dir = "log"
    # console_level = 10

    DB_URI = get_db_uri(user=user, password=password,
                        host=host, port=port, dbname=dbname)


class ProdConfig(Config):
    config_dir = os.getenv('CONFIG_DIR', '/etc/espn-ffb')

    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST', 'db')
    port = os.getenv('POSTGRES_PORT', '5432')
    dbname = os.getenv('POSTGRES_DB', 'espn-ffb')

    log_base_dir = os.getenv('LOG_BASE_DIR', '/var/log/espn-ffb')

    DB_URI = get_db_uri(user=user, password=password,
                        host=host, port=port, dbname=dbname)
