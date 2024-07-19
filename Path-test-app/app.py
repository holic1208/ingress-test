from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('image.html', image_url="https://xen-api.linkareer.com/attachments/107217")

@app.route("/ddong")
def ddong():
    return render_template('image.html', image_url="https://mblogthumb-phinf.pstatic.net/MjAyMDA4MzBfMTE5/MDAxNTk4NzI0NjA4NDEx.BzdlGdz4xN9MAG458Avn1gsSYUJnEHaldfGw2XSVaeUg.yD4pxO4hiwpsFr6i9f_BwbKafuGFBnN0M60kdboJLI0g.JPEG.gahee0317/IMG_6066.JPG?type=w800")

@app.route("/sunday")
def sunday():
    return render_template('image.html', image_url="https://mblogthumb-phinf.pstatic.net/MjAyMDA4MzBfMjMx/MDAxNTk4NzI0NjA3MzY2.8PGu5WjJNb0MrQQCV2TBqp-u6ydWqHpbO0Es-OPeaqQg.Zrn1kEyRhGOBg_v_Kf99vYVi0tjJBemXadgG7R7KGowg.JPEG.gahee0317/IMG_6082.JPG?type=w800")

@app.route("/tired")
def tired():
    return render_template('image.html', image_url="https://mblogthumb-phinf.pstatic.net/MjAyMDA4MzBfMTAx/MDAxNTk4NzI0NjA4MTEw.Y4cB4n1_qz_lXQwW3TTXXbNK1kRO5tle2DhGZ-yuUWwg._nTY7ZGccJoQdwJ7Dz5cbiUHp0eVjF7KQ2QxecNww9Ag.JPEG.gahee0317/IMG_6078.JPG?type=w800")

@app.route("/chiken")
def chiken():
    return render_template('image.html', image_url="https://d12zq4w4guyljn.cloudfront.net/750_750_20210914121555_photo1_e779ae9ed590.jpg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
