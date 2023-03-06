#IMPORTAÇÕES
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import urllib


#TELA PRINCIPAL
janela_principal = Tk()
janela_principal.geometry('500x300')
janela_principal.title('Página de Autenticação')
janela_principal.iconbitmap('icons\icon.ico')
janela_principal.resizable(height=False, width=False)

#FUNÇÃO QUE PEGA OS DADOS INSERIDOS E COMEÇA A AUTOMAÇÃO
def iniciarAutomação():
    #CAPTURA O TEXTO QUE SERÁ ENVIADO
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    texto = texto_entry.get()
    mensagem = urllib.parse.quote(f'{texto}')

    #USUARIO qwerty e senha 000 padrão
    if usuario != 'qwerty' or senha != '000':
        messagebox.showwarning(message='Entre em contato com o administrador caso não tenha o usuario e a senha!', title='Acesso negado!')

    if usuario == 'qwerty' and senha == '000':
        janela_principal.destroy()
        
        #FUNÇÃO QUE EFETUA O LOGIN 
        navegador = webdriver.Chrome()
        navegador.get('https://web.whatsapp.com/')
        while len(navegador.find_elements('id', 'side')) < 1:
            time.sleep(1)

        #LÊ A LISTA DE CONTATOS E COMEÇA A DISPARAR AS MENSAGENS
        lista_contatos = open("lista_contatos.txt")
        contatos = lista_contatos.readlines()
        for contato in contatos:
            navegador.get(f'https://web.whatsapp.com/send?phone={contato}&text={mensagem}')
            time.sleep(5)

            #TENTE ENVIAR A MENSAGEM, CASO CONSIGA,ADICIONE NO ARQUIVO TXT lista_contatos_validos, CASO NÃO, ADICIONE NO ARQUIVO TXT lista_contatos_invalidos
            try:
                navegador.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
                with open('lista_contatos_validos.txt', 'a') as lista_contatos_validos:
                    lista_contatos_validos.write(contato)
                    lista_contatos_validos.close()
            except:
                with open('lista_contatos_invalidos.txt', 'a') as lista_contatos_invalidos:
                    lista_contatos_invalidos.write(contato)
                    lista_contatos_invalidos.close()

#FRAMES
frame_esquerda = Frame(janela_principal, width=250,height=300, background='#ececec')
frame_esquerda.pack(side=LEFT)

frame_direita = Frame(janela_principal, width=250, height=300, background='#320139' )
frame_direita.pack(side=RIGHT)


label_login = Label(frame_direita, text='Login', font=("Century Gothic", 15), bg='#320139', fg='white')
label_login.place(x=10, y=20) # X = LARGURA, Y = ALTURA

label_comunicado = Label(frame_direita, text='Faça o login para começar a disparar', font=("Century Gothic", 9), bg='#320139', fg='white')
label_comunicado.place(x=10, y=60) # X = LARGURA, Y = ALTURA


label_usuario = Label(frame_direita, text='Usuário', font=("Century Gothic", 9), bg='#320139', fg='white')
label_usuario.place(x=10, y=100) # X = LARGURA, Y = ALTURA

usuario_entry = ttk.Entry(frame_direita, width=30)
usuario_entry.place(x=10, y=120)


label_senha = Label(frame_direita, text='Senha', font=("Century Gothic", 9), bg='#320139', fg='white')
label_senha.place(x=10, y=150) # X = LARGURA, Y = ALTURA

senha_entry = ttk.Entry(frame_direita, width=30)
senha_entry.place(x=10, y=170) # X = LARGURA, Y = ALTURA


label_texto = Label(frame_direita, text='Texto a ser enviado', font=("Century Gothic", 9), bg='#320139', fg='white')
label_texto.place(x=10, y=200) # X = LARGURA, Y = ALTURA

texto_entry = ttk.Entry(frame_direita, width=30)
texto_entry.place(x=10, y=220) # X = LARGURA, Y = ALTURA


botão_acessar = Button(frame_direita, text='Acessar',font=("Century Gothic", 9),bg='#a45785', command=iniciarAutomação )
botão_acessar.place(x=100,y=260) # X = LARGURA, Y = ALTURA


janela_principal.mainloop()