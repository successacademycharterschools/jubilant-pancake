"""
Configuration parser to retrive server run-time parameters.
Main source is config.[ENV].json in folder given by --configdir parameter.
SSL key and cert should be in the same folder,
in case of in-app SSL termination.
"""

import os
import json
from pkg_resources import resource_filename
from tornado import options


options.define(
    'static_path',
    default=resource_filename(__name__, '../static')
    )
options.define(
    'template_path',
    default=resource_filename(__name__, '../template')
    )
options.define(
    'configdir',
    default=resource_filename(__name__, '../config'),
    help="Folder with config.json and keys"
    )
options.define(
    'env',
    default='dev',
    help="Runtime environment: dev, prd"
    )

options.parse_command_line()

config_file = os.path.join(
    options.options.configdir,
    'config.{}.json'.format(options.options.env)
    )
if os.path.exists(config_file):
    for k, v in json.load(open(config_file)).items():
        options.define(k, default=v)
else:
    raise FileNotFoundError('file {} could not be read'.format(config_file))
