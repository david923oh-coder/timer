import tkinter as tk
import time
import webbrowser


# Start at:
# 15 Minutes, 15 Seconds, 15 Milliseconds,
# 15 Microseconds, 15 Nanoseconds
START_MINUTES = 15
START_SECONDS = 15
START_MILLISECONDS = 15
START_MICROSECONDS = 15
START_NANOSECONDS = 15


START_TIME = (
    START_MINUTES * 60
    + START_SECONDS
    + START_MILLISECONDS / 1000
    + START_MICROSECONDS / 1_000_000
    + START_NANOSECONDS / 1_000_000_000
)


END_MESSAGE = "【MAD/AMV】アスカ・ラングレー × this is the dream (裏コード999 BGM)"


time_left = START_TIME
last_time = time.perf_counter()
running = True
video_opened = False




def update_timer():
    global time_left, last_time, video_opened


    now = time.perf_counter()


    if running and time_left > 0:
        elapsed = now - last_time
        time_left -= elapsed


        if time_left < 0:
            time_left = 0


    last_time = now


    if time_left <= 0:
        timer_label.config(
            text=END_MESSAGE,
            font=("Arial", 18)
        )


        if not video_opened:
            webbrowser.open("https://www.youtube.com/watch?v=0rDWyS2m6M4")
            video_opened = True


        return


    hours = int(time_left // 3600)
    minutes = int((time_left % 3600) // 60)
    seconds = int(time_left % 60)


    fraction = time_left % 1


    milliseconds = int(fraction * 1000) % 1000
    microseconds = int(fraction * 1_000_000) % 1000
    nanoseconds = int(fraction * 1_000_000_000) % 1000


    timer_label.config(
        text=(
            f"{hours:02}:"
            f"{minutes:02}:"
            f"{seconds:02}:"
            f"{milliseconds:03}:"
            f"{microseconds:03}:"
            f"{nanoseconds:03}"
        ),
        font=("Arial", 30)
    )


    root.after(1, update_timer)




def add_time():
    global time_left
    time_left += START_TIME




def subtract_time():
    global time_left
    time_left = max(0, time_left - START_TIME)




def stop_timer():
    global running


    running = not running


    if running:
        stop_button.config(text="Stop")
    else:
        stop_button.config(text="Start")




def restart_timer():
    global time_left, last_time, running, video_opened


    time_left = START_TIME
    last_time = time.perf_counter()
    running = True
    video_opened = False


    stop_button.config(text="Stop")


    update_timer()




root = tk.Tk()
root.title("Timer")
root.geometry("1400x500")


title_label = tk.Label(
    root,
    text="Hours : Minutes : Seconds : Milliseconds : Microseconds : Nanoseconds",
    font=("Arial", 20)
)
title_label.pack(pady=10)


timer_label = tk.Label(
    root,
    font=("Arial", 30)
)
timer_label.pack(pady=20)


add_button = tk.Button(
    root,
    text="Add 15m 15s 15ms 15us 15ns",
    bg="red",
    fg="white",
    font=("Arial", 16),
    command=add_time
)
add_button.pack(pady=5)


subtract_button = tk.Button(
    root,
    text="Subtract 15m 15s 15ms 15us 15ns",
    bg="orange",
    fg="white",
    font=("Arial", 16),
    command=subtract_time
)
subtract_button.pack(pady=5)


stop_button = tk.Button(
    root,
    text="Stop",
    bg="green",
    fg="white",
    font=("Arial", 16),
    command=stop_timer
)
stop_button.pack(pady=5)


restart_button = tk.Button(
    root,
    text="Restart",
    bg="blue",
    fg="white",
    font=("Arial", 16),
    command=restart_timer
)
restart_button.pack(pady=5)


update_timer()
root.mainloop()
