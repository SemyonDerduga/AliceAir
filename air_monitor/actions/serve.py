import co2meter as co2

def run(ctx, port):
    # create co2 monitoring obj
    mon = co2.CO2monitor()
    date, co2ppm, temperature = mon.read_data()
    print(f"Сейчас в комнате концентрация углекислого газа равна {co2ppm}, температура {temperature} градусов.")