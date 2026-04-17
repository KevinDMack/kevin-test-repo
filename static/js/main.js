/**
 * Main JavaScript file for Flask application
 */

/**
 * Send greeting request to the server
 */
async function greetUser() {
    const name = prompt('Enter your name:') || 'Friend';
    
    try {
        const response = await fetch('/api/greet', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: name })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        showResponse(data.message);
    } catch (error) {
        console.error('Error:', error);
        showResponse('Error occurred while fetching greeting.');
    }
}

/**
 * Display response message on the page
 */
function showResponse(message) {
    const responseDiv = document.getElementById('response');
    if (responseDiv) {
        responseDiv.textContent = message;
        responseDiv.style.display = 'block';
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            responseDiv.style.display = 'none';
        }, 5000);
    }
}

/**
 * Initialize any event listeners on page load
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('Flask application loaded');
});
