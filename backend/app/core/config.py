import os

config = {key.replace("BLOG_", "").lower(): value for key, value in os.environ.items() if key.startswith("BLOG_")}
