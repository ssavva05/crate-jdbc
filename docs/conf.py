from crate.theme.rtd.conf.crate_server import *

exclude_patterns = ['.venv/**', 'out/**', 'tmp/**', 'eggs/**', 'requirements.txt', 'requirements-raw.txt']

# crate.theme sets html_favicon to favicon.png which causes a warning because it should be a .ico
# and in addition there is no favicon.png in this project so it can't find the file
html_favicon = None
