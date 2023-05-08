from flask import render_template

from backend.config import app


@app.route('/product')
def index():
    name = "Product"
    return render_template('product.html', name=name)

@app.route('/')
def login():
    name = "Catalog"
    return render_template('catalog.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
