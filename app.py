from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

def resize_image(img, new_width):
    width, height = img.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = img.resize((new_width, new_height))
    return resized_image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')  # Get list of uploaded files
        new_width = int(request.form['width'])
        resized_images = []
        for file in files:
            if file:
                img = Image.open(file)
                resized_img = resize_image(img, new_width)
                filename = f"resized_{file.filename}"
                filepath = os.path.join("static", filename)
                resized_img.save(filepath)
                resized_images.append(filepath)
        return render_template('index.html', resized_images=resized_images)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
