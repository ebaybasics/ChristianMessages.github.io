import tkinter as tk
from tkinter import ttk

class HtmlEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("HTML Editor")
        self.geometry("800x600")

        # Title input
        tk.Label(self, text="Title:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=0, column=1, sticky="we", padx=5)

        # Flagship Verse input
        tk.Label(self, text="Flagship Verse:").grid(row=1, column=0, sticky="w")
        self.verse_entry = tk.Entry(self)
        self.verse_entry.grid(row=1, column=1, sticky="we", padx=5)

        # Sections and rows
        self.sections_frame = tk.Frame(self)
        self.sections_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Add section button
        self.add_section_button = tk.Button(self, text="Add Section", command=self.add_section)
        self.add_section_button.grid(row=3, column=0, sticky="w", padx=5)

        # Save button
        self.save_button = tk.Button(self, text="Save HTML", command=self.save_html)
        self.save_button.grid(row=3, column=1, sticky="e", padx=5)

        self.sections = []

    def add_section(self):
        section = Section(self.sections_frame)
        section.pack(fill="both", expand=True, padx=5, pady=5)
        self.sections.append(section)

    def save_html(self):
        file_name = self.title_entry.get().strip()
        if file_name:
            file_name += ".html"

            content = "<!DOCTYPE html>\n"
            content += '<html lang="en">\n'
            content += "<head>\n"
            content += '    <meta charset="UTF-8">\n'
            content += "    <title>" + self.title_entry.get() + "</title>\n"
            content += "</head>\n"
            content += "<body>\n"
            content += "    <h1>" + self.title_entry.get() + "</h1>\n"
            content += "    <h3>" + self.verse_entry.get() + "</h3>\n"
            content += "    <ul>\n"

            for section in self.sections:
                content += section.get_html()

            content += "    </ul>\n"
            content += "</body>\n"
            content += "</html>"

            with open(file_name, "w") as file:
                file.write(content)

class Section(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Section title input
        self.title_entry = tk.Entry(self)
        self.title_entry.pack(fill="x", padx=5)

        self.rows_frame = tk.Frame(self)
        self.rows_frame.pack(fill="both", expand=True, padx=5)

        # Add row button
        self.add_row_button = tk.Button(self, text="Add Row", command=self.add_row)
        self.add_row_button.pack(padx=5)

        self.rows = []

    def add_row(self):
        row = Row(self.rows_frame)
        row.pack(fill="x", padx=5, pady=5)
        self.rows.append(row)

    def get_html(self):
        content = ""
        content += "        <h2>" + self.title_entry.get() + "</h2>\n"
        content += "        <ul>\n"
        for row in self.rows:
            content += row.get_html()

        content += "        </ul>\n"

        return content

class Row(tk.Frame):
    def init(self, parent):
        super().init(parent)
        self.topic_entry = tk.Entry(self)
        self.topic_entry.pack(side="left", fill="x", expand=True, padx=5)

        self.context_entry = tk.Entry(self)
        self.context_entry.pack(side="left", fill="x", expand=True, padx=5)

        self.reference_entry = tk.Entry(self)
        self.reference_entry.pack(side="left", fill="x", expand=True, padx=5)

    def get_html(self):
        content = "            <li><span class=\"highlight\">" + self.topic_entry.get() + "</span> "
        content += self.context_entry.get() + " <b>" + self.reference_entry.get() + "</b></li>\n"
        return content



app = HtmlEditor()
app.mainloop()
