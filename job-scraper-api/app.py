from flask import Flask, jsonify, request
from jobspy import scrape_jobs

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def get_jobs():
    # Get parameters from the URL, with default values if not provided
    search_term = request.args.get('search_term', 'software engineer')
    location = request.args.get('location', 'India')
    
    print(f"Scraping for '{search_term}' in '{location}'...")

    try:
        jobs_df = scrape_jobs(
            site_name=["indeed", "linkedin", "naukri"],
            search_term=search_term,
            location=location,
            results_wanted=5
        )
        
        results = jobs_df.to_dict('records')
        print(f"Found {len(results)} jobs. Sending response.")
        return jsonify(results)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)