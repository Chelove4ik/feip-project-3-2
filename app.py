from flask import render_template

from backend.config import app


@app.route('/')
def index():
    name = "Test"
    return render_template('product.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
