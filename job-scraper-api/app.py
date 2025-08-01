from flask import Flask
from jobspy import scrape_jobs
import jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def get_jobs():
    try:
        jobs_df = scrape_jobs(
            site_name=["indeed", "linkedin", "naukri"],
            search_term="software engineer",
            location="India",
            results_wanted=25,
            hours_old=48,
            country_indeed='IND'
        )
        
        results = jobs_df.to_dict('records')
        print(f"Found {len(results)} jobs. Sending response.")
        
        return jsonify(results)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # '0.0.0.0' makes the server accessible from your local network (and Docker)
    app.run(host='0.0.0.0', port=5000, debug=True)