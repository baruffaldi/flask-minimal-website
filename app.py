import os
from flask import Flask, render_template, send_from_directory

app = Flask(
        __name__, 
        template_folder="templates",
        static_folder="static"
    )

@app.route("/helloworld")
def helloworld():
    return "<p>Hello, World!</p>"

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(os.path.join(app.root_path, 'static'), 'images'),
                'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/", defaults={'path': "index.html"})
@app.route("/<path:path>")
def template_render_path(path):
    return render_template(path)