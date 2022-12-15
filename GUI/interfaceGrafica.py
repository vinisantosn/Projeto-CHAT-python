import socket
import threading
from tkinter import *
import tkinter.messagebox
import customtkinter

from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk


customtkinter.set_appearance_mode("System")  # Modes: "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PORT = 8080
SERVER = "127.0.0.1"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect(ADDRESS)

import xmlrpc.client



class Ticket:
    def __init__(self,nome, tel, tipo_caso):
        self.nome = nome
        self.tel = tel
        self.tipo_caso = tipo_caso



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
        self.btn = customtkinter.CTkButton(self.sidebar_frame, fg_color="transparent", text="Join",border_width=2, text_color=("gray10", "#DCE4EE"),command=lambda: self.logar(self.eText.get()))
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
        self.m_btn = customtkinter.CTkButton(master=self, fg_color="transparent",  text="Send", border_width=2, text_color=("gray10", "#DCE4EE"),command=lambda: self.sendButton(self.m_eText.get()))
        self.m_btn.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # "SECOND" COLUMN 
        # CREATE README OF APP: textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.insert("0.0", "README \n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        #CREATE VIEW OF CHAT: message_box        


        # CREATE TEXTBOX VIEW CHAT FRAME
        '''
        self.textCons = Text(self,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font="Helvetica 14",
                             padx=20,
                             pady=20)
        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)
        self.textCons.config(cursor="arrow")
        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight=1,
                        relx=0.974)
 
        scrollbar.config(command=self.textCons.yview)
        '''
        #self.textCons.config(state=DISABLED)
        
        
        self.message_box_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.message_box_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.message_box_frame.grid_columnconfigure(0, weight=1)
        self.message_box_frame.grid_rowconfigure(4, weight=1)
        
        
        self.message_box = scrolledtext.ScrolledText(self.message_box_frame)
        #message_box.insert(END,'A'+"\n\n")
        
        #self.message_box.config(state=tkinter.DISABLED)
        self.message_box.pack(side=tkinter.TOP)

        
        self.open_new_window_frame = customtkinter.CTkFrame(self)
        self.open_new_window_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        
        self.button = customtkinter.CTkButton(self.open_new_window_frame, text="Open cases", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    

        # set default values        
        self.seleBtn.set("Dark")  

           

    def logar(self,msg):
        self.login=msg
        self.eText.delete(0, END)
        rcv = threading.Thread(target=self.receive)
        rcv.start()
    def sendButton(self,msg):
        self.msg=msg
        self.m_eText.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                if message == 'NAME':
                    
                    client.send(self.login.encode(FORMAT))
                else:

                    self.message_box.insert(END,
                                         message+"\n\n")

            except:

                print("An error occurred!")
                client.close()
                break

    def sendMessage(self):
        while True:
            message = (f"{self.login}: {self.msg}")
            client.send(message.encode(FORMAT))
            break
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)



    def sidebar_button_event(self):
        print("sidebar_button click")

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry(f"{1100}x{580}")
        window.title("Chat - Cases")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create label on CTkToplevel window
        cl = customtkinter.CTkFrame(window, width=580, corner_radius=0)
        cl.grid(row=0, column=0, rowspan=4, sticky="nsew")
        cl.grid_rowconfigure(4, weight=1)
        # 9 -- LABEL: LOGO
        vText2_label = customtkinter.CTkLabel(cl, text="Casos", font=customtkinter.CTkFont(size=20, weight="bold"))
        vText2_label.grid(row=0, column=0, padx=120, pady=(10,20))
        
        # 10 -- LABEL: vText3
        vText3_label = customtkinter.CTkLabel(cl, text="Nome do Representado:", font=customtkinter.CTkFont(size=12))
        vText3_label.grid(row=1, column=0, pady=(5,0))
        # 11 -- ENTRY: eText1
        eText1 = customtkinter.CTkEntry(cl, justify='left')
        eText1.grid(row=2, column=0, padx=(20, 20), pady=(5, 15))
        # 10 -- LABEL: vText4
        vText4_label = customtkinter.CTkLabel(cl, text="Tipo de Defesa:", font=customtkinter.CTkFont(size=12))
        vText4_label.grid(row=3, column=0, pady=(5,0))
        # 11 -- ENTRY: eText2
        eText2 = customtkinter.CTkEntry(cl)
        eText2.grid(row=4, column=0,   columnspan=2, padx=(20, 20), pady=(5, 15))
        # 10 -- LABEL: vText5
        vText5_label = customtkinter.CTkLabel(cl, text="Telefone:", font=customtkinter.CTkFont(size=12))
        vText5_label.grid(row=5, column=0, pady=(5,0))
        # 11 -- ENTRY: eText3
        eText3 = customtkinter.CTkEntry(cl)
        eText3.grid(row=6, column=0,   columnspan=2, padx=(20, 20), pady=(5, 15))




        def inserir():
            nome = eText1.get()
            defesa = eText2.get()
            tel = eText3.get()
            dado = Ticket(nome,tel,defesa)
            if nome=='':
                messagebox.showerror('Error','O nome não pode ser vazio')
            else:
                proxy = xmlrpc.client.ServerProxy("http://127.0.0.2:5000/")
                proxy.inserir(dado)
                messagebox.showinfo('Sucesso','Os dados foram inseridos corretamente')
                eText1.delete(0,'end')
                eText2.delete(0,'end')
                eText3.delete(0,'end')
            mostrar()
        
        def atualizar():
            treev_dados=tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista= treev_dicionario['values']

            id_item = tree_lista[0]
            def update():
                nome = eText1.get()
                defesa = eText2.get()
                tel = eText3.get()
                dado = Ticket(nome,tel,defesa)
                if nome=='':
                    messagebox.showerror('Error','O nome não pode ser vazio')
                else:
                    proxy = xmlrpc.client.ServerProxy("http://127.0.0.2:5000/")
                    proxy.atualizar(id_item,dado)
                    messagebox.showinfo('Sucesso','Os dados foram atualizados corretamente')
                    eText1.delete(0,'end')
                    eText2.delete(0,'end')
                    eText3.delete(0,'end')
                mostrar()
                

            eText1.delete(0,'end')
            eText2.delete(0,'end')
            eText3.delete(0,'end')

            eText1.insert(0,tree_lista[1])
            eText2.insert(0,tree_lista[3])
            eText3.insert(0,tree_lista[2])

            self.btn13 = customtkinter.CTkButton(cl, fg_color="transparent", text="Confirmar",border_width=2, text_color=("gray10", "#DCE4EE"),command=update)
            self.btn13.grid(row=10, column=0, padx=(20, 0), pady=(10,0))
            
        def deletar():
            treev_dados=tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista= treev_dicionario['values']

            id_item = tree_lista[0]
            proxy = xmlrpc.client.ServerProxy("http://127.0.0.2:5000/")
            proxy.deletar(id_item)

            mostrar()
        # 4 -- BUTTON: btn1
        self.btn1 = customtkinter.CTkButton(cl, fg_color="transparent", text="Inserir",border_width=2, text_color=("gray10", "#DCE4EE"),command=inserir)
        self.btn1.grid(row=7, column=0, padx=(0, 0), pady=(10,0))

        self.btn12 = customtkinter.CTkButton(cl, fg_color="transparent", text="Deletar",border_width=2, text_color=("gray10", "#DCE4EE"),command=deletar)
        self.btn12.grid(row=8, column=0, padx=(0, 0), pady=(10,0))

        self.btn13 = customtkinter.CTkButton(cl, fg_color="transparent", text="Atualizar",border_width=2, text_color=("gray10", "#DCE4EE"),command=atualizar)
        self.btn13.grid(row=9, column=0, padx=(0, 0), pady=(10,80))
        #COLUMN 2
        

                
        # CREATE CASES VIEW TREE FRAME
        def mostrar():
            global tree
            cl2 = customtkinter.CTkFrame(window, fg_color="transparent")
            cl2.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
            cl2.grid_columnconfigure(0, weight=1)
            cl2.grid_rowconfigure(4, weight=1) 
            # define columns
            columns = ('id', 'NomedoRepresentado','Telefone', 'TipodeDefesa')
            vText2_label = customtkinter.CTkLabel(cl2, text="Cases view", font=customtkinter.CTkFont(size=20, weight="bold"))
            vText2_label.grid(row=0, column=1, padx=40, pady=(10,20))

            tree = ttk.Treeview(cl2, columns=columns, show='headings')

            # define headings
            tree.heading('id', text='ID')
            tree.heading('NomedoRepresentado', text='Nome do Representado')

            tree.heading('Telefone', text='Telefone')
            tree.heading('TipodeDefesa', text='Tipo de Defesa')

            # add data to the treeview
            proxy = xmlrpc.client.ServerProxy("http://127.0.0.2:5000/")
            dados=proxy.selecionar()
            for dt in dados:
                tree.insert('', tkinter.END, values=dt)

            def item_selected(event):
                for selected_item in tree.selection():
                    item = tree.item(selected_item)
                    record = item['values']
                    # show a message
                    print(record)

            tree.bind('<<TreeviewSelect>>', item_selected)

            tree.grid(row=0, column=1, sticky='nsew')
            # add a scrollbar
            scrollbar = ttk.Scrollbar(cl, orient=tkinter.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')

        mostrar()


if __name__ == "__main__":
    app = App()
    app.mainloop()
