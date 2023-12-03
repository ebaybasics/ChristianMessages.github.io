import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HTML Editor")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Add a label and entry for the title
        title_label = ttk.Label(self, text="Title:")
        title_label.pack(pady=10)
        self.title_entry = ttk.Entry(self)
        self.title_entry.pack()

        # Add a label and entry for the flagship verse
        verse_label = ttk.Label(self, text="Flagship Verse:")
        verse_label.pack(pady=10)
        self.verse_entry = ttk.Entry(self)
        self.verse_entry.pack()

        # Add a button to add a new section
        add_button = ttk.Button(self, text="Add Section", command=self.add_section)
        add_button.pack(pady=10)

        # Add a button to save the HTML code to a file
        save_button = ttk.Button(self, text="Save to File", command=self.save_file)
        save_button.pack(pady=10)

        # Add a scrollable frame to hold the sections
        scrollable_frame = ttk.Frame(self)
        scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollable_frame.columnconfigure(0, weight=1)
        scrollable_frame.rowconfigure(0, weight=1)

        canvas = tk.Canvas(scrollable_frame)
        canvas.grid(column=0, row=0, sticky="nsew")
        canvas.config(width=780, height=400, scrollregion=canvas.bbox("all"))

        scrollbar = ttk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(column=1, row=0, sticky="ns")

        canvas.config(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

        self.sections_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.sections_frame, anchor="nw")

    def add_section(self):
        section_frame = ttk.Frame(self.sections_frame, borderwidth=2, relief="groove")
        section_frame.pack(pady=10, fill=tk.X)

        # Add a label and entry for the section title
        title_label = ttk.Label(section_frame, text="Section Title:")
        title_label.pack(side=tk.LEFT, padx=10, pady=5)
        title_entry = ttk.Entry(section_frame)
        title_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

        # Add a label and entry for the section flagship verse
        verse_label = ttk.Label(section_frame, text="Flagship Verse:")
        verse_label.pack(side=tk.LEFT, padx=10, pady=5)
        verse_entry = ttk.Entry(section_frame)
        verse_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

        # Add a button to add a new row to the section
        add_button = ttk.Button(section_frame, text="Add Row", command=lambda: self.add_row(section_frame))
        add_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Add a button to remove the section
        remove_button = ttk.Button(section_frame, text="Remove", command=lambda:section_frame.destroy())
        remove_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Add a frame to hold the rows
        rows_frame = ttk.Frame(section_frame)
        rows_frame.pack(fill=tk.X, padx=10, pady=5)

        # Store the section data in a dictionary
        section_data = {
            "title_entry": title_entry,
            "verse_entry": verse_entry,
            "rows_frame": rows_frame,
            "rows_data": []
        }

        # Add the section data to the sections list
        self.sections.append(section_data)

    def add_row(self, section_frame):
        # Get the section data for the section containing the given frame
        section_data = next((s for s in self.sections if s["rows_frame"] is section_frame), None)

        if section_data is not None:
            # Add a row to the section
            row_frame = ttk.Frame(section_data["rows_frame"])
            row_frame.pack(fill=tk.X, padx=10, pady=5)

            # Add a label and entry for the highlight
            highlight_label = ttk.Label(row_frame, text="Highlight:")
            highlight_label.pack(side=tk.LEFT, padx=10, pady=5)
            highlight_entry = ttk.Entry(row_frame)
            highlight_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

            # Add a label and entry for the context
            context_label = ttk.Label(row_frame, text="Context:")
            context_label.pack(side=tk.LEFT, padx=10, pady=5)
            context_entry = ttk.Entry(row_frame)
            context_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

            # Add a label and entry for the Bible reference
            ref_label = ttk.Label(row_frame, text="Bible Reference:")
            ref_label.pack(side=tk.LEFT, padx=10, pady=5)
            ref_entry = ttk.Entry(row_frame)
            ref_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

            # Store the row data in a dictionary
            row_data = {
                "highlight_entry": highlight_entry,
                "context_entry": context_entry,
                "ref_entry": ref_entry
            }

            # Add the row data to the section data
            section_data["rows_data"].append(row_data)
    def save_file(self):
        # Get the title entered by the user
        title = self.title_entry.get()

        if not title:
            mb.showerror("Error", "Please enter a title.")
            return

        # Create the HTML code
        html = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<title>{title}</title>\n<link rel=\"stylesheet\" href=\"/css/styles.css\">\n</head>\n<body>\n<a href=\"../index.html\">Home</a>\n<a href=\"./additional_notes/additional_notes_template.html\">Additional Notes</a>\n<h1>{title}</h1>\n<h3>{self.verse_entry.get()}</h3>\n<ul>\n"

        for section_data in self.sections:
            # Get the section title and flagship verse entered by the user
            section_title = section_data["title_entry"].get()
            section_verse = section_data["verse_entry"].get()

            if not section_title:
                mb.showerror("Error", "Please enter a section title.")
                return

            html += f"<li><h2>{section_title}</h2><h3>{section_verse}</h3><ul>"

            for row_data in section_data["rows_data"]:
                # Get the highlight, context, and Bible reference entered by the user
                highlight = row_data["highlight_entry"].get()
                context = row_data["context_entry"].get()
                ref = row_data["ref_entry"].get()

                html += f"<li><span class=\"highlight\">{highlight}</span>{context}<b>{ref}</b></li>"

            html += "</ul></li>"

        html += "</ul></body>\n</html>"

        # Save the HTML code to a file with the specified name
        filename = f"{title}.html"

        with open(filename, "w") as f:
            f.write(html)

        mb.showinfo("Success", f"The HTML code has been saved to {filename}.")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.sections = []
    app.run()
