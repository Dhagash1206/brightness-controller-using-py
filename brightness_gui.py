import tkinter as tk
import subprocess

NIRC_EXECUTABLE_PATH = r"C:\Users\dhagash\Desktop\nircmd-x64\nircmd.exe"

def apply_brightness():
    brightness_value = brightness_slider.get()
    subprocess.run(
        [NIRC_EXECUTABLE_PATH, "setbrightness", str(brightness_value)],
        check=False
    )

def preset_brightness(value):
    brightness_slider.set(value)
    apply_brightness()

main_window = tk.Tk()
main_window.title("Brightness Controller")
main_window.geometry("420x260")
main_window.configure(bg="#0b1412")

tab_bar = tk.Frame(main_window, bg="#08100e", height=40)
tab_bar.pack(fill="x", side="top")

tk.Label(
    tab_bar, text="Brightness Controller",
    bg="#08100e", fg="#6fe3c1",
    font=("Segoe UI", 11, "bold")
).pack(pady=8)

content_frame = tk.Frame(main_window, bg="#0f1f1b")
content_frame.pack(fill="both", expand=True, padx=15, pady=15)

brightness_slider = tk.Scale(
    content_frame, from_=0, to=100, orient="horizontal",
    bg="#0f1f1b", fg="#cfeee6",
    troughcolor="#1e3a32", length=300,
    highlightthickness=0
)
brightness_slider.set(60)
brightness_slider.pack(pady=10)

preset_frame = tk.Frame(content_frame, bg="#0f1f1b")
preset_frame.pack(pady=6)

for preset_value in [25, 50, 75, 100]:
    tk.Button(
        preset_frame, text=f"{preset_value}%",
        bg="#132925", fg="#cfeee6",
        activebackground="#1f4d42",
        relief="flat", width=6,
        command=lambda value=preset_value: preset_brightness(value)
    ).pack(side="left", padx=5)

tk.Button(
    content_frame, text="Apply",
    bg="#f4b942", fg="#0b1412",
    activebackground="#ffd36a",
    relief="flat", width=24,
    command=apply_brightness
).pack(pady=15)

main_window.mainloop()
