import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound

work_time = 25 * 60
long_work_time = 60 * 60
break_time = 5 * 60
long_break_time = 10 * 60
timer_running = False

def countdown(seconds):
    global timer_running
    minutes, sec = divmod(seconds, 60)
    time_var.set(f"{minutes:02}:{sec:02}")
    if seconds > 0 and timer_running:
        root.after(1000, countdown, seconds - 1)
    elif seconds == 0:
        playsound("alarm_sound.mp3")
        show_break_message()

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        duration = work_time if break_type.get() == "short" else long_work_time
        countdown(duration)

def reset_timer():
    global timer_running
    timer_running = False
    time_var.set("25:00" if break_type.get() == "short" else "60:00")

def show_break_message():
    global timer_running
    timer_running = False
    messagebox.showinfo("Time's up!", "Time to take a break!")
    countdown(break_time if break_type.get() == "short" else long_break_time)

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("800x500")
root.resizable(False, False)

bg_image = Image.open("Background.jpg").convert("RGBA").resize((800, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

time_var = tk.StringVar(value="25:00")
time_label = tk.Label(root, textvariable=time_var, font=("Helvetica", 48, "bold"), fg="white", bg="#000000", bd=0)
time_label.place(relx=0.5, rely=0.4, anchor="center")

start_button = tk.Button(root, text="Start", font=("Helvetica", 18), command=start_timer, bg="#4CAF50", fg="white")
start_button.place(relx=0.4, rely=0.55, anchor="center", width=100, height=40)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 18), command=reset_timer, bg="#f44336", fg="white")
reset_button.place(relx=0.6, rely=0.55, anchor="center", width=100, height=40)

break_type = tk.StringVar(value="short")
short_break_radio = tk.Radiobutton(root, text="Short Break", variable=break_type, value="short", bg="#E0218A", fg="white")
long_break_radio = tk.Radiobutton(root, text="Long Break", variable=break_type, value="long", bg="#008000", fg="white")
short_break_radio.place(relx=0.35, rely=0.65, anchor="center")
long_break_radio.place(relx=0.65, rely=0.65, anchor="center")

root.mainloop()
