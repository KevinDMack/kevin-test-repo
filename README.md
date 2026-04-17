# Flask Web Application

A simple and elegant Flask web application with multiple pages, API endpoints, and responsive design.

## Features

- **Home Page**: Welcome page with feature cards
- **About Page**: Information about the application
- **Contact Page**: Contact form for user submissions
- **REST API**: `/api/greet` endpoint for greeting users
- **Error Handling**: Custom 404 and 500 error pages
- **Responsive Design**: Mobile-friendly CSS styling
- **Static Files**: Organized CSS and JavaScript files

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── contact.html      # Contact form page
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
└── README.md             # This file
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd kevin-test-repo
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

3. **Open in browser**:
   Navigate to `http://localhost:5000`

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/about` | GET | About page |
| `/contact` | GET, POST | Contact form page |
| `/api/greet` | POST | API endpoint that returns a greeting |

## API Usage

### Greet Endpoint

**Request**:
```bash
curl -X POST http://localhost:5000/api/greet \
  -H "Content-Type: application/json" \
  -d '{"name": "John"}'
```

**Response**:
```json
{
  "message": "Hello, John!",
  "timestamp": "2026-04-17T12:00:00.000000"
}
```

## Development

### Modifying Templates

Edit files in the `templates/` directory. All templates inherit from `base.html` which includes the navigation and footer.

### Styling

Modify `static/css/style.css` to customize the appearance. CSS variables are defined at the top for easy theming.

### Adding JavaScript

Add JavaScript functionality to `static/js/main.js`. The `greetUser()` function demonstrates calling the API endpoint.

## Adding New Routes

Example of adding a new route to `app.py`:

```python
@app.route('/new-page')
def new_page():
    """New page description"""
    return render_template('new_page.html')
```

Create the corresponding template in `templates/new_page.html` extending `base.html`.

## Configuration

Edit the `app.py` file to modify:
- `SECRET_KEY`: Change for production deployment
- `DEBUG`: Set to `False` for production
- Host and port in the `app.run()` call

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please create an issue in the repository.