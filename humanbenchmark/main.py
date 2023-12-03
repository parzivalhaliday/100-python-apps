import tkinter as tk
import time
import random

def start_test():
    def end_test():
        nonlocal start_time
        end_time = time.time()
        reaction_time = end_time - start_time
        result_label.config(text=f"Tepki süreniz: {reaction_time:.3f} saniye")
        start_button.config(state=tk.NORMAL)

    def change_color():
        button.config(bg="red")
        button.after(random.randint(2000, 5000), lambda: button.config(bg="green"))
        root.bind("<space>", lambda event: end_test())

    start_time = time.time()
    start_button.config(state=tk.DISABLED)
    result_label.config(text="")
    
    button = tk.Button(root, text="Başla", font=("Arial", 24), command=start_test)
    button.pack(pady=50)
    
    button.config(bg="green")
    change_color()

root = tk.Tk()
root.title("Tepki Süresi Testi")
root.geometry("400x300")

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

restart_button = tk.Button(root, text="Yeniden Başlat", font=("Arial", 16), command=lambda: start_test())
restart_button.pack(pady=20)

root.mainloop()
