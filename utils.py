import os
from datetime import datetime

from config import static_path

static_for = lambda x: os.path.join(static_path, x)
current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")