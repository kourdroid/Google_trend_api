# PythonAnywhere Deployment Guide

## 🚀 Deploy Your Google Trends API on PythonAnywhere

This guide will walk you through deploying your Google Trends API on PythonAnywhere step by step.

## Prerequisites

- PythonAnywhere account (free or paid)
- Your API files ready (app.py, requirements.txt, etc.)

## Step 1: Upload Your Files

### Option A: Using the Files Tab (Recommended for beginners)

1. **Login to PythonAnywhere**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Login to your account

2. **Navigate to Files**
   - Click on the "Files" tab in your dashboard
   - Navigate to your home directory (usually `/home/yourusername/`)

3. **Create Project Directory**
   - Click "New directory"
   - Name it `trends-api` or similar
   - Enter the directory

4. **Upload Files**
   - Click "Upload a file" for each file:
     - `app.py`
     - `requirements.txt`
     - `README.md`
   - Or use "New file" to copy-paste the content

### Option B: Using Git (Recommended for experienced users)

1. **Open a Bash Console**
   - Go to "Consoles" tab
   - Click "Bash"

2. **Clone Your Repository**
   ```bash
   cd ~
   git clone https://github.com/yourusername/your-repo.git trends-api
   cd trends-api
   ```

## Step 2: Install Dependencies

1. **Open a Bash Console** (if not already open)
   - Go to "Consoles" tab
   - Click "Bash"

2. **Navigate to Your Project**
   ```bash
   cd ~/trends-api
   ```

3. **Install Requirements**
   ```bash
   pip3.10 install --user -r requirements.txt
   ```
   
   **Note:** Use the Python version available on your PythonAnywhere plan:
   - Free accounts: `pip3.10`
   - Paid accounts: `pip3.11` or newer versions

## Step 3: Create WSGI Configuration

1. **Go to Web Tab**
   - Click on the "Web" tab in your dashboard
   - Click "Add a new web app"

2. **Choose Framework**
   - Select "Manual configuration"
   - Choose Python version (3.10 for free accounts, 3.11+ for paid)

3. **Configure WSGI File**
   - Scroll down to "Code" section
   - Click on the WSGI configuration file link (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`)

4. **Replace WSGI Content**
   Replace the entire content with:
   ```python
   import sys
   import os
   
   # Add your project directory to Python path
   path = '/home/yourusername/trends-api'  # Replace 'yourusername' with your actual username
   if path not in sys.path:
       sys.path.insert(0, path)
   
   # Set environment variables if needed
   os.environ['FLASK_APP'] = 'app.py'
   
   # Import your Flask app
   from app import app as application
   
   if __name__ == "__main__":
       application.run()
   ```

   **Important:** Replace `yourusername` with your actual PythonAnywhere username!

## Step 4: Configure Static Files (Optional)

If you plan to serve static files later:

1. **In Web Tab**
   - Scroll to "Static files" section
   - Add mapping:
     - URL: `/static/`
     - Directory: `/home/yourusername/trends-api/static/`

## Step 5: Set Environment Variables

1. **In Web Tab**
   - Scroll to "Environment variables" section
   - Add any needed variables:
     - `FLASK_ENV`: `production`
     - `PORT`: `80` (PythonAnywhere handles this automatically)

## Step 6: Reload and Test

1. **Reload Web App**
   - In Web tab, click the green "Reload" button
   - Wait for the reload to complete

2. **Test Your API**
   - Your API will be available at: `https://yourusername.pythonanywhere.com`
   - Test the endpoints:
     - `https://yourusername.pythonanywhere.com/` - API documentation
     - `https://yourusername.pythonanywhere.com/health` - Health check
     - `https://yourusername.pythonanywhere.com/trends/suggestions?keyword=python`

## Step 7: Update Your App (Future Updates)

### Method 1: File Upload
1. Go to Files tab
2. Navigate to your project directory
3. Upload new files or edit existing ones

### Method 2: Git Pull
1. Open Bash console
2. Navigate to project: `cd ~/trends-api`
3. Pull updates: `git pull origin main`
4. Install new dependencies: `pip3.10 install --user -r requirements.txt`
5. Reload web app in Web tab

## Troubleshooting

### Common Issues and Solutions

1. **Import Errors**
   - Check that all dependencies are installed
   - Verify Python version compatibility
   - Check WSGI file path configuration

2. **Module Not Found**
   ```bash
   # In Bash console, check installed packages
   pip3.10 list --user
   
   # Reinstall if needed
   pip3.10 install --user package-name
   ```

3. **WSGI Configuration Issues**
   - Double-check the path in WSGI file
   - Ensure your username is correct
   - Verify the import statement matches your app structure

4. **Check Error Logs**
   - In Web tab, click on "Error log" link
   - Review recent errors for debugging

### Testing Individual Components

1. **Test in Console**
   ```bash
   cd ~/trends-api
   python3.10
   >>> from app import app
   >>> # If no errors, your app imports correctly
   ```

2. **Test Dependencies**
   ```bash
   python3.10 -c "import flask, pytrends, pandas; print('All imports successful')"
   ```

## PythonAnywhere-Specific Notes

### Free Account Limitations
- Limited CPU seconds per day
- Automatic sleep after inactivity
- Limited outbound internet access
- Python 3.10 maximum

### Paid Account Benefits
- No CPU limitations
- Always-on tasks
- Full internet access
- Latest Python versions
- Custom domains

### API Rate Limiting
- Google Trends has built-in rate limiting
- PythonAnywhere may add additional limits
- Consider implementing caching for frequently requested data

## Example n8n Configuration for PythonAnywhere

```json
{
  "nodes": [
    {
      "name": "Get Trends Data",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://yourusername.pythonanywhere.com/trends/interest_over_time",
        "qs": {
          "keywords": "python,javascript",
          "timeframe": "today 12-m",
          "geo": "US"
        }
      }
    }
  ]
}
```

## Security Considerations

1. **Environment Variables**
   - Store sensitive data in environment variables
   - Never commit API keys to version control

2. **HTTPS**
   - PythonAnywhere provides HTTPS by default
   - Always use HTTPS URLs in production

3. **Rate Limiting**
   - Consider implementing rate limiting for your API
   - Monitor usage to prevent abuse

## Performance Tips

1. **Caching**
   - Implement caching for frequently requested data
   - Use Redis or simple file caching

2. **Error Handling**
   - Implement comprehensive error handling
   - Log errors for debugging

3. **Monitoring**
   - Monitor your app's performance
   - Set up alerts for downtime

## Support

- **PythonAnywhere Help**: [help.pythonanywhere.com](https://help.pythonanywhere.com)
- **Forums**: [pythonanywhere.com/forums](https://www.pythonanywhere.com/forums/)
- **API Documentation**: Available at your app's root URL

---

**Your Google Trends API is now ready for production on PythonAnywhere! 🎉**

Remember to replace `yourusername` with your actual PythonAnywhere username throughout the configuration.