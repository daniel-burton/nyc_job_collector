from flask import Flask
from flask import render_template
import json
import collect

app = Flask(__name__)



@app.route('/')
def jobs_route():
    with open("jobs.json","r") as job_file:
        jobs_data = json.loads(job_file.read())
    with open("job_log.txt","r") as log_file:
        log = log_file.readline()
    return render_template(
        "jobs.html",
        jobs = jobs_data,
        updated = log
        )

if __name__ == '__main__':
    app.run()
