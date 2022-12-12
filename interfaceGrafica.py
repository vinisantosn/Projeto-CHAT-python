import tkinter
import tkinter.messagebox
import customtkinter

from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk


customtkinter.set_appearance_mode("System")  # Modes: "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Chat")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        
        # FIRST COLUMN
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # 1 -- LABEL: LOGO
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chat with Websockets in Python", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # 2 -- LABEL: vText
        self.vText_label = customtkinter.CTkLabel(self.sidebar_frame, text="Enter your username", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.vText_label.grid(row=1, column=0, padx=20, pady=(80,10))
        # 3 -- ENTRY: eText
        self.eText = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Type your username...")
        self.eText.grid(row=2, column=0,  padx=(20, 0), pady=(20, 5))
        # 4 -- BUTTON: btn
        self.btn = customtkinter.CTkButton(self.sidebar_frame, fg_color="transparent", text="Join",border_width=2, text_color=("gray10", "#DCE4EE"))
        self.btn.grid(row=3, column=0, padx=(20, 0), pady=0)
        # 5 -- LABEL: vText1
        self.vText1 = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.vText1.grid(row=5, column=0, padx=20, pady=(10, 0))
        # 6 -- SELECTIONBUTTON: seleBtn
        self.seleBtn = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.seleBtn.grid(row=6, column=0, padx=20, pady=(10, 10))
       

        # CREATE MAIN ENTRY AND BUTTON
        # 7 -- ENTRY: m_eText
        self.m_eText = customtkinter.CTkEntry(self, placeholder_text="Type your message...")
        self.m_eText.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # 8 -- BUTTON: m_btn
        self.m_btn = customtkinter.CTkButton(master=self, fg_color="transparent",  text="Send", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.m_btn.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # "SECOND" COLUMN 
        # CREATE README OF APP: textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.insert("0.0", "README \n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        #CREATE VIEW OF CHAT: message_box        

        # CREATE TEXTBOX VIEW CHAT FRAME
        self.message_box_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.message_box_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.message_box_frame.grid_columnconfigure(0, weight=1)
        self.message_box_frame.grid_rowconfigure(4, weight=1)        

        message_box = scrolledtext.ScrolledText(self.message_box_frame)
        # message_box.config(state=tkinter.DISABLED)
        message_box.pack(side=tkinter.TOP)

        self.open_new_window_frame = customtkinter.CTkFrame(self)
        self.open_new_window_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")


        self.button = customtkinter.CTkButton(self.open_new_window_frame, text="Open cases", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    

        # set default values        
        self.seleBtn.set("Dark")  

           
        
        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)



    def sidebar_button_event(self):
        print("sidebar_button click")

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("1100x370")
        window.title("Chat - Cases")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create label on CTkToplevel window
        cl = customtkinter.CTkFrame(window, width=200, corner_radius=0)
        cl.grid(row=0, column=0, rowspan=4, sticky="nsew")
        cl.grid_rowconfigure(4, weight=1)
        # 9 -- LABEL: LOGO
        vText2_label = customtkinter.CTkLabel(cl, text="Cases", font=customtkinter.CTkFont(size=20, weight="bold"))
        vText2_label.grid(row=0, column=0, padx=40, pady=(10,20))
        
        # 10 -- LABEL: vText3
        vText3_label = customtkinter.CTkLabel(cl, text="Defendant's name*:", font=customtkinter.CTkFont(size=12))
        vText3_label.grid(row=1, column=0, pady=(5,0))
        # 11 -- ENTRY: eText1
        eText1 = customtkinter.CTkEntry(cl, placeholder_text="etnry1", justify='left')
        eText1.grid(row=2, column=0, padx=(20, 20), pady=(5, 15))
        # 10 -- LABEL: vText4
        vText4_label = customtkinter.CTkLabel(cl, text="Defense type*:", font=customtkinter.CTkFont(size=12))
        vText4_label.grid(row=3, column=0, pady=(5,0))
        # 11 -- ENTRY: eText2
        eText2 = customtkinter.CTkEntry(cl, placeholder_text="etnry2")
        eText2.grid(row=4, column=0,   columnspan=2, padx=(20, 20), pady=(5, 15))
        # 10 -- LABEL: vText5
        vText5_label = customtkinter.CTkLabel(cl, text="Date*:", font=customtkinter.CTkFont(size=12))
        vText5_label.grid(row=5, column=0, pady=(5,0))
        # 11 -- ENTRY: eText3
        eText3 = customtkinter.CTkEntry(cl, placeholder_text="etnry3")
        eText3.grid(row=6, column=0,   columnspan=2, padx=(20, 20), pady=(5, 15))
        # 4 -- BUTTON: btn1
        self.btn1 = customtkinter.CTkButton(cl, fg_color="transparent", text="Submit",border_width=2, text_color=("gray10", "#DCE4EE"))
        self.btn1.grid(row=7, column=0, padx=(20, 0), pady=(40,0))

        #COLUMN 2
        

        # CREATE CASES VIEW TREE FRAME
        cl2 = customtkinter.CTkFrame(window, fg_color="transparent")
        cl2.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        cl2.grid_columnconfigure(0, weight=1)
        cl2.grid_rowconfigure(4, weight=1) 
        # define columns
        columns = ('id', 'defendants_name', 'defense_type','date')
        vText2_label = customtkinter.CTkLabel(cl2, text="Cases view", font=customtkinter.CTkFont(size=20, weight="bold"))
        vText2_label.grid(row=0, column=1, padx=40, pady=(10,20))

        tree = ttk.Treeview(cl2, columns=columns, show='headings')

        # define headings
        tree.heading('id', text='ID')
        tree.heading('defendants_name', text='DEFENDANTS NAME')
        tree.heading('defense_type', text='DEFENSE TYPE')
        tree.heading('date', text='DATE')

        # generate sample data
        data = []
        for n in range(1, 100):
            data.append((f'id {n}', f'name {n}', f'type{n}' , f'date{n}'))

        # add data to the treeview
        for dt in data:
            tree.insert('', tkinter.END, values=dt)


        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))


        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=1, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(cl, orient=tkinter.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        


if __name__ == "__main__":
    app = App()
    app.mainloop()