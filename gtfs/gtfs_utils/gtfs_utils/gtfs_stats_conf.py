import re
import os.path

# change this to your local working dir
# BASE_FOLDER = '../../../'
BASE_FOLDER = r'C:\Users\adiwa\Documents\OpenBusLocal'

DATA_FOLDER = os.path.join(BASE_FOLDER, 'data')

# LOCAL_TARIFF_PATH = DATA_FOLDER + 'archive/2018-07-27/Tariff.zip'
LOCAL_TARIFF_PATH = os.path.join(DATA_FOLDER, 'Tariff.zip')

GTFS_FEEDS_PATH = os.path.join(DATA_FOLDER, 'gtfs_feeds')

OUTPUT_DIR = os.path.join(DATA_FOLDER, 'gtfs_stats_MOD_ffill')

OUTPUT_FILE_NAME_RE = re.compile('^(?P<date_str>[^_]+?)'
                                 '_(?P<type>\w+)\.pkl\.gz')

BUCKET_NAME = 's3.obus.hasadna.org.il'
BUCKET_VALID_FILES_RE = re.compile('2018-08-12\.zip')
# BUCKET_VALID_FILES_RE = re.compile('2018-\d\d-\d\d\.zip')
FORWARD_FILL = False

DOWNLOAD_PBAR = False
SIZE_FOR_DOWNLOAD_PBAR = False
DELETE_DOWNLOADED_GTFS_ZIPS = False
WRITE_FEED_DANGEROUSLY = False
# FILTERED_FEEDS_PATH = DATA_FOLDER + 'filtered_feeds/'
FILTERED_FEEDS_PATH = os.path.join(DATA_FOLDER, 'filtered_feeds')

STATS_TYPES = ['trip_stats', 'route_stats']

# LOG_FOLDER = BASE_FOLDER + 'logs/'
LOG_FOLDER = os.path.join(BASE_FOLDER, 'logs')

PROFILE = False
# PROFILE_PATH = BASE_FOLDER + 'gtfs_stats_180601.prof'
PROFILE_PATH = os.path.join(BASE_FOLDER, 'gtfs_stats_180601.prof')
