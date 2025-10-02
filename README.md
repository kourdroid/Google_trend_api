# Google Trends API

A flexible REST API for accessing Google Trends data using pytrends. Perfect for integration with n8n workflows and deployment on Render.com.

## Features

- 🔍 **Interest Over Time** - Track keyword popularity over time
- 🌍 **Interest by Region** - Geographic distribution of search interest
- 🔗 **Related Topics & Queries** - Discover related content
- 📈 **Trending Searches** - Current trending searches by country
- 🏆 **Top Charts** - Annual top searches
- 💡 **Keyword Suggestions** - Get search suggestions
- 🚀 **Ready for Render.com** - Configured for easy deployment
- 🔄 **n8n Compatible** - Perfect for workflow automation

## Quick Start

### Local Development

1. **Clone and Install**
   ```bash
   git clone <your-repo>
   cd trends-api
   pip install -r requirements.txt
   ```

2. **Run the API**
   ```bash
   python app.py
   ```

3. **Test the API**
   ```bash
   curl http://localhost:5000/
   ```

### Deploy on Render.com

1. **Connect Repository**
   - Go to [Render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository

2. **Configure Service**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3

3. **Deploy**
   - Click "Create Web Service"
   - Your API will be available at `https://your-service.onrender.com`

## API Endpoints

### Base URL
- Local: `http://localhost:5000`
- Render: `https://your-service.onrender.com`

### Endpoints Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/health` | GET | Health check |
| `/trends/interest_over_time` | GET | Interest over time |
| `/trends/interest_by_region` | GET | Interest by region |
| `/trends/related_topics` | GET | Related topics |
| `/trends/related_queries` | GET | Related queries |
| `/trends/trending_searches` | GET | Trending searches |
| `/trends/top_charts` | GET | Top charts |
| `/trends/suggestions` | GET | Keyword suggestions |

### 1. Interest Over Time

Get search interest over time for keywords.

**Endpoint:** `GET /trends/interest_over_time`

**Parameters:**
- `keywords` (required): Comma-separated keywords (max 5)
- `timeframe` (optional): Time range (default: "today 12-m")
- `geo` (optional): Geographic location (e.g., "US", "GB")
- `category` (optional): Category ID (default: 0)
- `gprop` (optional): Google property ("", "images", "news", "youtube", "froogle")

**Example:**
```bash
curl "https://your-api.onrender.com/trends/interest_over_time?keywords=python,javascript&timeframe=today 3-m&geo=US"
```

**Response:**
```json
{
  "keywords": ["python", "javascript"],
  "timeframe": "today 3-m",
  "geo": "US",
  "data": [
    {
      "date": "2024-01-01",
      "python": 75,
      "javascript": 82,
      "isPartial": false
    }
  ]
}
```

### 2. Interest by Region

Get geographic distribution of search interest.

**Endpoint:** `GET /trends/interest_by_region`

**Parameters:**
- `keywords` (required): Comma-separated keywords (max 5)
- `timeframe` (optional): Time range (default: "today 12-m")
- `geo` (optional): Geographic location
- `resolution` (optional): "COUNTRY", "REGION", "CITY" (default: "COUNTRY")

**Example:**
```bash
curl "https://your-api.onrender.com/trends/interest_by_region?keywords=python&resolution=COUNTRY"
```

### 3. Related Topics

Get topics related to your keywords.

**Endpoint:** `GET /trends/related_topics`

**Example:**
```bash
curl "https://your-api.onrender.com/trends/related_topics?keywords=artificial intelligence"
```

### 4. Related Queries

Get search queries related to your keywords.

**Endpoint:** `GET /trends/related_queries`

**Example:**
```bash
curl "https://your-api.onrender.com/trends/related_queries?keywords=machine learning"
```

### 5. Trending Searches

Get current trending searches by country.

**Endpoint:** `GET /trends/trending_searches`

**Parameters:**
- `country` (optional): Country name (default: "united_states")

**Example:**
```bash
curl "https://your-api.onrender.com/trends/trending_searches?country=united_states"
```

### 6. Top Charts

Get top searches for a specific year.

**Endpoint:** `GET /trends/top_charts`

**Parameters:**
- `year` (optional): Year (default: current year)
- `geo` (optional): Geographic location (default: "GLOBAL")

**Example:**
```bash
curl "https://your-api.onrender.com/trends/top_charts?year=2023&geo=US"
```

### 7. Keyword Suggestions

Get keyword suggestions for a search term.

**Endpoint:** `GET /trends/suggestions`

**Parameters:**
- `keyword` (required): Search term

**Example:**
```bash
curl "https://your-api.onrender.com/trends/suggestions?keyword=programming"
```

## n8n Integration

### Setting up in n8n

1. **HTTP Request Node**
   - Method: GET
   - URL: `https://your-api.onrender.com/trends/interest_over_time`
   - Query Parameters:
     - `keywords`: `python,javascript`
     - `timeframe`: `today 12-m`
     - `geo`: `US`

2. **Example Workflow**
   ```json
   {
     "nodes": [
       {
         "name": "Get Trends Data",
         "type": "n8n-nodes-base.httpRequest",
         "parameters": {
           "url": "https://your-api.onrender.com/trends/interest_over_time",
           "qs": {
             "keywords": "=python,javascript",
             "timeframe": "today 12-m",
             "geo": "US"
           }
         }
       }
     ]
   }
   ```

### Common n8n Use Cases

1. **Daily Trend Reports**
   - Schedule: Daily trigger
   - Get trending searches
   - Send to Slack/Email

2. **Keyword Monitoring**
   - Schedule: Weekly trigger
   - Monitor specific keywords
   - Alert on significant changes

3. **Competitive Analysis**
   - Compare brand keywords
   - Track regional performance
   - Generate reports

## Time Frames

Common timeframe values:
- `now 1-H` - Last hour
- `now 4-H` - Last 4 hours
- `now 1-d` - Last day
- `now 7-d` - Last 7 days
- `today 1-m` - Last month
- `today 3-m` - Last 3 months
- `today 12-m` - Last 12 months
- `today 5-y` - Last 5 years
- `all` - All available data

## Geographic Codes

Common geo codes:
- `US` - United States
- `GB` - United Kingdom
- `DE` - Germany
- `FR` - France
- `JP` - Japan
- `AU` - Australia
- `CA` - Canada
- `IN` - India
- `BR` - Brazil

## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `400` - Bad Request (invalid parameters)
- `500` - Internal Server Error

Error response format:
```json
{
  "error": "Error description"
}
```

## Rate Limiting

Google Trends has built-in rate limiting. If you encounter rate limits:
- Reduce request frequency
- Use longer timeframes
- Implement retry logic with exponential backoff

## Environment Variables

For production deployment:
- `PORT` - Server port (default: 5000)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - feel free to use in your projects!

## Support

For issues and questions:
- Check the API documentation at the root endpoint
- Review error messages for debugging
- Test endpoints locally before deploying

---

**Happy trending! 📈**