from flask import Flask
from flask import render_template
import json

app = Flask(__name__)



@app.route('/')
def jobs_route():
    with open("jobs.json","r") as job_file:
        jobs_data = json.loads(job_file.read())
    return render_template(
        "jobs.html",
        jobs = jobs_data,
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
