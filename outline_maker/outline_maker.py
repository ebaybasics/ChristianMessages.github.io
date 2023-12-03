import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def add_point(section_points_frame):
    point_frame = ttk.Frame(section_points_frame)
    point_frame.pack(fill="x", pady=(5, 0))

    point_title_label = ttk.Label(point_frame, text="Point Title:")
    point_title_label.pack(side="left")
    point_title_entry = ttk.Entry(point_frame)
    point_title_entry.pack(side="left", padx=(0, 5))
    point_titles.append(point_title_entry)

    context_label = ttk.Label(point_frame, text="Context:")
    context_label.pack(side="left")
    context_entry = ttk.Entry(point_frame)
    context_entry.pack(side="left", padx=(0, 5))
    contexts.append(context_entry)

    bible_reference_label = ttk.Label(point_frame, text="Bible Reference:")
    bible_reference_label.pack(side="left")
    bible_reference_entry = ttk.Entry(point_frame)
    bible_reference_entry.pack(side="left", padx=(0, 5))
    bible_references.append(bible_reference_entry)

def add_section():
    section_title_entry = ttk.Entry(sections_frame)
    section_title_entry.pack(fill="x", pady=(5, 0))
    section_entries.append(section_title_entry)

    section_points_frame = ttk.Frame(sections_frame)
    section_points_frame.pack(fill="x")
    section_points_frames.append(section_points_frame)

    add_point(section_points_frame)

    add_point_button = ttk.Button(section_points_frame, text="Add Point", command=lambda: add_point(section_points_frame))
    add_point_button.pack(side="right")

def save_html():
    title = title_entry.get()
    flagship_verse = flagship_verse_entry.get()

    max_points = max([len(point_titles[i::len(section_entries)]) for i in range(len(section_entries))])

    sections = ""
    for point_index in range(max_points):
        point_list = []
        for i, section_title_entry in enumerate(section_entries):
            if point_index < len(point_titles[i::len(section_entries)]):
                point_title = point_titles[i::len(section_entries)][point_index].get()
                context = contexts[i + point_index * len(section_entries)].get()
                bible_reference = bible_references[i + point_index * len(section_entries)].get()

                point_list.append(f'<li><span class="highlight">{point_title}</span> {context} <b>{bible_reference}</b></li>')

        sections += f"""
        <div>
            <ul>
                {''.join(point_list)}
            </ul>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
    <a href="../index.html"> Home </a>
    <a href="./additional_notes/additional_notes_template.html"> Additional Notes </a>
    <h1>Title: {title}</h1>
    <h3>Flagship Verse: {flagship_verse}</h3>

        {sections}

</body>
</html>"""

    file_path = filedialog.asksaveasfilename(defaultextension=".html")
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html)
        messagebox.showinfo("Success", "HTML file saved successfully!")

root = tk.Tk()
root.title("HTML Outline Builder")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

title_label = ttk.Label(mainframe, text="Title:")
title_label.grid(column=0, row=0, sticky=(tk.W, tk.E))
title_entry = ttk.Entry(mainframe)
title_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

flagship_verse_label = ttk.Label(mainframe, text="Flagship Verse:")
flagship_verse_label.grid(column=0, row=1, sticky=(tk.W, tk.E))
flagship_verse_entry = ttk.Entry(mainframe)
flagship_verse_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

sections_label = ttk.Label(mainframe, text="Sections:")
sections_label.grid(column=0, row=2, sticky=(tk.W, tk.E))

# create a Canvas widget and place it using grid()
canvas = tk.Canvas(mainframe, width=1000)
canvas.grid(column=1, row=2, sticky=(tk.W, tk.E))

# create a Scrollbar widget and place it using grid()
scrollbar = ttk.Scrollbar(mainframe, orient="vertical", command=canvas.yview)
scrollbar.grid(column=2, row=2, sticky=(tk.NS, tk.E))

# create a Horizontal Scrollbar widget and place it using grid()
hscrollbar = ttk.Scrollbar(mainframe, orient="horizontal", command=canvas.xview)
hscrollbar.grid(column=1, row=3, sticky=(tk.EW, tk.S))

# configure the Canvas widget to use the Scrollbar
canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=hscrollbar.set)

sections_frame = ttk.Frame(canvas, height=8000)
canvas.create_window((0, 0), window=sections_frame, anchor='nw')

add_section_button = ttk.Button(mainframe, text="Add Section", command=add_section)
add_section_button.grid(column=1, row=3, sticky=(tk.W, tk.E))

save_button = ttk.Button(mainframe, text="Save HTML", command=save_html)
save_button.grid(column=1, row=4, sticky=(tk.W, tk.E))

section_entries = []
section_points_frames = []
point_titles = []
contexts = []
bible_references = []

add_section()

# configure the rows and columns of the mainframe to expand
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mainframe.grid_rowconfigure(2, weight=1)
mainframe.grid_columnconfigure(1, weight=1)

# make the scrollbars stick to the right and bottom as the window gets larger
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.mainloop()







