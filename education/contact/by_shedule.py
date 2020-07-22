from datetime import datetime, timedelta
from redis import Redis
from views import contact_view
from rq_scheduler import Scheduler

scheduler = Scheduler(connection=Redis())
# 20 часов 41 минута
# 20 - 3 время в UTC
# Запуск в определенное время
# scheduler.enqueue_at(datetime(2020, 4, 27, 21 - 3, 1), get_currency_rate, 'USD')
# Запуск с задержкой
scheduler.enqueue_in(timedelta(seconds=5), contact_view)

# scheduler.schedule(...) - можно настроить запуск по расписанию