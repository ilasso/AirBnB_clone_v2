#!/usr/bin/python3
"""
    Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
"""

from fabric.api import *
from datetime import datetime
import os
env.hosts = ['35.231.101.65', '3.87.83.183']


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy

    """
    if os.path.exists(archive_path) is False:
        return False
    # Extract filename without extension (tgz)
    withoutext = archive_path[9:34]

    # Extract Complete filename with extension (tgz)
    withext = archive_path[9:]

    # Built uncompress path
    uncomprespath = "/data/web_static/releases/{}/".format(withoutext)

    try:
        # copy file tgz to servers
        put(archive_path, "/tmp/")
        # create uncompress path if doesnt exist
        run("sudo mkdir -p {}".format(uncomprespath))
        # uncompress file in uncompress path
        run("sudo tar -zxvf /tmp/{} -C {}".format(withext, uncomprespath))
        # delete tar file tgz
        run("sudo rm -rf /tmp/{}".format(withext))
        # move files under uncompress path/web_static --> releases
        run("sudo mv -n {}/web_static/* {}".format(uncomprespath,
                                                   uncomprespath))
        # rm web_static directory
        run("sudo rm -rf {}/web_static".format(uncomprespath))
        # recreate link
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(uncomprespath))
        return True

    except Exception:
        return False
