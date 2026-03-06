from flask import Flask, render_template, request, send_file, make_response
from werkzeug.utils import secure_filename
from bonkify.bonkifier import Bonkifier
import tempfile
import logging
import base64
import os


TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'j2')

class BonkifyServer(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.app =  Flask(__name__, template_folder=TEMPLATE_DIR)
        self.bonkifier = Bonkifier()

        @self.app.route('/')
        def index():
            return render_template('bonkify.html')

        @self.app.route('/process', methods=['POST'])
        def process():
            dst = tempfile.NamedTemporaryFile()
            out = tempfile.NamedTemporaryFile(suffix=".gif")
            file = request.files['file']
            file.save(dst.name)
            self.bonkifier.bonkify(dst.name, out.name)
            # res = send_file(out.name, mimetype='image/gif')
            # self.logger.warning(type(res))
            with open(out.name, 'rb') as f:
                image_binary = f.read()
                response = make_response(base64.b64encode(image_binary))
                response.headers.set('Content-Type', 'image/gif')
                response.headers.set('Content-Disposition', 'attachment', filename='image.gif')
                return response
            # return out.name

    def run(self):
        self.app.run(host='0.0.0.0', debug=False)

if __name__ == '__main__':
    BonkifyServer().run()
