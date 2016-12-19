# flask10.py
# ref:
# http://flask.pocoo.org/

# Demo1:
# export FLASK_DEBUG=1
# export FLASK_APP=flask10.py
# flask run
# curl 127.0.0.1:5000/
# Above syntax offers 'auto-reload' feature.

# Demo2:
# python flask10.py

# Demo3:
# gunicorn wsgi

# Demo2, Demo3 offer one-shell-command simplicity.

import os
from   flask import Flask
application = Flask(__name__)
                               
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
'bye'
