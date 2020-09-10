import time
from rq import Queue
from redis import Redis
from .tasks import contact_view

redis_conn = Redis()
queue = Queue(connection=redis_conn)
job = queue.enqueue(contact_view, 'http://127.0.0.1:8000/contact/')
#  job = contact_view.delay('POST')
print(job.result)
time.sleep(5)
print(job.result)
