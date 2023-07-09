from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    Create a .tgz archive from the web_static folder
    """

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the archive using tar and gzip
    archive_name = "web_static_{}.tgz".format(timestamp)
    command = "tar -czvf versions/{} web_static".format(archive_name)
    result = local(command)

    if result.failed:
        return None

    # Check if the archive was created successfully
    archive_path = os.path.join("versions", archive_name)
    if os.path.exists(archive_path):
        # Set permissions to -rw-rw-r--
        local("chmod 664 {}".format(archive_path))
        return archive_path
    else:
        return None
