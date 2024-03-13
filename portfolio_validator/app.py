# app.py
from flask import Flask, render_template, request, redirect, url_for
from validator import validate_portfolio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    html_file = request.files.get('html_file')
    css_file = request.files.get('css_file')

    if not html_file or not css_file:
        return redirect(url_for('index', error="Please upload both HTML and CSS files."))

    # Check if the uploaded files are of the correct type
    if html_file.filename.split('.')[-1].lower() != 'html':
        return redirect(url_for('index', error="Please upload an HTML file."))

    if css_file.filename.split('.')[-1].lower() != 'css':
        return redirect(url_for('index', error="Please upload a CSS file."))

    # Read HTML and CSS file contents
    html_content = html_file.read().decode('utf-8')
    css_content = css_file.read().decode('utf-8')

    # Validate HTML and CSS
    errors = validate_portfolio(html_content, css_content)

    if errors:
        return render_template('result.html', errors=errors)
    else:
        return render_template('result.html', message="Congratulations! Your portfolio meets all the criteria.")

if __name__ == '__main__':
    app.run(debug=True)
