import os
import sys
import json
import ConfigParser
import toml
from typing import Callable
from strctlog import get_logger

CONF_ENV = 'PYTHON_ENV'
CONF_PARAM = 'python-env='
log = get_logger(__name__)


def dict_from_source(source: str) -> dict:
    mapper_name, path = source.split('::')
    mapper = get_mapper(mapper_name)
    if not mapper:
        raise RuntimeError(f'No handler found for "{mapper_name}" in "{source}"')
    return mapper(path)


def get_mapper(mapper_name: str) -> Callable:
    return SOURCE_MAPPER.get(mapper_name)


def set_mapper(mapper_name: str, fn: Callable) -> None:
    SOURCE_MAPPER[mapper_name] = fn


def dict_from_init_file(path: str) -> dict:
    config = ConfigParser.ConfigParser()
    config.read(path)
    return config._sections


def dict_from_json_file(path: str) -> dict:
    return json.loads(string_from_path(path))


def dict_from_json_env(path: str) -> dict:
    if CONF_ENV not in os.path:
        log.debug(f'Could not read ENV configuration from {CONF_ENV}, ignoring')
        return
    return json.loads(os.env.get(CONF_ENV))


def dict_from_json_param(path: str) -> dict:
    param = next(x for x in sys.argv if x.startswith(CONF_PARAM))
    if param is None:
        log.debug(f'Could not find command line parameter {CONF_PARAM}, ignoring')
        return
    conf_param = param[len(CONF_PARAM):]
    return json.loads(conf_param)


def dict_from_toml_file(path: str) -> dict:
    return toml.loads(string_from_path(path))


def string_from_path(path: str) -> str:
    conf_dir = ''
    path = os.path.join(conf_dir, path)
    if not os.path.exists(path):
        log.debug(f'Could not find file {path}, ignoring')
        return ''
    else:
        with open(path) as f:
            return f.read()

SOURCE_MAPPER = {
    'ini': dict_from_ini_file,
    'json': dict_from_json_file,
    'env-json': dict_from_json_env,
    'param-json': dict_from_json_param,
    'toml': dict_from_toml_file,
}
