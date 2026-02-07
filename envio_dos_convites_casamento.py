import pyautogui
import pyperclip
import time
import os

convidados = [
    #{"nome": "Rayssa", "telefone": "5519983340123", "codigo": "Rayssa Crepaldi", "qtd": 3, "filhos_3menos": False},
    {"nome": "Papai", "telefone": "5519987420654", "codigo": "Joel Domingues", "qtd": 3, "filhos_3menos": True},
    {"nome": "Papai 2 ", "telefone": "5519987291126", "codigo": "É Só teste", "qtd": 2, "filhos_3menos": False},
]

arquivo_pdf = r"C:\Users\guido\Downloads\Convite_Rayssa_&_Guilherme.pdf"

# tempo pra você abrir o WhatsApp Desktop manualmente
print("Abra o WhatsApp Desktop e deixe maximizado.")
print("Você tem 10 segundos...")
time.sleep(10)

for pessoa in convidados:
    nome = pessoa["nome"]
    telefone = pessoa["telefone"]
    codigo = pessoa["codigo"]
    qtd = pessoa["qtd"]
    filhos_3menos = pessoa["filhos_3menos"]
    
    if filhos_3menos == False:
        mensagem = f"""Olá {nome}! 😊

    Você está convidado(a) para o nosso casamento 💍✨

    Seu código de acesso é: {codigo}

    Você tem {qtd} acompanhantes anexados eu seu convite.

    Abra o PDF do convite e clique no link para confirmar presença ❤️
    """
    else:
        mensagem = f"""Olá {nome}! 😊

    Você está convidado(a) para o nosso casamento 💍✨

    Seu código de acesso é: {codigo}

    Você tem {qtd} acompanhantes anexados eu seu convite.

    Sabemos que você tem crianças, crianças de ou até 3 anos não entram na contagem ❤️

    Abra o PDF do convite e clique no link para confirmar presença ❤️   
    
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

    print(f"✅ Enviado para {nome}")

print("🎉 Todos enviados!")
