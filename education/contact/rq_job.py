import time
from rq import Queue
from redis import Redis
from .views import contact_view

queue = Queue(connection=Redis())


job = queue.enqueue(contact_view, 'contact/contact.html')

time.sleep(5)
print(job)
