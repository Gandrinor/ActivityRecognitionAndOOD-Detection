from experiment import ex
from sacred.observers import MongoObserver, FileStorageObserver, QueueObserver
import logging
import sys

log = logging.getLogger("root")
log.handlers = []

log_format = logging.Formatter(
    "[{levelname:.1s}] {asctime} || {name} - {message}", style="{"
)

streamhandler = logging.StreamHandler(sys.stdout)
streamhandler.setFormatter(log_format)
log.addHandler(streamhandler)

log.setLevel("INFO")
ex.logger = log
#
# logging.getLogger("test").setLevel("INFO")


mobs = MongoObserver(
    url="curtiz:27017",
    db_name="sbartkow_sacred",
    username="sbartkow",
    password=open("/home/sbartkow/.mongodb_password")
    .read()
    .replace("\n", ""),
    authSource="admin",
)
ex.observers.append(QueueObserver(mobs))

# fs_observer = FileStorageObserver(basedir='my_runs')
# ex.observers.append(fs_observer)

r = ex.run()