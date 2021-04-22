from datetime import datetime, timedelta


start = datetime.strptime('20180101', '%Y%m%d').date()
dt_now = datetime.now().date().isoformat().replace('-', '')
end = datetime.strptime(dt_now, '%Y%m%d').date()


def daterange_strings(start=start, end=end):
    for n in range((end - start).days):
        dt = start + timedelta(n)
        yield dt
