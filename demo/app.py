from flask import Flask, render_template, request, url_for, redirect, abort

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('products-page.html')

if __name__ == "__main__":
    app.run(debug = True)