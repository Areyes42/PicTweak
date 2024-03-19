from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            image_path = os.path.join('uploads', file.filename)
            file.save(image_path)
            manipulated_image_path = manipulate_image(image_path)
            return f'<img src="{manipulated_image_path}" alt="manipulated image">'
    return render_template('index.html')

def manipulate_image(image_path):
    img = Image.open(image_path)
    # Perform image manipulation here
    # For example, convert to black and white
    img = img.convert('L')
    manipulated_image_path = os.path.join('manipulated', os.path.basename(image_path))
    img.save(manipulated_image_path)
    return manipulated_image_path

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('manipulated'):
        os.makedirs('manipulated')
    app.run(port=8000, debug=True)