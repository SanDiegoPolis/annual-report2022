from count import count as count_data
import time

def offset_str(hour): # 传入str类型
    int_hour = (int(hour) - 6) % 24
    if int_hour < 10: return str(int_hour).zfill(2)
    else: return str(int_hour)

def deoffset_str(hour): # 传入str类型
    int_hour = (int(hour) + 6) % 24
    if int_hour < 10: return str(int_hour).zfill(2)
    else: return str(int_hour)

def juan():
    t0  = time.time()
    file_sender = './list/list_sender.txt'
    file_time = './list/list_time.txt'

    with open(file_sender, 'r', encoding='utf-8') as f:
        list_sender = [word.strip('\n') for word in f.readlines()]
    with open(file_time, 'r', encoding='utf-8') as f:
        list_time = [word.strip('\n') for word in f.readlines()]

    list_Y_M_D = []
    list_h_m_s = []
    for time1 in list_time:
        [Y_M_D, h_m_s] = time1.split('T')
        list_Y_M_D.append(Y_M_D)
        list_h_m_s.append(h_m_s)

    list_month = []
    list_date = []
    for Y_M_D in list_Y_M_D:
        [year, month, date] = Y_M_D.split('-')
        list_month.append(month)
        list_date.append(date)

    list_hour = []
    list_minute = []
    for h_m_s in list_h_m_s:
        [hour, minute, second] = h_m_s.split(':')
        list_hour.append(hour)
        list_minute.append(minute)

    sender, count = count_data() # 导入count.py

    month_latest = []
    date_latest = []
    hour_latest = []
    minute_latest = []
    hour_latest_morning = []
    minute_latest_morning = []
    month_earliest = []
    date_earliest = []
    hour_earliest = []
    minute_earliest = []
    
    for sender_id in sender:
        month_latest_i = '-1'
        date_latest_i = '-1'
        hour_latest_i = '06'
        minute_latest_i = '00'
        hour_latest_morning_i = '-1'
        minute_latest_morning_i = '-1'
        month_earliest_i = '-1'
        date_earliest_i = '-1'
        hour_earliest_i = '05'
        minute_earliest_i = '59'
        
        for i in range(len(list_sender)):
            if (list_sender[i] == sender_id):
                if (offset_str(list_hour[i]) >= offset_str(hour_latest_i)):
                    hour_latest_i = list_hour[i] # 最晚发言小时
                if (offset_str(list_hour[i]) <= offset_str(hour_earliest_i)):
                    hour_earliest_i = list_hour[i] # 最早发言小时
        hour_latest.append(hour_latest_i)
        hour_earliest.append(hour_earliest_i)

        for i in range(len(list_sender)):
            if (list_sender[i] == sender_id):
                if (list_minute[i] >= minute_latest_i and list_hour[i] == hour_latest_i):
                        minute_latest_i = list_minute[i] # 最晚发言分钟
                        month_latest_i = list_month[i]   # 最晚发言月份
                        date_latest_i = list_date[i]     # 最晚发言日期
                if (list_minute[i] <= minute_earliest_i and list_hour[i] == hour_earliest_i):
                        minute_earliest_i = list_minute[i] # 最早发言分钟
                        month_earliest_i = list_month[i]   # 最早发言月份
                        date_earliest_i = list_date[i]     # 最早发言日期
        minute_latest.append(minute_latest_i)
        month_latest.append(month_latest_i)
        date_latest.append(date_latest_i)
        minute_earliest.append(minute_earliest_i)
        month_earliest.append(month_earliest_i)
        date_earliest.append(date_earliest_i)
        
        for i in range(len(list_sender)):
            if (list_sender[i] == sender_id
                    and list_month[i] == month_latest_i and list_date[i] == date_latest_i
                    and list_hour[i] > hour_latest_i):
                morning_time = (list_hour[i], list_minute[i])
                if hour_latest_morning_i == '-1' or morning_time < (hour_latest_morning_i, minute_latest_morning_i):
                    hour_latest_morning_i, minute_latest_morning_i = morning_time
        hour_latest_morning.append(hour_latest_morning_i)
        minute_latest_morning.append(minute_latest_morning_i)
        
    # for obj in zip(month_latest, date_latest, hour_latest, minute_latest, hour_latest_morning, minute_latest_morning, month_earliest, date_earliest, hour_earliest, minute_earliest):
    #     print(obj)
    t1  = time.time()
    print(str(round(t1 - t0, 2)) + 's') # 测量运行时间

    return month_latest, date_latest, hour_latest, minute_latest, hour_latest_morning, minute_latest_morning, month_earliest, date_earliest, hour_earliest, minute_earliest

if __name__ == '__main__': 
    juan()