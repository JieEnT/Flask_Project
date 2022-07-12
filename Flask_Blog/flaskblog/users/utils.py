import os
import secrets
from PIL import Image
#Need to import current_app since we no longer have immediate reference to app but instead have
#to rely on flask to find the app
from flask import current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    # saving the picture to the folder static with a name
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)

    # Resizing the image before saving so we dont have to load a large image each time which will slow down the app
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
