from tkinter import *


def ita_main():
    root = Tk()
    root.geometry('600x800')
    root.title('Gioco delle Parole Pazze')
    root.resizable(False, False)
    root.configure(bg='lightblue')

    Label(root, text='Gioco delle Parole Pazze\nDivertiti!', font='arial 20 bold', bg='lightblue').pack()
    Label(root, text='Scegli una storia:', font='arial 15 bold', bg='lightblue').place(x=208, y=80)

    def madlib1():
        def finish_madlib(tl: Toplevel, aggettivo1, sostantivo1, aggettivo2, sostantivo2, aggettivo3, sostantivo3, aggettivo4, sostantivo4, aggettivo5, sostantivo5, aggettivo6, sostantivo6, aggettivo7):
            testo = f'''Oggi sono andato al parco {aggettivo1} {sostantivo1} con il mio {aggettivo2} {sostantivo2}. Abbiamo portato con noi alcuni {aggettivo3} {sostantivo3} e un {aggettivo4} {sostantivo4} per giocare. Mentre stavamo giocando, è passato
                         di corsa un {aggettivo5} {sostantivo5} e ci ha rubato il nostro {aggettivo6} {sostantivo6}! Abbiamo cercato di inseguirlo, ma era troppo {aggettivo7} per essere preso. Nonostante l'incidente, ci siamo divertiti molto al parco e
                         non vediamo l'ora di tornarci.'''
            Label(tl, text='La storia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=480)
            Label(tl, text=testo, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=480)

        top = Toplevel(bg='lightblue')
        top.title("Il furto")
        top.geometry('600x600')
        top.resizable(False, False)

        Label(top, text='Il furto - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(x=115, y=0)

        aggettivo1 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=60)
        sostantivo1 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=90)
        aggettivo2 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=120)
        sostantivo2 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=150)
        aggettivo3 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=180)
        sostantivo3 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=210)
        aggettivo4 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=240)
        sostantivo4 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=270)
        aggettivo5 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=300)
        sostantivo5 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=330)
        aggettivo6 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=360)
        sostantivo6 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=390)
        aggettivo7 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=420)

        aggettivo1_input_area = Entry(top, width=30)
        aggettivo1_input_area.place(x=210, y=60)
        sostantivo1_entry_area = Entry(top, width=30)
        sostantivo1_entry_area.place(x=210, y=90)
        aggettivo2_input_area = Entry(top, width=30)
        aggettivo2_input_area.place(x=210, y=120)
        sostantivo2_entry_area = Entry(top, width=30)
        sostantivo2_entry_area.place(x=210, y=150)
        aggettivo3_input_area = Entry(top, width=30)
        aggettivo3_input_area.place(x=210, y=180)
        sostantivo3_entry_area = Entry(top, width=30)
        sostantivo3_entry_area.place(x=210, y=210)
        aggettivo4_input_area = Entry(top, width=30)
        aggettivo4_input_area.place(x=210, y=240)
        sostantivo4_entry_area = Entry(top, width=30)
        sostantivo4_entry_area.place(x=210, y=270)
        aggettivo5_input_area = Entry(top, width=30)
        aggettivo5_input_area.place(x=210, y=300)
        sostantivo5_entry_area = Entry(top, width=30)
        sostantivo5_entry_area.place(x=210, y=330)
        aggettivo6_input_area = Entry(top, width=30)
        aggettivo6_input_area.place(x=210, y=360)
        sostantivo6_entry_area = Entry(top, width=30)
        sostantivo6_entry_area.place(x=210, y=390)
        aggettivo7_input_area = Entry(top, width=30)
        aggettivo7_input_area.place(x=210, y=420)
        submit_btn = Button(top, text="Invia", background="SteelBlue", font=('Times', 12, 'bold'),
                            command=lambda: finish_madlib(top, aggettivo1_input_area.get(), sostantivo1_entry_area.get(),
                                                           aggettivo2_input_area.get(), sostantivo2_entry_area.get(),
                                                           aggettivo3_input_area.get(), sostantivo3_entry_area.get(),
                                                           aggettivo4_input_area.get(), sostantivo4_entry_area.get(),
                                                           aggettivo5_input_area.get(), sostantivo5_entry_area.get(),
                                                           aggettivo6_input_area.get(), sostantivo6_entry_area.get(),
                                                           aggettivo7_input_area.get()))
        submit_btn.place(x=40, y=480)
        top.mainloop()

    def madlib2():
        def finish_madlib2(tl: Toplevel, aggettivo1, sostantivo1, aggettivo2, aggettivo3, sostantivo2, aggettivo4, sostantivo3, sostantivo4, aggettivo5, sostantivo5, aggettivo6, sostantivo6, aggettivo7, sostantivo7, aggettivo8, sostantivo8, aggettivo9):
            testo = f'''C'era una volta, un(a) {aggettivo1} {sostantivo1} che si mise in viaggio {aggettivo2}. Avevano preparato un(a) {aggettivo3} {sostantivo2}, un(a) {aggettivo4} {sostantivo3} e un(a) {aggettivo5} {sostantivo4} per il viaggio. Lungo il cammino, incontrarono un(a) {aggettivo6} {sostantivo5} che offrì il suo aiuto. Insieme, affrontarono un(a) {aggettivo7} {sostantivo6} e alla fine scoprirono un(a) {aggettivo8} {sostantivo7}. Il/la {aggettivo9} {sostantivo8} tornò a casa.'''
            Label(tl, text='La storia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=600)
            Label(tl, text=testo, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=600)

        top = Toplevel(bg='lightblue')
        top.title("Il viaggio")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Il viaggio - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)
        
        aggettivo1 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=60)
        sostantivo1 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=90)
        aggettivo2 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=120)
        aggettivo3 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=150)
        sostantivo2 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=180)
        aggettivo4 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=210)
        sostantivo3 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=240)
        sostantivo4 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=270)
        aggettivo5 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=300)
        sostantivo5 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=330)
        aggettivo6 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=360)
        sostantivo6 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=390)
        aggettivo7 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=420)
        sostantivo7 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=450)
        aggettivo8 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=480)
        sostantivo8 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=510)
        aggettivo9 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=540)
        
        aggettivo1_area_input = Entry(top, width=30)
        aggettivo1_area_input.place(x=210, y=60)
        sostantivo1_area_input = Entry(top, width=30)
        sostantivo1_area_input.place(x=210, y=90)
        aggettivo2_area_input = Entry(top, width=30)
        aggettivo2_area_input.place(x=210, y=120)
        aggettivo3_area_input = Entry(top, width=30)
        aggettivo3_area_input.place(x=210, y=150)
        sostantivo2_area_input = Entry(top, width=30)
        sostantivo2_area_input.place(x=210, y=180)
        aggettivo4_area_input = Entry(top, width=30)
        aggettivo4_area_input.place(x=210, y=210)
        sostantivo3_area_input = Entry(top, width=30)
        sostantivo3_area_input.place(x=210, y=240)
        sostantivo4_area_input = Entry(top, width=30)
        sostantivo4_area_input.place(x=210, y=270)
        aggettivo5_area_input = Entry(top, width=30)
        aggettivo5_area_input.place(x=210, y=300)
        sostantivo5_area_input = Entry(top, width=30)
        sostantivo5_area_input.place(x=210, y=330)
        aggettivo6_area_input = Entry(top, width=30)
        aggettivo6_area_input.place(x=210, y=360)
        sostantivo6_area_input = Entry(top, width=30)
        sostantivo6_area_input.place(x=210, y=390)
        aggettivo7_area_input = Entry(top, width=30)
        aggettivo7_area_input.place(x=210, y=420)
        sostantivo7_area_input = Entry(top, width=30)
        sostantivo7_area_input.place(x=210, y=450)
        aggettivo8_area_input = Entry(top, width=30)
        aggettivo8_area_input.place(x=210, y=480)
        sostantivo8_area_input = Entry(top, width=30)
        sostantivo8_area_input.place(x=210, y=510)
        aggettivo9_area_input = Entry(top, width=30)
        aggettivo9_area_input.place(x=210, y=540)
        
        submit_btn = Button(top, text="Invia", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finish_madlib2(top, aggettivo1_area_input.get(), sostantivo1_area_input.get(), aggettivo2_area_input.get(), aggettivo3_area_input.get(), sostantivo2_area_input.get(), aggettivo4_area_input.get(), sostantivo3_area_input.get(), sostantivo4_area_input.get(), aggettivo5_area_input.get(), sostantivo5_area_input.get(), aggettivo6_area_input.get(), sostantivo6_area_input.get(), aggettivo7_area_input.get(), sostantivo7_area_input.get(), aggettivo8_area_input.get(), sostantivo8_area_input.get(), aggettivo9_area_input.get()))
        submit_btn.place(x=40, y=600)
        top.mainloop()

    def madlib3():
        def finish_madlib3(tl: Toplevel, animale1, aggettivo1, parte_del_corpo1, cibo1, numero1, parte_del_corpo2, numero2, parte_del_corpo3, aggettivo2, azione, lavoro, aggettivo3, aggettivo4, sostantivo1):
            testo = f'''Il {animale1} è un animale domestico. Un {animale1} ha {aggettivo1} {parte_del_corpo1} in modo da poter mangiare {cibo1} molto facilmente, ha {numero1} {parte_del_corpo2} e {numero2} {parte_del_corpo3}. È un animale molto {aggettivo2} e è molto utile in {azione} {lavoro}. Corre molto {aggettivo3}, abbaia {aggettivo4} e attacca il {sostantivo1}. Si possono trovare {animale1} ovunque nel mondo.'''
            Label(tl, text='La storia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=500)
            Label(tl, text=testo, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Animale")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Animale - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)
        
        animale1 = Label(top, text="Inserisci un animale: ", bg='lightblue').place(x=40, y=60)
        aggettivo1 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=90)
        parte_del_corpo1 = Label(top, text="Inserisci una parte del corpo: ", bg='lightblue').place(x=40, y=120)
        cibo1 = Label(top, text="Inserisci un cibo: ", bg='lightblue').place(x=40, y=150)
        numero1 = Label(top, text="Inserisci un numero: ", bg='lightblue').place(x=40, y=180)
        parte_del_corpo2 = Label(top, text="Inserisci una parte del corpo: ", bg='lightblue').place(x=40, y=210)
        numero2 = Label(top, text="Inserisci un numero: ", bg='lightblue').place(x=40, y=240)
        parte_del_corpo3 = Label(top, text="Inserisci una parte del corpo: ", bg='lightblue').place(x=40, y=270)
        aggettivo2 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=300)
        azione = Label(top, text="Inserisci un'azione: ", bg='lightblue').place(x=40, y=330)
        lavoro = Label(top, text="Inserisci un lavoro: ", bg='lightblue').place(x=40, y=360)
        aggettivo3 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=390)
        aggettivo4 = Label(top, text="Inserisci un aggettivo: ", bg='lightblue').place(x=40, y=420)
        sostantivo1 = Label(top, text="Inserisci un sostantivo: ", bg='lightblue').place(x=40, y=450)
        
        animale1_input_area = Entry(top, width=30)
        animale1_input_area.place(x=210, y=60)
        aggettivo1_entry_area = Entry(top, width=30)
        aggettivo1_entry_area.place(x=210, y=90)
        parte_del_corpo1_input_area = Entry(top, width=30)
        parte_del_corpo1_input_area.place(x=210, y=120)
        cibo1_entry_area = Entry(top, width=30)
        cibo1_entry_area.place(x=210, y=150)
        numero1_input_area = Entry(top, width=30)
        numero1_input_area.place(x=210, y=180)
        parte_del_corpo2_entry_area = Entry(top, width=30)
        parte_del_corpo2_entry_area.place(x=210, y=210)
        numero2_input_area = Entry(top, width=30)
        numero2_input_area.place(x=210, y=240)
        parte_del_corpo3_entry_area = Entry(top, width=30)
        parte_del_corpo3_entry_area.place(x=210, y=270)
        aggettivo2_input_area = Entry(top, width=30)
        aggettivo2_input_area.place(x=210, y=300)
        azione_entry_area = Entry(top, width=30)
        azione_entry_area.place(x=210, y=330)
        lavoro_input_area = Entry(top, width=30)
        lavoro_input_area.place(x=210, y=360)
        aggettivo3_entry_area = Entry(top, width=30)
        aggettivo3_entry_area.place(x=210, y=390)
        aggettivo4_input_area = Entry(top, width=30)
        aggettivo4_input_area.place(x=210, y=420)
        sostantivo1_entry_area = Entry(top, width=30)
        sostantivo1_entry_area.place(x=210, y=450)
        submit_btn = Button(top, text="Invia", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finish_madlib3(top, animale1_input_area.get(), aggettivo1_entry_area.get(), parte_del_corpo1_input_area.get(), cibo1_entry_area.get(), numero1_input_area.get(), parte_del_corpo2_entry_area.get(), numero2_input_area.get(), parte_del_corpo3_entry_area.get(), aggettivo2_input_area.get(), azione_entry_area.get(), lavoro_input_area.get(), aggettivo3_entry_area.get(), aggettivo4_input_area.get(), sostantivo1_entry_area.get()))
        submit_btn.place(x=40, y=600)
        top.mainloop()

    def madlib4():
        def finish_madlib4(tl: Toplevel, anno, paese1, nazionalita1, luogo1, paese2, numero):
            testo = f'''Il 7 dicembre {anno}, {paese1} ha lanciato un attacco aereo a sorpresa sulla base navale {nazionalita1} sull'Isola di {luogo1}, {paese2}, costringendo {paese2} ad entrare nella Seconda Guerra Mondiale. L'attacco ha segnato il culmine di un decennio di peggioramento delle relazioni tra {paese1} e {paese2}.'''
            Label(tl, text='La storia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(x=130, y=500)
            Label(tl, text=testo, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Guerra")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Guerra - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(x=115, y=0)

        anno = Label(top, text="Inserisci un anno: ", bg='lightblue').place(x=40, y=60)
        paese1 = Label(top, text="Inserisci un paese: ", bg='lightblue').place(x=40, y=90)
        nazionalita1 = Label(top, text="Inserisci una nazionalità: ", bg='lightblue').place(x=40, y=120)
        luogo1 = Label(top, text="Inserisci un luogo: ", bg='lightblue').place(x=40, y=150)
        paese2 = Label(top, text="Inserisci un paese: ", bg='lightblue').place(x=40, y=180)
        numero = Label(top, text="Inserisci un numero: ", bg='lightblue').place(x=40, y=210)

        area_input_anno = Entry(top, width=30)
        area_input_anno.place(x=210, y=60)
        area_input_paese1 = Entry(top, width=30)
        area_input_paese1.place(x=210, y=90)
        area_input_nazionalita1 = Entry(top, width=30)
        area_input_nazionalita1.place(x=210, y=120)
        area_input_luogo1 = Entry(top, width=30)
        area_input_luogo1.place(x=210, y=150)
        area_input_paese2 = Entry(top, width=30)
        area_input_paese2.place(x=210, y=180)
        area_input_numero = Entry(top, width=30)
        area_input_numero.place(x=210, y=210)

        bottone_invio = Button(top, text="Invia", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finish_madlib4(top, area_input_anno.get(), area_input_paese1.get(), area_input_nazionalita1.get(), area_input_luogo1.get(), area_input_paese2.get(), area_input_numero.get()))
        bottone_invio.place(x=40, y=600)

        top.mainloop()

    def madlib5():
        def finish_madlib5(tl: Toplevel, adjective1, noun1, noun2, number, adjective2, celebrity, adjective3, verb1, verb2, adjective4):
            text = f'''La Formula 1 è il mio sport {adjective1} preferito. L'odore di {noun1} e il suono di {noun2} mentre i piloti sfrecciano a {number} km/h è veramente {adjective2}. Il mio pilota preferito è {celebrity}, che ha una {adjective3} incredibile e sembra sempre {verb1} al momento giusto. Non vedo l'ora di vedere chi vincerà il trofeo {adjective4} questa stagione!'''
            Label(tl, text='La storia:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=500)
            Label(tl, text=text, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Formula 1")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Formula 1 - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        adjective1 = Label(top, text = "Inserisci un aggettivo: ", bg='lightblue').place(x = 40, y = 60) 
        noun1 = Label(top, text = "Inserisci un sostantivo: ", bg='lightblue').place(x = 40, y = 90)
        noun2 = Label(top, text = "Inserisci un sostantivo: ", bg='lightblue').place(x = 40, y = 120)
        number = Label(top, text = "Inserisci un numero: ", bg='lightblue').place(x = 40, y = 150)
        adjective2 = Label(top, text = "Inserisci un aggettivo: ", bg='lightblue').place(x = 40, y = 180)
        celebrity = Label(top, text = "Inserisci una celebrità: ", bg='lightblue').place(x = 40, y = 210)
        adjective3 = Label(top, text = "Inserisci un aggettivo: ", bg='lightblue').place(x = 40, y = 240)
        verb1 = Label(top, text = "Inserisci un verbo: ", bg='lightblue').place(x = 40, y = 270)
        verb2 = Label(top, text = "Inserisci un verbo: ", bg='lightblue').place(x = 40, y = 300)
        adjective4 = Label(top, text = "Inserisci un aggettivo: ", bg='lightblue').place(x = 40, y = 330)

        adjective1_input_area = Entry(top, width = 30)
        adjective1_input_area.place(x = 210, y = 60) 
        noun1_entry_area = Entry(top, width = 30)
        noun1_entry_area.place(x = 210, y = 90)
        noun2_input_area = Entry(top, width = 30)
        noun2_input_area.place(x = 210, y = 120)
        number_entry_area = Entry(top, width = 30)
        number_entry_area.place(x = 210, y = 150)
        adjective2_input_area = Entry(top, width = 30)
        adjective2_input_area.place(x = 210, y = 180)
        celebrity_entry_area = Entry(top, width = 30)
        celebrity_entry_area.place(x = 210, y = 210)
        adjective3_input_area = Entry(top, width = 30)
        adjective3_input_area.place(x = 210, y = 240)
        verb1_entry_area = Entry(top, width = 30)
        verb1_entry_area.place(x = 210, y = 270)
        verb2_input_area = Entry(top, width = 30)
        verb2_input_area.place(x = 210, y = 300)
        adjective4_entry_area = Entry(top, width = 30)
        adjective4_entry_area.place(x = 210, y = 330)
        submit_btn = Button(top, text="Invia", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finish_madlib5(top, adjective1_input_area.get(), noun1_entry_area.get(), noun2_input_area.get(), number_entry_area.get(), adjective2_input_area.get(), celebrity_entry_area.get(), adjective3_input_area.get(), verb1_entry_area.get(), verb2_input_area.get(), adjective4_entry_area.get()))
        submit_btn.place(x=40, y=600)
        top.mainloop()

    Button(root, text= 'Il furto', font ='arial 15', command= madlib1, bg = 'white').place(x=251, y=120)
    Button(root, text= 'Il viaggio', font ='arial 15', command = madlib2, bg = 'white').place(x=243, y=180)
    Button(root, text= 'Animale', font ='arial 15', command = madlib3, bg = 'white').place(x=246, y=240)
    Button(root, text= 'Guerra', font ='arial 15', command = madlib4, bg = 'white').place(x=251, y=300)
    Button(root, text= 'Formula 1', font ='arial 15', command = madlib5, bg = 'white').place(x=238, y=360)
    root.mainloop()