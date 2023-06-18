from datetime import datetime

# Folder structure settings
root_folder = ''  # Relative to this file
data_folder = 'terep/adatok'  # Relative to root folder
project_folder = 'terep/projects'  # Relative to root folder
master_folder = 'terep/master'  # Relative to root folder
sensitive_folder = 'sensitive'  # Relative to root folder

# Variables for project files
project_version = '3.1.' + datetime.now().strftime('%Y%m%d')
workgroup = 'DHTE'
compiling_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
server_short_name = 'NC'
server_url = 'https://nextcloud.del-heves.hu'

# Variables for data upload
server_type = ['OBM']  # Should be a set with the following values: 'OBM, POSTGIS'
postgres_server = None
obm_server = 'https://obm.bnpi.hu'
