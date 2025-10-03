# PythonAnywhere Troubleshooting Guide

## 🚨 "Something went wrong" Error - Step by Step Fix

### Step 1: Check Your WSGI Configuration

1. **Go to Web Tab** in your PythonAnywhere dashboard
2. **Click on your WSGI configuration file** (usually `/var/www/mehdikour_pythonanywhere_com_wsgi.py`)
3. **Replace the entire content** with the improved WSGI file I created

### Step 2: Verify Your File Structure

Make sure your files are in the correct location:
```
/home/mehdikour/
└── trends-api/
    ├── app.py
    ├── requirements.txt
    ├── wsgi.py
    └── other files...
```

### Step 3: Install Dependencies

1. **Open a Bash Console**
2. **Run these commands:**
   ```bash
   cd ~/trends-api
   pip3.10 install --user Flask Flask-CORS pytrends requests
   ```

### Step 4: Test Your App Locally

1. **In Bash Console:**
   ```bash
   cd ~/trends-api
   python3.10 app.py
   ```
   
2. **If you get errors, they'll show here**

### Step 5: Check Error Logs

1. **Go to Web Tab**
2. **Click "Error log"** link
3. **Look for recent errors**

## Common Issues and Solutions

### Issue 1: Import Errors

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
pip3.10 install --user Flask Flask-CORS pytrends requests pandas
```

### Issue 2: Path Issues

**Error:** `ModuleNotFoundError: No module named 'app'`

**Solution:** Check that your WSGI file has the correct path:
```python
path = '/home/mehdikour/trends-api'  # Replace 'mehdikour' with YOUR username
```

### Issue 3: Python Version

**Error:** Various import errors

**Solution:** Make sure you're using Python 3.10 (free accounts):
- In Web tab, select Python 3.10
- Use `pip3.10` not just `pip`

### Issue 4: File Permissions

**Error:** Permission denied

**Solution:**
```bash
chmod +x ~/trends-api/app.py
```

## Quick Diagnostic Commands

Run these in Bash Console to diagnose issues:

```bash
# Check if files exist
ls -la ~/trends-api/

# Check Python version
python3.10 --version

# Check installed packages
pip3.10 list --user

# Test imports
python3.10 -c "import flask; print('Flask OK')"
python3.10 -c "import pytrends; print('PyTrends OK')"

# Test your app import
cd ~/trends-api
python3.10 -c "from app import app; print('App import OK')"
```

## Step-by-Step Recovery Process

### 1. Clean Installation

```bash
# Remove old installation
rm -rf ~/trends-api

# Create fresh directory
mkdir ~/trends-api
cd ~/trends-api
```

### 2. Upload Files Again

- Upload `app.py`
- Upload `requirements.txt`
- Upload the new `wsgi.py`

### 3. Install Dependencies

```bash
pip3.10 install --user -r requirements.txt
```

### 4. Update WSGI Configuration

Copy the content from the improved `wsgi.py` file to your PythonAnywhere WSGI configuration.

### 5. Reload Web App

Click the green "Reload" button in the Web tab.

## Alternative Simple WSGI Configuration

If you're still having issues, try this minimal WSGI configuration:

```python
import sys
import os

# Add your project directory to the sys.path
path = '/home/mehdikour/trends-api'
if path not in sys.path:
    sys.path.insert(0, path)

try:
    from app import app as application
except ImportError:
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Import error: Could not import Flask app']
```

## Testing Your API Endpoints

Once your app is running, test these URLs:

1. **Basic test:** `https://mehdikour.pythonanywhere.com/`
2. **Health check:** `https://mehdikour.pythonanywhere.com/health`
3. **Simple endpoint:** `https://mehdikour.pythonanywhere.com/trends/suggestions?keyword=python`

## Common PythonAnywhere Gotchas

1. **Username in paths:** Always use YOUR actual username, not `yourusername`
2. **Python version:** Free accounts are limited to Python 3.10
3. **Package installation:** Always use `--user` flag
4. **File paths:** Use absolute paths starting with `/home/yourusername/`
5. **Reload required:** Always reload after changes

## If Nothing Works

1. **Delete the web app** in Web tab
2. **Create a new one** with manual configuration
3. **Start fresh** with the files I provided
4. **Follow the deployment guide** step by step

## Getting Help

If you're still stuck:

1. **Check the error log** in Web tab
2. **Run diagnostic commands** in Bash console
3. **Copy exact error messages**
4. **Check PythonAnywhere forums**

## Success Indicators

You'll know it's working when:
- ✅ No errors in error log
- ✅ Your site loads without "Something went wrong"
- ✅ API endpoints return JSON responses
- ✅ Health check returns status

---

**Remember:** Replace `mehdikour` with your actual PythonAnywhere username in all paths and configurations!