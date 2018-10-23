from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

with open(jobs.json,"r") as job_file:
    jobs_data = json.loads(job_file.read())[0]


@app.route('/')
def jobs_route():
    return render_template(
        "jobs.html",
        jobs = all_jobs,
        )
