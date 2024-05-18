import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.geometry("700x300")
root.title("Sortify - File Management")
window_title = Label(root, text="File Management", font=("Arial", 45))
window_title.pack()

# path = r"C:/Users/Sean__38/Downloads/"
folder_names = ["PDF Files", "Word Documents", "Image Files", "Video Files", "Music Files", "App Files", "PowerPoint Files", "Zip Files", "Excel Files"]




def sort_files():
    path = filedialog.askdirectory()
    file_names = os.listdir(path)

    for folder_name in folder_names:
        if not os.path.exists(os.path.join(path, folder_name)):
            os.makedirs(os.path.join(path, folder_name))

    for file in file_names:
        if file.endswith(".pdf") and not os.path.exists(os.path.join(path, "PDF Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "PDF Files", file))
        elif file.endswith((".docx", ".doc")) and not os.path.exists(os.path.join(path, "Word Documents", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Word Documents", file))
        elif file.endswith((".png", ".jpeg", ".svg", ".webp")) and not os.path.exists(
                os.path.join(path, "Image Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Image Files", file))
        elif file.endswith((".mp4", ".webm", ".mkv")) and not os.path.exists(os.path.join(path, "Video Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Video Files", file))
        elif file.endswith((".mp3", ".m4a")) and not os.path.exists(os.path.join(path, "Music Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Music Files", file))
        elif file.endswith((".exe", ".msi")) and not os.path.exists(os.path.join(path, "App Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "App Files", file))
        elif file.endswith(".pptx") and not os.path.exists(os.path.join(path, "Powerpoint Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Powerpoint Files", file))
        elif file.endswith(".zip") and not os.path.exists(os.path.join(path, "Zip Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Zip Files", file))
        elif file.endswith(".xlsx") and not os.path.exists(os.path.join(path, "Excel Files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "Excel Files", file))

def widgets():
    folder_lbl = Label(root, text="Choose a folder to sort: ")
    folder_lbl.pack()

    sort_btn = Button(root, text="Choose", command=sort_files)
    sort_btn.pack()

def main():
    widgets()
    root.mainloop()


if __name__ == "__main__":
    main()