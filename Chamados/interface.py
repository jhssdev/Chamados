import PySimpleGUI as sg

# Função para validar usuário e senha
def validar_login(usuario, senha):
    return usuario == 'Continental' and senha == 'Conti12345!'

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Mostrar senha', key='mostrar_senha', enable_events=True)],
    [sg.Checkbox('Salvar o login?', key='salvar_login')],
    [sg.Button('Entrar')],
    [sg.Text('', size=(30, 1), key='mensagem', text_color='red')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()

    # Fechar a janela
    if eventos == sg.WINDOW_CLOSED:
        break

    # Mostrar ou esconder a senha
    if eventos == 'mostrar_senha':
        if valores['mostrar_senha']:
            janela['senha'].update(password_char='')
        else:
            janela['senha'].update(password_char='*')

    # Quando o botão Entrar é clicado
    if eventos == 'Entrar':
        usuario = valores['usuario']
        senha = valores['senha']

        if validar_login(usuario, senha):
            sg.popup('Bem-vindo(a) à automação da Continental!', title='Sucesso')
        else:
            janela['mensagem'].update('Usuário ou senha incorretos. Tente novamente.')

# Fechar a janela no final do loop
janela.close()
