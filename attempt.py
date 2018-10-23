import re
import requests
import csv

all_sites = ['cas', 'cig', 'fap', 'itt', 'poa', 'soc', 'cbs', 'eap', 'hlt',
             'leg', 'mop', 'psi']

root = ('https://a127-jobs.nyc.gov/psc/nycjobs/EMPLOYEE/HRMS/c'
        '/HRS_HRAM.HRS_APP_SCHJOB.GBL?FOCUS=Applicant&category=')

full_sites = [root + site for site in all_sites]

all_jobs = [] #will contain list of lists of tuples, each tuple is job details

for site in full_sites:
    all_jobs.append(requests.get(site))


address = "https://a127-jobs.nyc.gov/psc/nycjobs/EMPLOYEE/HRMS/c/HRS_HRAM.HRS_APP_SCHJOB.GBL?Page=HRS_APP_JBPST&Action=U&FOCUS=Applicant&SiteId=1&JobOpeningId={}&PostingSeq=1"

entry = re.compile(r"Display details of (.+) - (\d\d\d\d\d\d)")

for this_job in all_jobs:
    jobs.append(re.findall(entry, thisjob.text))

with open('./jobs.csv',"w") as out:
    outwrite = csv.writer(out)
    for title, number in jobs:
        location = title.find('-')
        outwrite.writerow(number, title[:location],address.format(number))

#print(jobs)
