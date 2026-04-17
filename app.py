from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['DEBUG'] = True


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/api/greet', methods=['POST'])
def greet():
    """API endpoint to greet a user"""
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({
        'message': f'Hello, {name}!',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically save to database or send email
        print(f"Contact form submission: {name}, {email}, {message}")
        
        return render_template('contact.html', success=True)
    
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
