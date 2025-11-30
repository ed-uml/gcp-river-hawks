import functions_framework

@functions_framework.http
def hello_http(request):
    """
    Week 6 HTML page for GCP Cloud Function instead of plain text return through CURL
    """
    cloud_run_logo_url = "https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6883d202716f923df4558b3d_google-cloud-run.webp"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>River Hawk Cloud Deployment Week 6</title>
        
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        
        <style>
            body {{
                font-family: 'Roboto', sans-serif; 
                background-color: #004990; /* UML Blue */
                color: white; 
                text-align: center; 
                padding-top: 50px; 
            }}
            .header-logo {{
                display: block; 
                margin: 0 auto; 
                max-width: 300px; 
                height: auto; 
                margin-bottom: 25px; 
            }}
            .main-message {{
                font-size: 1.8em;
                margin-bottom: 30px;
                font-weight: bold;
            }}
            .cloud-run-logo {{
                max-height: 75px; 
                margin-left: 10px; 
                vertical-align: middle;
            }}
        </style>
    </head>
    <body>
        <img src="https://a.espncdn.com/i/teamlogos/ncaa/500-dark/2349.png" 
             alt="UMass Lowell River Hawks" 
             class="header-logo">

        <p style="margin-top: 50px; font-size: 1.8em;">
            Served by Google 
            <img src="{cloud_run_logo_url}" alt="Google Cloud Run Logo" class="cloud-run-logo">
        </p>
    </body>
    </html>
    """
    
    # Return Code 200
    return html_content, 200, {'Content-Type': 'text/html'}
