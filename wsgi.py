#!/usr/bin/python3.10

import sys
import os
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    # Add your project directory to the sys.path
    # Replace 'mehdikour' with your actual PythonAnywhere username
    path = '/home/mehdikour/trends-api'
    if path not in sys.path:
        sys.path.insert(0, path)
    
    logger.info(f"Added path to sys.path: {path}")
    logger.info(f"Current sys.path: {sys.path}")
    
    # Set environment variables
    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'production'
    
    logger.info("Environment variables set")
    
    # Import your Flask application
    from app import app as application
    
    logger.info("Flask app imported successfully")
    
except Exception as e:
    logger.error(f"Error in WSGI setup: {str(e)}")
    # Create a simple error application
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [f'<h1>Error</h1><p>WSGI Error: {str(e)}</p>'.encode('utf-8')]

if __name__ == "__main__":
    application.run()