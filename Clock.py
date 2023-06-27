import time

def pomodoro_timer(total_time, focus_time, break_time):
    cycles = total_time // (focus_time + break_time)
    remaining_time = total_time % (focus_time + break_time)

    for i in range(cycles):
        print("Focus mode: {} minutes".format(focus_time))
        time.sleep(focus_time * 60)  # 转换为秒

        print("Break mode: {} minutes".format(break_time))
        time.sleep(break_time * 60)  # 转换为秒

    if remaining_time > 0:
        print("Focus mode: {} minutes".format(remaining_time))
        time.sleep(remaining_time * 60)  # 转换为秒

    print("Pomodoro timer finished!")

# 设置总时间为60分钟，专注时间为25分钟，休息时间为5分钟
pomodoro_timer(60, 25, 5)
