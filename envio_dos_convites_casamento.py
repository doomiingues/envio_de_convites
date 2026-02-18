import pyautogui
import pyperclip
import time
import os

convidados = [

    #filho_3menos // False: Não tem filhos   //  True: tem filhos
    
    #Familia Rayssa
    {"grupo": "Familia Rayssa", "nome": "Adriano Crepaldi", "telefone": "5519992705561", "codigo": "Adriano Crepaldi", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Andreia David", "telefone": "5515988236327", "codigo": "Andreia David", "qtd": 3, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Lucileia Menezes", "telefone": "5519993024568", "codigo": "Lucileia Menezes", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Elena Cristina Caetano", "telefone": "5519997778775", "codigo": "Elena Cristina Caetano", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Leia Silva", "telefone": "5519998216406", "codigo": "Leia Silva", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Lilian Caroline", "telefone": "5519999556176", "codigo": "Lilian Caroline", "qtd": 0, "filhos_3menos": False},
    {"grupo": "Familia Rayssa", "nome": "Lidia Vanessa", "telefone": "5519992324095", "codigo": "Lidia Vanessa", "qtd": 0, "filhos_3menos": False},
    {"grupo": "Familia Rayssa", "nome": "Maria José Crepaldi", "telefone": "5519983228753", "codigo": "Maria José Crepaldi", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Paula Andreia Crepaldi", "telefone": "5519993141823", "codigo": "Paula Andreia Crepaldi", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Rayanne Crepaldi", "telefone": "5519982022980", "codigo": "Rayanne Crepaldi", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Eunice da Silva", "telefone": "5519987368134", "codigo": "Eunice da Silva", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Rayssa", "nome": "Rogerio da Silva", "telefone": "5519996873234", "codigo": "Rogerio da Silva", "qtd": 0, "filhos_3menos": False}, 


    #Familia Guilherme
    {"grupo": "Familia Guilherme", "nome": "Adriano Domingues", "telefone": "554288411493", "codigo": "Adriano Domingues", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Guilherme", "nome": "Ariane Domingues", "telefone": "554299203151", "codigo": "Ariane Domingues", "qtd": 1, "filhos_3menos": True}, 
    {"grupo": "Familia Guilherme", "nome": "Daniel Augusto", "telefone": "554284285746", "codigo": "Daniel Augusto", "qtd": 3, "filhos_3menos": False}, 
    {"grupo": "Familia Guilherme", "nome": "Eva Ramos", "telefone": "554288530439", "codigo": "Eva Ramos", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Guilherme", "nome": "Gabriel David", "telefone": "554288000732", "codigo": "Gabriel David Domingues", "qtd": 1, "filhos_3menos": True}, 
    {"grupo": "Familia Guilherme", "nome": "Julia Ramos", "telefone": "554288582712", "codigo": "Julia Ramos", "qtd": 2, "filhos_3menos": True}, 
    {"grupo": "Familia Guilherme", "nome": "Marcio Domingues", "telefone": "554299168185", "codigo": "Marcio Domingues", "qtd": 2, "filhos_3menos": True}, 
    {"grupo": "Familia Guilherme", "nome": "Matheus Isidoro", "telefone": "554288892258", "codigo": "Matheus Isidoro", "qtd": 2, "filhos_3menos": True}, 
    {"grupo": "Familia Guilherme", "nome": "Ponciano Domingues", "telefone": "554284012798", "codigo": "Ponciano Domingues", "qtd": 3, "filhos_3menos": True}, 
    {"grupo": "Familia Guilherme", "nome": "Suelen Ramos", "telefone": "554288696067", "codigo": "Suelen Ramos", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Guilherme", "nome": "Taciele Domingues", "telefone": "554299957984", "codigo": "Taciele Domingues", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Familia Guilherme", "nome": "Elyeser Requiao", "telefone": "554298718522", "codigo": "Elyeser Requiao", "qtd": 0, "filhos_3menos": False}, 


    #Amigos Rayssa
    {"grupo": "Amigos Rayssa", "nome": "Ana Carolina", "telefone": "5519971213050", "codigo": "Ana Carolina", "qtd": 2, "filhos_3menos": False}, 
    {"grupo": "Amigos Rayssa", "nome": "Gabriely Zamarchi", "telefone": "5519994601738", "codigo": "Gabriely Zamarchi", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Amigos Rayssa", "nome": "Kelrry Michetti", "telefone": "5519981538774", "codigo": "Kelrry Michetti", "qtd": 2, "filhos_3menos": False}, 
    {"grupo": "Amigos Rayssa", "nome": "Maria Eduarda Suyama", "telefone": "5519982970013", "codigo": "Maria Eduarda Suyama", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Amigos Rayssa", "nome": "Maria Vitoria", "telefone": "5519983911259", "codigo": "Maria Vitoria", "qtd": 2, "filhos_3menos": False}, 
    {"grupo": "Amigos Rayssa", "nome": "Marina", "telefone": "5519998369450", "codigo": "Marina", "qtd": 0, "filhos_3menos": False}, 


    #Amigos Guilherme
    {"grupo": "Amigos Guilherme", "nome": "Anderson Candido", "telefone": "5519993764674", "codigo": "Anderson Candido", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Amigos Guilherme", "nome": "Henrique Monteiro", "telefone": "5519993072881", "codigo": "Henrique Monteiro", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Amigos Guilherme", "nome": "Vinicius Alves", "telefone": "5519984607162", "codigo": "Vinicius Alves", "qtd": 0, "filhos_3menos": False},


    #Amigos Igreja
    {"grupo": "Amigos Igreja", "nome": "Adarlan Alves Ferreira", "telefone": "5519989954336", "codigo": "Alves Ferreira", "qtd": 3, "filhos_3menos": True}, 
    {"grupo": "Amigos Igreja", "nome": "Alexandre Valeriano", "telefone": "5519992354942", "codigo": "Alexandre Valeriano", "qtd": 2, "filhos_3menos": False}, 
    {"grupo": "Amigos Igreja", "nome": "Ana Paula Souza", "telefone": "5519991959731", "codigo": "Ana Paula Souza", "qtd": 4, "filhos_3menos": True}, 
    {"grupo": "Amigos Igreja", "nome": "Davi Lucca", "telefone": "5519989754529", "codigo": "Davi Lucca", "qtd": 0, "filhos_3menos": False}, #mandar para o andre ou nos msm confirmamos 
    {"grupo": "Amigos Igreja", "nome": "Edimar Oliveira", "telefone": "5519993463770", "codigo": "Edimar Oliveira", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Amigos Igreja", "nome": "Fernando Dias", "telefone": "5519989955389", "codigo": "Fernando Dias", "qtd": 1, "filhos_3menos": True}, 	
    {"grupo": "Amigos Igreja", "nome": "Isac Silva", "telefone": "5519998709059", "codigo": "Isac Silva", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Amigos Igreja", "nome": "Joyce Lorena Oliveira", "telefone": "5519998094218", "codigo": "Joyce Lorena Oliveira", "qtd": 0, "filhos_3menos": True}, 
    {"grupo": "Amigos Igreja", "nome": "Luiz Carlos Figueiredo", "telefone": "5519997245365", "codigo": "Luiz Carlos Figueiredo", "qtd": 1, "filhos_3menos": False}, 
    {"grupo": "Amigos Igreja", "nome": "Regiane Ramos", "telefone": "5519998478474", "codigo": "Regiane Ramos Santana", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Amigos Igreja", "nome": "Tamires Dias", "telefone": "5519994990381", "codigo": "Tamires Dias", "qtd": 0, "filhos_3menos": False},

    #Outros
    {"grupo": "Outros", "nome": "José Aldair Pereira", "telefone": "5519991488472", "codigo": "José Aldair Pereira", "qtd": 0, "filhos_3menos": False}, 
    {"grupo": "Outros", "nome": "Pedro da Luz", "telefone": "5519987291126", "codigo": "Pedro da Luz", "qtd": 0, "filhos_3menos": False}, #numero do meu pai


]

arquivo_pdf = r"C:\Users\Domingues\Documents\Apps\envio_dos_convites\envio_de_convites\Convite_Rayssa_&_Guilherme.pdf"

# tempo pra você abrir o WhatsApp Desktop manualmente
print("Abra o WhatsApp Desktop e deixe maximizado.")
print("Você tem 10 segundos...")
time.sleep(10)

for pessoa in convidados:
    grupo = pessoa["grupo"]
    nome = pessoa["nome"]
    telefone = pessoa["telefone"]
    codigo = pessoa["codigo"]
    qtd = pessoa["qtd"]
    filhos_3menos = pessoa["filhos_3menos"]

    if grupo != grupo_atual:
        grupo_atual = grupo
        print("\n" + "=" * 60)
        print(f"Inicianando envio: {grupo_atual.upper()}")
        print("\n" + "=" * 60)
    
    if filhos_3menos == False:
        mensagem = f"""Olá {nome}! 😊

    💍✨ Olá! Você está convidado(a) para o casamento de Guilherme e Rayssa! ✨💍

    Ficaremos muito felizes em ter você conosco nesse dia tão especial ❤️

    📌 Seu nome de acesso é: {codigo}

    👥 Neste convite estão incluídos: {qtd} acompanhante(s)

    📄 Agora é só abrir o PDF do convite e clicar no link para confirmar sua presença.

    ✅ Contamos com você!

    📌 Obs.: Caso tenha algum problema para abrir o PDF ou dificuldade para confirmar presença, é só nos chamar no WhatsApp que ajudamos rapidinho 😊

    — Guilherme & Rayssa ❤️
    """
    else:
        mensagem = f"""Olá {nome}! 😊

    💍✨ Olá! Você está convidado(a) para o casamento de Guilherme e Rayssa! ✨💍

    Ficaremos muito felizes em ter você conosco nesse dia tão especial ❤️

    📌 Seu nome de acesso é: {codigo}

    👥 Neste convite estão incluídos: {qtd} acompanhante(s)
    👶 Obs.: crianças de até 3 anos não entram na contagem de acompanhantes.

    📄 Agora é só abrir o PDF do convite e clicar no link para confirmar sua presença.

    ✅ Contamos com você!

    📌 Obs.: Caso tenha algum problema para abrir o PDF ou dificuldade para confirmar presença, é só nos chamar no WhatsApp que ajudamos rapidinho 😊

    — Guilherme & Rayssa ❤️   
    
    """

    # clicar na barra de pesquisa (CTRL+F geralmente funciona)
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)

    # colar telefone
    pyperclip.copy(telefone)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)

    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.hotkey("alt", "a")
    time.sleep(2)

    pyautogui.press("tab")
    time.sleep(2)

    pyautogui.press("enter")
    time.sleep(2)

    # digitar caminho do arquivo
    pyperclip.copy(arquivo_pdf)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(3)

    # colar mensagem
    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # enviar arquivo (ENTER geralmente envia)
    pyautogui.press("enter")
    time.sleep(3)

    print(f"✅ Enviado para {nome} ({grupo})")

print("🎉 Todos enviados!")
