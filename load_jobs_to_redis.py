import datetime, redis, os, collect, json

jobs = json.dumps(collect.scraper())

r = redis.from_url(os.environ.get("REDIS_URL"))
r.flushall()
r.set('jobs', jobs)
r.set('time', str(datetime.datetime.now()))
