#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy"""
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
import os

env.hosts =["52.91.182.187", "54.237.207.18"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    local("mkdir -p versions")
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("version") is False:
        if local("mkdir -p versions").failed is True:
            return None
        if local("tar -cvzf {} web_static".format(file)).failed is True:
            return None
        return file

def do_deploy(archive_path):
    """Distribute an archive.to the web server.
    Args:
        archive_path (str): The path of the archive
    Returns:
        False if the file doesn't exist at archive_path or an error occurs.
        And True if Otherwise.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/released/{}/web_static/* /data/web_static/released/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/released/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
