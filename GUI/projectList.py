import tkinter.ttk as tkt
from GUI.config.process import *


class ProcessList(tkt.Treeview):
    def __init__(self, root):
        super(ProcessList, self).__init__(root, columns=get_columns())

        # Columns param
        for (col_id, col_name, col_size) in get_col_config():
            self.heading(col_id, text=col_name)
            self.column(col_id, width=col_size)
        self["show"] = "headings"

        self.__add_categories()
        self.__add_default_process()
        self.__set_style()

        self.pack(side="left", fill="y")

    def __add_default_process(self):
        for proc in DEFAULT_PROC:
            self.add_process(proc)

    def __add_categories(self):
        first = True
        for (cat_id, cat_name, multiple) in get_categories():
            si = ""
            if multiple:
                si = "v"

            self.insert('', 'end', cat_id, values=(si, cat_name), tags=("simple", CATEGORY_TAG,))

            if first:
                self.selection_set(cat_id)
                first = False

    def __set_style(self):
        self.tag_configure(CATEGORY_TAG, background="#FFFF00")

    def add_process(self, proc: Tuple[str, str, str]) -> None:
        """
        Add a process into the list

        :param proc: (cat, proc_id, proc_name)
        """
        self.insert(proc[0], 'end', proc[1], values=("0", proc[2]), tags=("simple"))
