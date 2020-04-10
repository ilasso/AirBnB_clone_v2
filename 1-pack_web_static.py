#!/usr/bin/python3
"""
    Deploys the archive to web server
"""

from fabric.api import *
from datetime import datetime
import os
env.hosts = ['35.231.101.65', '3.87.83.183']


def do_pack():
    """
        compresses a folder to a .tgz archive
    """
    local("sudo mkdir -p versions/")
    date_string = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        local("sudo tar -cvzf versions/web_static_{}.tgz "
              .format(date_string) + "web_static")
        return "/versions/web_static_{}.tgz".format(date_string)
    except BaseException:
        return None
