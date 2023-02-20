import tkinter as tk
import psutil

# Criando a janela principal
root = tk.Tk()
root.configure(background='red')
root.title('Tempo Restante da Bateria')
root.geometry('500x70')
root.iconbitmap('battery-3_icon-icons.com_64867.ico')
lab = tk.Label(root,bg='red')
lab.pack()
root.wm_attributes("-transparentcolor", 'red')
# Criando o widget de exibição do tempo restante
time_label = tk.Label(root, text='---',fg='white',bg='red')
time_label.pack()

# Função para atualizar o tempo restante
def update_time():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    time_left = 'Calculando...'
    if percent != 100:
        if plugged:
            time_left = 'Carregando...'
        else:
            time_left = str(battery.secsleft//3600) + 'h ' + str((battery.secsleft%3600)//60) + 'min restantes'
    time_label.config(text=time_left)
    root.after(1000, update_time)

# Iniciando a atualização do tempo restante
update_time()

# Executando a janela principal
root.mainloop()
