from __future__ import print_function
from __future__ import absolute_import
from swc import app

if __name__ == '__main__':
    print('Starting app.run')
    app.run(host='0.0.0.0', port=8000, use_reloader=True, threaded=True, debug=True)
    print('Stopped app.run')