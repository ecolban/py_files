

def get_start_time(schedules, duration):

    def to_int(time):
        hm = time.split(':')
        return 60 * int(hm[0]) + int(hm[1])

    def to_str(n):
        return '%02d:%02d' % (n / 60, n % 60)
    
    busy_times = [map(to_int, m) for sch in schedules for m in sch]
    busy_times.sort(key=lambda x: x[0])
    start = 9 * 60 # 9:00
    for x in busy_times:
        if start + duration <= x[0]:
            return to_str(start)
        start = max(start, x[1])
    if start + duration <= 19 * 60: # 19:00
        return to_str(start)

    return None


schedules = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]
            
