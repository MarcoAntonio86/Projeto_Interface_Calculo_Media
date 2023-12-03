from tkinter import *

def calcular_media():
    notas = entrada_notas.get().split(',')
    notas = [float(nota) for nota in notas if nota.strip()]
    
    if notas:
        media = sum(notas) / len(notas)
        texto_resultado.config(text=f'A média é {media:.2f}')
    else:
        texto_resultado.config(text='Nenhuma nota válida inserida.')

janela = Tk()
janela.title('Cálculo de Média')
janela.geometry('500x300')

texto_orientacao = Label(janela, text='Informe as notas separadas por vírgula:')
texto_orientacao.pack(padx=10, pady=10)

entrada_notas = Entry(janela)
entrada_notas.pack(padx=10, pady=10)

botao_calcular = Button(janela, text='Calcular Média', command=calcular_media)
botao_calcular.pack(padx=10, pady=10)

texto_resultado = Label(janela, text='')
texto_resultado.pack(padx=10, pady=10)

janela.mainloop()
