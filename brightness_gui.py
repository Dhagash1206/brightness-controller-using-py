import tkinter as tk
import subprocess

NIRC_EXECUTABLE_PATH = r"C:\Users\dhagash\Desktop\nircmd-x64\nircmd.exe"

def apply_brightness():
    brightness_value = brightness_slider.get()
    subprocess.run(
        [NIRC_EXECUTABLE_PATH, "setbrightness", str(brightness_value)],
        check=False
    )

main_window = tk.Tk()
main_window.title("Brightness Controller")
main_window.geometry("300x150")
main_window.configure(bg="#2e2e2e")

brightness_slider = tk.Scale(
    main_window,
    from_=0,
    to=100,
    orient="horizontal",
    label="Brightness",
    bg="#2e2e2e",
    fg="white",
    troughcolor="#555555",
    highlightthickness=0
)
brightness_slider.set(60)
brightness_slider.pack(pady=10)

apply_button = tk.Button(
    main_window,
    text="Apply",
    bg="#444444",
    fg="white",
    activebackground="#666666",
    command=apply_brightness
)
apply_button.pack()

main_window.mainloop()
