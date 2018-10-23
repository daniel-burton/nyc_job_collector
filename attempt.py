import re
import time
import requests
import csv

all_sites = ['cas', 'cig', 'fap', 'itt', 'poa', 'soc', 'cbs', 'eap', 'hlt',
             'leg', 'mop', 'psi']
# the list of job categories

root = ('https://a127-jobs.nyc.gov/psc/nycjobs/EMPLOYEE/HRMS/c'
        '/HRS_HRAM.HRS_APP_SCHJOB.GBL?FOCUS=Applicant&category=')
# root is the basic address for getting the HTML of the job entries, usually
# fetched by the javascript on the NYC jobs explorer site. Add the category at
# the end to get full address.

address = ("https://a127-jobs.nyc.gov/psc/nycjobs/EMPLOYEE/HRMS/c"
          "/HRS_HRAM.HRS_APP_SCHJOB.GBL?Page=HRS_APP_JBPST&Action"
          "=U&FOCUS=Applicant&SiteId=1&JobOpeningId={}&PostingSeq=1")
# address is for generating the permalinks using job id

reg_ex = (r"Display details of (.+\s)- (\d\d\d\d\d\d)'.+\n.+<b>Department:</b>"
          r"(.*?\s)\s+\|.+<b>Agency:</b>\s(.*?\s)\s+\|")

entry = re.compile(reg_ex)

for site in all_sites:
    """this iterates through the categories, fetches the HTML, uses the regex
    to find the jobs, writes them to the csv."""
    full_address = root + site
    full_page = requests.get(full_address)
    jobs = re.findall(entry, full_page.text)
    with open('./jobs.csv','w') as out:
        outwrite = csv.writer(out)
        for title, number, department, agency in jobs:
            dash = title.find('-')
            office = agency + ": " + department
            permalink = address.format(number)
            outwrite.writerow([site, office, number, title[:dash],
                               permalink])
    time.sleep(5)
