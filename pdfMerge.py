import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import ttkthemes

merger = PyPDF2.PdfMerger()
selected_theme = ttkthemes.ThemedStyle()
selected_theme.theme_use('equilux')

selected_theme.configure('BrowseButton.TButton', background='#70c1b3', font=('Helvetica', 12), relief="flat", borderwidth=10, padding=5, anchor="center", bordercolor="#ededed", focuscolor="none")
selected_theme.map('BrowseButton.TButton', background=[('active', '#5eaaa8')], bordercolor=[('active', '#ededed')])

def ask_for_file(button):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    merger.append(file_path)
    button.config(text=os.path.basename(file_path))

    root.update_idletasks()
    root.geometry(f"{col1.winfo_reqwidth()+50}x400")
        
def merge_pdf():
    if len(merger.inputs) < 2:
        tk.messagebox.showwarning("Error", "Please select two PDF files to merge.")
        return
    else:
        merger.write("combined.pdf")

    msg = "The PDF merging process is complete."
    popup = ttkthemes.ThemedTk()
    popup.get_themes()
    popup.set_theme("equilux")
    popup.title("File is ready!")
    popup.geometry("250x100")
    popup.resizable(False, False)
    popup.configure(background="#ededed")
    popup.attributes('-transparentcolor', "#ededed")
    popup.attributes('-alpha', 0.97)
    tk.Label(popup, text=msg).pack(pady=20)
    tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("equilux")
root.title("Merge PDF app")
root.resizable(False, False)
root.minsize(200, 300)
root.maxsize(800, 800)
root.grid_rowconfigure(0, weight=1, minsize=100)
root.grid_columnconfigure(0, weight=1, minsize=100)
root.configure(background="#ededed")
root.attributes('-transparentcolor', "#ededed")
root.attributes('-alpha', 0.97)

col1 = ttk.Frame(root, padding=(10, 10, 0, 0), borderwidth=0, relief="flat")
col1.grid(row=0, column=0, sticky="nsew")

btn_first_file = ttk.Button(col1, text="Browse", command=lambda: ask_for_file(btn_first_file), style="BrowseButton.TButton")
btn_first_file = ttk.Button(col1, text="Browse", command=lambda: ask_for_file(btn_first_file), style="BrowseButton.TButton")
btn_first_file.pack(pady=10, anchor="center")

btn_second_file = ttk.Button(col1, text="Browse", command=lambda: ask_for_file(btn_second_file), style="BrowseButton.TButton")
btn_second_file = ttk.Button(col1, text="Browse", command=lambda: ask_for_file(btn_second_file), style="BrowseButton.TButton")
btn_second_file.pack(pady=10, anchor="center")

btn_merge = ttk.Button(col1, text="Merge files")
btn_merge = ttk.Button(col1, text="Merge files", command=merge_pdf, style="MergeButton.TButton")
btn_merge.pack(pady=0, anchor="center")

root.mainloop()
