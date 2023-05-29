from tkinter import *


def esp_main():
    root = Tk()
    root.geometry('600x800')
    root.title('Juego de Mad Libs')
    root.resizable(False, False)
    root.configure(bg='lightblue')
    Label(root, text='Juego de Mad Libs \n ¡Disfrútalo!', font='arial 20 bold', bg='lightblue').pack()
    Label(root, text='Elige una historia:', font='arial 15 bold', bg='lightblue').place(x=208, y=80)

    def madlib1():
        def completar_madlib(tl: Toplevel, adjetivo1, sustantivo1, adjetivo2, sustantivo2, adjetivo3, sustantivo3, adjetivo4, sustantivo4, adjetivo5, sustantivo5, adjetivo6, sustantivo6, adjetivo7, adjetivo8):
            texto = f'''Hoy fui al parque {adjetivo1} {sustantivo1} con mi {adjetivo2} {sustantivo2}. Llevamos algunos {adjetivo3} {sustantivo3} y un {adjetivo4} {sustantivo4} para jugar. Mientras jugábamos, ¡un {adjetivo5} {sustantivo5} pasó corriendo y robó nuestro {adjetivo6} {sustantivo6}! Lo perseguimos, pero era demasiado {adjetivo7} para atraparlo. A pesar del percance, nos divertimos mucho en el parque y ya estamos deseando volver.'''
            Label(tl, text='El cuento:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=480)
            Label(tl, text=texto, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=480)

        top = Toplevel(bg='lightblue')
        top.title("El robo")
        top.geometry('600x600')
        top.resizable(False, False)

        Label(top, text='El robo - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)
        
        adjetivo1 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=60) 
        sustantivo1 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=90)
        adjetivo2 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=120)
        sustantivo2 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=150)
        adjetivo3 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=180)
        sustantivo3 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=210)
        adjetivo4 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=240)
        sustantivo4 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=270)
        adjetivo5 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=300)
        sustantivo5 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=330)
        adjetivo6 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=360)
        sustantivo6 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=390)
        adjetivo7 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=420)
        adjetivo8 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=450) 
        
        area_entrada_adjetivo1 = Entry(top, width=30)
        area_entrada_adjetivo1.place(x=210, y=60) 
        area_entrada_sustantivo1 = Entry(top, width=30)
        area_entrada_sustantivo1.place(x=210, y=90)
        area_entrada_adjetivo2 = Entry(top, width=30)
        area_entrada_adjetivo2.place(x=210, y=120)
        area_entrada_sustantivo2 = Entry(top, width=30)
        area_entrada_sustantivo2.place(x=210, y=150)
        area_entrada_adjetivo3 = Entry(top, width=30)
        area_entrada_adjetivo3.place(x=210, y=180)
        area_entrada_sustantivo3 = Entry(top, width=30)
        area_entrada_sustantivo3.place(x=210, y=210)
        area_entrada_adjetivo4 = Entry(top, width=30)
        area_entrada_adjetivo4.place(x=210, y=240)
        area_entrada_sustantivo4 = Entry(top, width=30)
        area_entrada_sustantivo4.place(x=210, y=270)
        area_entrada_adjetivo5 = Entry(top, width=30)
        area_entrada_adjetivo5.place(x=210, y=300)
        area_entrada_sustantivo5 = Entry(top, width=30)
        area_entrada_sustantivo5.place(x=210, y=330)
        area_entrada_adjetivo6 = Entry(top, width=30)
        area_entrada_adjetivo6.place(x=210, y=360)
        area_entrada_sustantivo6 = Entry(top, width=30)
        area_entrada_sustantivo6.place(x=210, y=390)
        area_entrada_adjetivo7 = Entry(top, width=30)
        area_entrada_adjetivo7.place(x=210, y=420)
        area_entrada_adjetivo8 = Entry(top, width=30)
        area_entrada_adjetivo8.place(x=210, y=450)
        btn_enviar = Button(top, text="Enviar", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: completar_madlib(top, area_entrada_adjetivo1.get(), area_entrada_sustantivo1.get(), area_entrada_adjetivo2.get(), area_entrada_sustantivo2.get(), area_entrada_adjetivo3.get(), area_entrada_sustantivo3.get(), area_entrada_adjetivo4.get(), area_entrada_sustantivo4.get(), area_entrada_adjetivo5.get(), area_entrada_sustantivo5.get(), area_entrada_adjetivo6.get(), area_entrada_sustantivo6.get(), area_entrada_adjetivo7.get(), area_entrada_adjetivo8.get()))
        btn_enviar.place(x=40, y=480)

        top.mainloop()

    def madlib2():
        def finalizar_madlib2(tl: Toplevel, adjetivo1, sustantivo1, adjetivo2, adjetivo3, sustantivo2, adjetivo4, sustantivo3, adjetivo5, sustantivo4, adjetivo6, sustantivo5, adjetivo7, sustantivo6, adjetivo8, sustantivo7, adjetivo9, sustantivo8, adjetivo10):
            texto = f'''Había una vez, un(a) {adjetivo1} {sustantivo1} que emprendió un viaje {adjetivo2}. Empacaron un(a) {adjetivo3} {sustantivo2}, un(a) {adjetivo4} {sustantivo3} y un(a) {adjetivo5} {sustantivo4} para el viaje. En el camino, se encontraron con un(a) {adjetivo6} {sustantivo5} que se ofreció a ayudarles. Juntos, enfrentaron un(a) {adjetivo7} {sustantivo6} y finalmente descubrieron un(a) {adjetivo8} {sustantivo7}. El/La {adjetivo9} {sustantivo8} regresó a casa, orgulloso(a) de su viaje {adjetivo10}.'''
            Label(tl, text='La historia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=600)
            Label(tl, text=texto, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=600)

        top = Toplevel(bg='lightblue')
        top.title("El viaje")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='El viaje - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        adjetivo1 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=60)
        sustantivo1 = Label(top, text="Ingresa un sustantivo:", bg='lightblue').place(x=40, y=90)
        adjetivo2 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=120)
        adjetivo3 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=150)
        sustantivo2 = Label(top, text="Ingresa un sustantivo:", bg='lightblue').place(x=40, y=180)
        adjetivo4 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=210)
        sustantivo3 = Label(top, text="Ingresa un sustantivo:", bg='lightblue').place(x=40, y=240)
        adjetivo5 = Label(top, text="Ingresa un sustantivo:", bg='lightblue').place(x=40, y=270)
        sustantivo4 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=300)
        adjetivo6 = Label(top, text="Ingresa un sustantivo:", bg='lightblue').place(x=40, y=330)
        sustantivo5 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=360)
        adjetivo7 = Label(top, text="Ingresa un sustantivo:", bg='lightblue').place(x=40, y=390)
        sustantivo6 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=420)
        adjetivo8 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=450)
        sustantivo7 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=480)
        adjetivo9 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=510)
        sustantivo8 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=540)
        adjetivo10 = Label(top, text="Ingresa un adjetivo:", bg='lightblue').place(x=40, y=570)

        area_ingreso_adjetivo1 = Entry(top, width=30)
        area_ingreso_adjetivo1.place(x=210, y=60)
        area_ingreso_sustantivo1 = Entry(top, width=30)
        area_ingreso_sustantivo1.place(x=210, y=90)
        area_ingreso_adjetivo2 = Entry(top, width=30)
        area_ingreso_adjetivo2.place(x=210, y=120)
        area_ingreso_adjetivo3 = Entry(top, width=30)
        area_ingreso_adjetivo3.place(x=210, y=150)
        area_ingreso_sustantivo2 = Entry(top, width=30)
        area_ingreso_sustantivo2.place(x=210, y=180)
        area_ingreso_adjetivo4 = Entry(top, width=30)
        area_ingreso_adjetivo4.place(x=210, y=210)
        area_ingreso_sustantivo3 = Entry(top, width=30)
        area_ingreso_sustantivo3.place(x=210, y=240)
        area_ingreso_adjetivo5 = Entry(top, width=30)
        area_ingreso_adjetivo5.place(x=210, y=270)
        area_ingreso_sustantivo4 = Entry(top, width=30)
        area_ingreso_sustantivo4.place(x=210, y=300)
        area_ingreso_adjetivo6 = Entry(top, width=30)
        area_ingreso_adjetivo6.place(x=210, y=330)
        area_ingreso_sustantivo5 = Entry(top, width=30)
        area_ingreso_sustantivo5.place(x=210, y=360)
        area_ingreso_adjetivo7 = Entry(top, width=30)
        area_ingreso_adjetivo7.place(x=210, y=390)
        area_ingreso_sustantivo6 = Entry(top, width=30)
        area_ingreso_sustantivo6.place(x=210, y=420)
        area_ingreso_adjetivo8 = Entry(top, width=30)
        area_ingreso_adjetivo8.place(x=210, y=450)
        area_ingreso_sustantivo7 = Entry(top, width=30)
        area_ingreso_sustantivo7.place(x=210, y=480)
        area_ingreso_adjetivo9 = Entry(top, width=30)
        area_ingreso_adjetivo9.place(x=210, y=510)
        area_ingreso_sustantivo8 = Entry(top, width=30)
        area_ingreso_sustantivo8.place(x=210, y=540)
        area_ingreso_adjetivo10 = Entry(top, width=30)
        area_ingreso_adjetivo10.place(x=210, y=570)
        boton_enviar = Button(top, text="Enviar", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finalizar_madlib2(top, area_ingreso_adjetivo1.get(), area_ingreso_sustantivo1.get(), area_ingreso_adjetivo2.get(), area_ingreso_adjetivo3.get(), area_ingreso_sustantivo2.get(), area_ingreso_adjetivo4.get(), area_ingreso_sustantivo3.get(), area_ingreso_adjetivo5.get(), area_ingreso_sustantivo4.get(), area_ingreso_adjetivo6.get(), area_ingreso_sustantivo5.get(), area_ingreso_adjetivo7.get(), area_ingreso_sustantivo6.get(), area_ingreso_adjetivo8.get(), area_ingreso_sustantivo7.get(), area_ingreso_adjetivo9.get(), area_ingreso_sustantivo8.get(), area_ingreso_adjetivo10.get()))
        boton_enviar.place(x=40, y=600)
        top.mainloop()

    def madlib3():
        def completar_madlib3(tl: Toplevel, animal1, adjetivo1, parte_cuerpo1, comida1, numero1, parte_cuerpo2, numero2, parte_cuerpo3, adjetivo2, accion, trabajo, adjetivo3, adjetivo4, sustantivo1):
            texto = f'''El {animal1} es un animal doméstico. Un {animal1} tiene {adjetivo1} {parte_cuerpo1} para poder comer {comida1} con facilidad, tiene {numero1} {parte_cuerpo2} y {numero2} {parte_cuerpo3}. Es un animal muy {adjetivo2} y es muy útil en {accion} {trabajo}. Corre muy {adjetivo3}, ladra {adjetivo4} y ataca el {sustantivo1}. Se pueden encontrar {animal1}s en todas partes del mundo.'''
            Label(tl, text='La historia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=500)
            Label(tl, text=texto, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Animal")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Animal - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        animal1 = Label(top, text="Ingresa un animal: ", bg='lightblue').place(x=40, y=60)
        adjetivo1 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=90)
        parte_cuerpo1 = Label(top, text="Ingresa una parte del cuerpo: ", bg='lightblue').place(x=40, y=120)
        comida1 = Label(top, text="Ingresa una comida: ", bg='lightblue').place(x=40, y=150)
        numero1 = Label(top, text="Ingresa un número: ", bg='lightblue').place(x=40, y=180)
        parte_cuerpo2 = Label(top, text="Ingresa una parte del cuerpo: ", bg='lightblue').place(x=40, y=210)
        numero2 = Label(top, text="Ingresa un número: ", bg='lightblue').place(x=40, y=240)
        parte_cuerpo3 = Label(top, text="Ingresa una parte del cuerpo: ", bg='lightblue').place(x=40, y=270)
        adjetivo2 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=300)
        accion = Label(top, text="Ingresa un verbo: ", bg='lightblue').place(x=40, y=330)
        trabajo = Label(top, text="Ingresa un trabajo: ", bg='lightblue').place(x=40, y=360)
        adjetivo3 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=390)
        adjetivo4 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=420)
        sustantivo1 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=450)

        animal1_input_area = Entry(top, width=30)
        animal1_input_area.place(x=210, y=60)
        adjetivo1_entry_area = Entry(top, width=30)
        adjetivo1_entry_area.place(x=210, y=90)
        parte_cuerpo1_input_area = Entry(top, width=30)
        parte_cuerpo1_input_area.place(x=210, y=120)
        comida1_entry_area = Entry(top, width=30)
        comida1_entry_area.place(x=210, y=150)
        numero1_input_area = Entry(top, width=30)
        numero1_input_area.place(x=210, y=180)
        parte_cuerpo2_entry_area = Entry(top, width=30)
        parte_cuerpo2_entry_area.place(x=210, y=210)
        numero2_input_area = Entry(top, width=30)
        numero2_input_area.place(x=210, y=240)
        parte_cuerpo3_entry_area = Entry(top, width=30)
        parte_cuerpo3_entry_area.place(x=210, y=270)
        adjetivo2_input_area = Entry(top, width=30)
        adjetivo2_input_area.place(x=210, y=300)
        accion_entry_area = Entry(top, width=30)
        accion_entry_area.place(x=210, y=330)
        trabajo_input_area = Entry(top, width=30)
        trabajo_input_area.place(x=210, y=360)
        adjetivo3_entry_area = Entry(top, width=30)
        adjetivo3_entry_area.place(x=210, y=390)
        adjetivo4_input_area = Entry(top, width=30)
        adjetivo4_input_area.place(x=210, y=420)
        sustantivo1_entry_area = Entry(top, width=30)
        sustantivo1_entry_area.place(x=210, y=450)

        submit_btn = Button(top, text="Enviar", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: completar_madlib3(top, animal1_input_area.get(), adjetivo1_entry_area.get(), parte_cuerpo1_input_area.get(), comida1_entry_area.get(), numero1_input_area.get(), parte_cuerpo2_entry_area.get(), numero2_input_area.get(), parte_cuerpo3_entry_area.get(), adjetivo2_input_area.get(), accion_entry_area.get(), trabajo_input_area.get(), adjetivo3_entry_area.get(), adjetivo4_input_area.get(), sustantivo1_entry_area.get()))
        submit_btn.place(x=40, y=600)

        top.mainloop()

    def madlib4():
        def completar_madlib4(tl: Toplevel, año, pais1, nacionalidad1, lugar1, pais2, numero):
            texto = f'''El 7 de diciembre de {año}, {pais1} lanzó un sorpresivo ataque aéreo a la base naval {nacionalidad1} en la Isla de {lugar1}, {pais2}, obligando a {pais2} a entrar en la Segunda Guerra Mundial. El ataque marcó el clímax de una década de empeoramiento en las relaciones entre {pais1} y {pais2}.'''
            Label(tl, text='La historia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
            x=130, y=500)
            Label(tl, text=texto, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Guerra")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Guerra - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        año = Label(top, text="Ingresa un año: ", bg='lightblue').place(x=40, y=60)
        pais1 = Label(top, text="Ingresa un país: ", bg='lightblue').place(x=40, y=90)
        nacionalidad1 = Label(top, text="Ingresa una nacionalidad: ", bg='lightblue').place(x=40, y=120)
        lugar1 = Label(top, text="Ingresa un lugar: ", bg='lightblue').place(x=40, y=150)
        pais2 = Label(top, text="Ingresa un país: ", bg='lightblue').place(x=40, y=180)
        numero = Label(top, text="Ingresa un número: ", bg='lightblue').place(x=40, y=210)

        area_ingreso_año = Entry(top, width=30)
        area_ingreso_año.place(x=210, y=60)
        area_ingreso_pais1 = Entry(top, width=30)
        area_ingreso_pais1.place(x=210, y=90)
        area_ingreso_nacionalidad1 = Entry(top, width=30)
        area_ingreso_nacionalidad1.place(x=210, y=120)
        area_ingreso_lugar1 = Entry(top, width=30)
        area_ingreso_lugar1.place(x=210, y=150)
        area_ingreso_pais2 = Entry(top, width=30)
        area_ingreso_pais2.place(x=210, y=180)
        area_ingreso_numero = Entry(top, width=30)
        area_ingreso_numero.place(x=210, y=210)
        boton_enviar = Button(top, text="Enviar", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: completar_madlib4(top, area_ingreso_año.get(), area_ingreso_pais1.get(), area_ingreso_nacionalidad1.get(), area_ingreso_lugar1.get(), area_ingreso_pais2.get(), area_ingreso_numero.get()))
        boton_enviar.place(x=40, y=600)
        top.mainloop()

    def madlib5():
        def terminar_madlib5(tl: Toplevel, adjetivo1, sustantivo1, sustantivo2, numero, adjetivo2, celebridad, adjetivo3, verbo1, verbo2, adjetivo4):
            texto = f'''La Fórmula 1 es mi deporte favorito {adjetivo1}. El olor a {sustantivo1} y el sonido de {sustantivo2} mientras los pilotos corren a {numero} km/h es realmente {adjetivo2}. Mi piloto favorito es {celebridad}, quien tiene un {adjetivo3} increíble y siempre parece {verbo1} en el momento adecuado. ¡No puedo esperar para ver quién se llevará el trofeo {adjetivo4} esta temporada!'''
            Label(tl, text='La historia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
            x=130, y=500)
            Label(tl, text=texto, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Fórmula 1")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Fórmula 1 - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        adjetivo1 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=60)
        sustantivo1 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=90)
        sustantivo2 = Label(top, text="Ingresa un sustantivo: ", bg='lightblue').place(x=40, y=120)
        numero = Label(top, text="Ingresa un número: ", bg='lightblue').place(x=40, y=150)
        adjetivo2 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=180)
        celebridad = Label(top, text="Ingresa una celebridad: ", bg='lightblue').place(x=40, y=210)
        adjetivo3 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=240)
        verbo1 = Label(top, text="Ingresa un verbo: ", bg='lightblue').place(x=40, y=270)
        verbo2 = Label(top, text="Ingresa un verbo: ", bg='lightblue').place(x=40, y=300)
        adjetivo4 = Label(top, text="Ingresa un adjetivo: ", bg='lightblue').place(x=40, y=330)

        area_ingreso_adjetivo1 = Entry(top, width=30)
        area_ingreso_adjetivo1.place(x=210, y=60)
        area_ingreso_sustantivo1 = Entry(top, width=30)
        area_ingreso_sustantivo1.place(x=210, y=90)
        area_ingreso_sustantivo2 = Entry(top, width=30)
        area_ingreso_sustantivo2.place(x=210, y=120)
        area_ingreso_numero = Entry(top, width=30)
        area_ingreso_numero.place(x=210, y=150)
        area_ingreso_adjetivo2 = Entry(top, width=30)
        area_ingreso_adjetivo2.place(x=210, y=180)
        area_ingreso_celebridad = Entry(top, width=30)
        area_ingreso_celebridad.place(x=210, y=210)
        area_ingreso_adjetivo3 = Entry(top, width=30)
        area_ingreso_adjetivo3.place(x=210, y=240)
        area_ingreso_verbo1 = Entry(top, width=30)
        area_ingreso_verbo1.place(x=210, y=270)
        area_ingreso_verbo2 = Entry(top, width=30)
        area_ingreso_verbo2.place(x=210, y=300)
        area_ingreso_adjetivo4 = Entry(top, width=30)
        area_ingreso_adjetivo4.place(x=210, y=330)
        boton_enviar = Button(top, text="Enviar", background="SteelBlue", font=('Times', 12, 'bold'),
                            command=lambda: terminar_madlib5(top, area_ingreso_adjetivo1.get(),
                                                            area_ingreso_sustantivo1.get(),
                                                            area_ingreso_sustantivo2.get(),
                                                            area_ingreso_numero.get(),
                                                            area_ingreso_adjetivo2.get(),
                                                            area_ingreso_celebridad.get(),
                                                            area_ingreso_adjetivo3.get(),
                                                            area_ingreso_verbo1.get(),
                                                            area_ingreso_verbo2.get(),
                                                            area_ingreso_adjetivo4.get()))
        boton_enviar.place(x=40, y=600)
        top.mainloop()

    Button(root, text= 'El robo', font ='arial 15', command= madlib1, bg = 'white').place(x=250, y=120)
    Button(root, text= 'El viaje', font ='arial 15', command = madlib2, bg = 'white').place(x=250, y=180)
    Button(root, text= 'Animal', font ='arial 15', command = madlib3, bg = 'white').place(x=250, y=240)
    Button(root, text= 'Guerra', font ='arial 15', command = madlib4, bg = 'white').place(x=250, y=300)
    Button(root, text= 'Fórmula 1', font ='arial 15', command = madlib5, bg = 'white').place(x=235, y=360)
    root.mainloop()