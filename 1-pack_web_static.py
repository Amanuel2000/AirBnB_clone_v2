#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    """ Generates archive from the contents of web_static folder"""
    nameOfFile = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(nameOfFile))
        return "versions/web_static_{}.tgz".format(nameOfFile)
    except Exception as e:
        return None
