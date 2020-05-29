from datetime import datetime
from PIL import Image
import cv2
import io
import re
import base64
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
from google.cloud import storage


project_id = "your GCP project name"
bucket_name = 'your GCS backet name'
upload_path = "normal"
save_dir = 'one'

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    global save_dir
    global upload_path
    if request.method == 'POST':
        if 	request.form.get('radio') is None:
            ans = get_img(request)
            return jsonify({'ans': ans})
        else:
            save_dir = request.form.get('radio')
            upload_path = request.form.get('fav')
            return render_template('index.html', message=upload_path+'の'+save_dir+'が選択されています')
    else:
        return render_template('index.html', message='入力する文字の種類を選択してください')


def save_img(img):
    # Create a Cloud Storage client.
    time = datetime.now().strftime('%M_%S')

    gcs = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket(bucket_name)
    bio = io.BytesIO()
    img.save(bio, format='png')
    blob = storage.Blob('{}/{}/test{}.png'.format(upload_path, save_dir, time), bucket)
    blob.upload_from_string(data=bio.getvalue(), content_type="image/png")

    return 'save ok'


def get_img(req):
    img_str = re.search(r'base64,(.*)', req.form['img']).group(1)
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    img_resize = cv2.resize(img_gray, (32, 64))
    pil_img = Image.fromarray(img_resize)

    ans = save_img(pil_img)
    return ans


if __name__ == "__main__":
    app.run()
