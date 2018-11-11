import re, time, requests, json, datetime


def scraper():
    with open("job_log.txt","w") as job_log:
        job_log.write(str(datetime.datetime.now()))
    all_sites = ['cas', 'cig', 'fap', 'itt', 'poa', 'soc', 'cbs', 'eap', 'hlt',
                 'leg', 'mop', 'psi']
    # the list of job categories
    category = {'cas':"Administration and HR",
                'cig': "Communications and Intergovernmental affairs",
                'fap': "Finance, Accounting, and Procurement",
                'itt': "Technology, Data, and Innovation",
                'poa': "Policy, Research, and Analysis",
                'soc': "Social Services",
                'cbs': "Constituent Services & Community Programs",
                'eap': "Engineering, Infrastructure, and Planning",
                'hlt': "Health",
                'leg': "Legal Affairs",
                'mop': "Building Operations and Maintenance",
                'psi': "Public Safety, Inspections, and Enforcement"}

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
    # this regex finds the places in the HTML where job title, agency,
    # department and identifier are listed

    entry = re.compile(reg_ex)

    jobs_list = []

    for site in all_sites:
        """this iterates through the categories, fetches the HTML, uses the regex
        to find the jobs, writes them to the json."""
        full_address = root + site
        full_page = requests.get(full_address)
        jobs = re.findall(entry, full_page.text)
        for title, number, department, agency in jobs:
            dash = title.find('-')
            #find location of the dash in the job title, to separate title from #
            permalink = address.format(number)
            job_entry = {"title": title[: dash], "id": number,
                         "department": department, "agency": agency,
                         "category":category[site], "link": permalink}
            jobs_list.append(job_entry)
        time.sleep(5)

    jobs_list = sorted(jobs_list, key=lambda k: k['department'])
    with open("jobs.json", "w") as fp:
        json.dump(jobs_list, fp, indent=4)

if __name__ == "__main__":
    scraper()

# VERSION THAT USED CSV
#    with open('./jobs.csv','w') as out:
#        outwrite = csv.writer(out)
#        for title, number, department, agency in jobs:
#            dash = title.find('-')
#            office = agency + ": " + department
#            permalink = address.format(number)
#            outwrite.writerow([site, office, number, title[:dash],
#                               permalink])

