from flask import Flask, jsonify, request
from flask_cors import CORS
from pytrends.request import TrendReq
import pandas as pd
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)
CORS(app)

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

@app.route('/', methods=['GET'])
def home():
    """API home endpoint with documentation"""
    return jsonify({
        "message": "Google Trends API",
        "version": "1.0.0",
        "endpoints": {
            "/trends/interest_over_time": "GET - Get interest over time for keywords",
            "/trends/interest_by_region": "GET - Get interest by region for keywords", 
            "/trends/related_topics": "GET - Get related topics for keywords",
            "/trends/related_queries": "GET - Get related queries for keywords",
            "/trends/trending_searches": "GET - Get trending searches by country",
            "/trends/top_charts": "GET - Get top charts for a year and country",
            "/trends/suggestions": "GET - Get keyword suggestions"
        },
        "parameters": {
            "keywords": "Comma-separated list of keywords (max 5)",
            "timeframe": "Time range (e.g., 'today 5-y', 'today 12-m', 'now 7-d')",
            "geo": "Geographic location (e.g., 'US', 'GB', 'DE')",
            "category": "Category ID (0 for all categories)",
            "gprop": "Google property ('', 'images', 'news', 'youtube', 'froogle')"
        }
    })

@app.route('/trends/interest_over_time', methods=['GET'])
def interest_over_time():
    """Get interest over time for keywords"""
    try:
        keywords = request.args.get('keywords', '').split(',')
        keywords = [k.strip() for k in keywords if k.strip()]
        
        if not keywords:
            return jsonify({"error": "Keywords parameter is required"}), 400
        
        if len(keywords) > 5:
            return jsonify({"error": "Maximum 5 keywords allowed"}), 400
        
        timeframe = request.args.get('timeframe', 'today 12-m')
        geo = request.args.get('geo', '')
        category = int(request.args.get('category', 0))
        gprop = request.args.get('gprop', '')
        
        # Build payload
        pytrends.build_payload(
            kw_list=keywords,
            cat=category,
            timeframe=timeframe,
            geo=geo,
            gprop=gprop
        )
        
        # Get interest over time
        data = pytrends.interest_over_time()
        
        if data.empty:
            return jsonify({"data": [], "keywords": keywords, "message": "No data available"})
        
        # Convert to JSON-friendly format
        data = data.reset_index()
        data['date'] = data['date'].dt.strftime('%Y-%m-%d')
        
        result = {
            "keywords": keywords,
            "timeframe": timeframe,
            "geo": geo,
            "data": data.to_dict('records')
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trends/interest_by_region', methods=['GET'])
def interest_by_region():
    """Get interest by region for keywords"""
    try:
        keywords = request.args.get('keywords', '').split(',')
        keywords = [k.strip() for k in keywords if k.strip()]
        
        if not keywords:
            return jsonify({"error": "Keywords parameter is required"}), 400
        
        if len(keywords) > 5:
            return jsonify({"error": "Maximum 5 keywords allowed"}), 400
        
        timeframe = request.args.get('timeframe', 'today 12-m')
        geo = request.args.get('geo', '')
        category = int(request.args.get('category', 0))
        resolution = request.args.get('resolution', 'COUNTRY')
        
        # Build payload
        pytrends.build_payload(
            kw_list=keywords,
            cat=category,
            timeframe=timeframe,
            geo=geo
        )
        
        # Get interest by region
        data = pytrends.interest_by_region(resolution=resolution, inc_low_vol=True, inc_geo_code=True)
        
        if data.empty:
            return jsonify({"data": [], "keywords": keywords, "message": "No data available"})
        
        # Convert to JSON-friendly format
        data = data.reset_index()
        
        result = {
            "keywords": keywords,
            "timeframe": timeframe,
            "geo": geo,
            "resolution": resolution,
            "data": data.to_dict('records')
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trends/related_topics', methods=['GET'])
def related_topics():
    """Get related topics for keywords"""
    try:
        keywords = request.args.get('keywords', '').split(',')
        keywords = [k.strip() for k in keywords if k.strip()]
        
        if not keywords:
            return jsonify({"error": "Keywords parameter is required"}), 400
        
        if len(keywords) > 5:
            return jsonify({"error": "Maximum 5 keywords allowed"}), 400
        
        timeframe = request.args.get('timeframe', 'today 12-m')
        geo = request.args.get('geo', '')
        category = int(request.args.get('category', 0))
        
        # Build payload
        pytrends.build_payload(
            kw_list=keywords,
            cat=category,
            timeframe=timeframe,
            geo=geo
        )
        
        # Get related topics
        data = pytrends.related_topics()
        
        result = {"keywords": keywords, "related_topics": {}}
        
        for keyword in keywords:
            if keyword in data:
                keyword_data = {}
                if data[keyword]['top'] is not None:
                    keyword_data['top'] = data[keyword]['top'].to_dict('records')
                else:
                    keyword_data['top'] = []
                    
                if data[keyword]['rising'] is not None:
                    keyword_data['rising'] = data[keyword]['rising'].to_dict('records')
                else:
                    keyword_data['rising'] = []
                    
                result["related_topics"][keyword] = keyword_data
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trends/related_queries', methods=['GET'])
def related_queries():
    """Get related queries for keywords"""
    try:
        keywords = request.args.get('keywords', '').split(',')
        keywords = [k.strip() for k in keywords if k.strip()]
        
        if not keywords:
            return jsonify({"error": "Keywords parameter is required"}), 400
        
        if len(keywords) > 5:
            return jsonify({"error": "Maximum 5 keywords allowed"}), 400
        
        timeframe = request.args.get('timeframe', 'today 12-m')
        geo = request.args.get('geo', '')
        category = int(request.args.get('category', 0))
        
        # Build payload
        pytrends.build_payload(
            kw_list=keywords,
            cat=category,
            timeframe=timeframe,
            geo=geo
        )
        
        # Get related queries
        data = pytrends.related_queries()
        
        result = {"keywords": keywords, "related_queries": {}}
        
        for keyword in keywords:
            if keyword in data:
                keyword_data = {}
                if data[keyword]['top'] is not None:
                    keyword_data['top'] = data[keyword]['top'].to_dict('records')
                else:
                    keyword_data['top'] = []
                    
                if data[keyword]['rising'] is not None:
                    keyword_data['rising'] = data[keyword]['rising'].to_dict('records')
                else:
                    keyword_data['rising'] = []
                    
                result["related_queries"][keyword] = keyword_data
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trends/trending_searches', methods=['GET'])
def trending_searches():
    """Get trending searches by country"""
    try:
        country = request.args.get('country', 'united_states')
        
        # Get trending searches
        data = pytrends.trending_searches(pn=country)
        
        if data.empty:
            return jsonify({"data": [], "country": country, "message": "No data available"})
        
        # Convert to list
        trending_list = data[0].tolist()
        
        result = {
            "country": country,
            "trending_searches": trending_list,
            "count": len(trending_list)
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trends/top_charts', methods=['GET'])
def top_charts():
    """Get top charts for a year and country"""
    try:
        year = int(request.args.get('year', datetime.now().year))
        geo = request.args.get('geo', 'GLOBAL')
        
        # Get top charts
        data = pytrends.top_charts(year, hl='en-US', tz=300, geo=geo)
        
        if data.empty:
            return jsonify({"data": [], "year": year, "geo": geo, "message": "No data available"})
        
        result = {
            "year": year,
            "geo": geo,
            "data": data.to_dict('records')
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trends/suggestions', methods=['GET'])
def suggestions():
    """Get keyword suggestions"""
    try:
        keyword = request.args.get('keyword', '')
        
        if not keyword:
            return jsonify({"error": "Keyword parameter is required"}), 400
        
        # Get suggestions
        data = pytrends.suggestions(keyword=keyword)
        
        result = {
            "keyword": keyword,
            "suggestions": data
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Google Trends API"
    })

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='127.0.0.1', port=port, debug=debug)
    
# For PythonAnywhere WSGI
# The application object is used by WSGI servers