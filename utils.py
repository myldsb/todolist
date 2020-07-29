import os

from config import static_path

static_for = lambda x: os.path.join(static_path, x)