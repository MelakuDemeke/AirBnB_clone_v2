#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        
        local("tar -czvf {} web_static".format(archive_path))

        file_size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, file_size))
        
        return archive_path
    except:
        return None
