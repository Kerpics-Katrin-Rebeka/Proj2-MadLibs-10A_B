from tkinter import *


def hun_main():
    root = Tk()
    root.geometry('600x800')
    root.title('Mad Libs Játék')
    root.resizable(False, False)
    root.configure(bg='lightblue')
    Label(root, text='Mad Libs Játék \n Jó játékot!' , font='arial 20 bold', bg='lightblue').pack()
    Label(root, text='Válasszon történetet :', font='arial 15 bold', bg='lightblue').place(x=191, y=80)


    def madlib1():
        def finish_madlib(tl: Toplevel, melleknev1, fonev1, melleknev2, fonev2, melleknev3, fonev3, melleknev4, fonev4, melleknev5, fonev5,melleknev6, fonev6, melleknev7, fonev7):
            text = f'''Volt egyszer egy bátor,{melleknev1} {fonev1}, aki elindult egy küldetésre, hogy megtalálja a(z) {melleknev2} {fonev2}-t. Útközben találkozott egy {melleknev3} {fonev3}-val/vel, egy {melleknev4} {fonev4}-val/vel és egy {melleknev5} {fonev5}-val/vel. De a {melleknev6} {fonev6}-jével/jával és eltökéltségével sikerült elérnie a célját és megszereznie az {melleknev7} {fonev7}-t/-at/-et, mint jutalmat.'''

            Label(tl, text='A sztori:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='DarkOrange').place(
            x=130, y=480)
            Label(tl, text=text, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='DarkOrange').place(x=0, y=480)

        top = Toplevel(bg='DarkOrange')
        top.title("A jutalom")
        top.geometry('600x600')
        top.resizable(False, False)

        Label(top, text='A Jutalom - Mad Libs', font=("Times", 17, 'bold'), bg='DarkOrange').place(
            x=115, y=0)
        
        melleknev1 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 60) 
        fonev1 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 90)
        melleknev2 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 120)
        fonev2 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 150)
        melleknev3 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 180)
        fonev3 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 210)
        melleknev4 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 240)
        fonev4 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 270)
        melleknev5 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 300)
        fonev5 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 330)
        melleknev6 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 360)
        fonev6 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 390)
        melleknev7 = Label(top, text = "Adjon meg egy melléknevet: ", bg='DarkOrange').place(x = 40, y = 420)
        fonev7 = Label(top, text = "Adjon meg egy főnevet: ", bg='DarkOrange').place(x = 40, y = 450) 
        
        melleknev1_input_area = Entry(top, width = 30)
        melleknev1_input_area.place(x = 210, y = 60) 
        fonev1_entry_area = Entry(top, width = 30)
        fonev1_entry_area.place(x = 210, y = 90)
        melleknev2_input_area = Entry(top, width = 30)
        melleknev2_input_area.place(x = 210, y = 120)
        fonev2_entry_area = Entry(top, width = 30)
        fonev2_entry_area.place(x = 210, y = 150)
        melleknev3_input_area = Entry(top, width = 30)
        melleknev3_input_area.place(x = 210, y = 180)
        fonev3_entry_area = Entry(top, width = 30)
        fonev3_entry_area.place(x = 210, y = 210)
        melleknev4_input_area = Entry(top, width = 30)
        melleknev4_input_area.place(x = 210, y = 240)
        fonev4_entry_area = Entry(top, width = 30)
        fonev4_entry_area.place(x = 210, y = 270)
        melleknev5_input_area = Entry(top, width = 30)
        melleknev5_input_area.place(x = 210, y = 300)
        fonev5_entry_area = Entry(top, width = 30)
        fonev5_entry_area.place(x = 210, y = 330)
        melleknev6_input_area = Entry(top, width = 30)
        melleknev6_input_area.place(x = 210, y = 360)
        fonev6_entry_area = Entry(top, width = 30)
        fonev6_entry_area.place(x = 210, y = 390)
        melleknev7_input_area = Entry(top, width = 30)
        melleknev7_input_area.place(x = 210, y = 420)
        fonev7_entry_area = Entry(top, width = 30)
        fonev7_entry_area.place(x = 210, y = 450)
        submit_btn = Button(top, text="Bevitel", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finish_madlib(top, melleknev1_input_area.get(), fonev1_entry_area.get(), melleknev2_input_area.get(), fonev2_entry_area.get(), melleknev3_input_area.get(), fonev3_entry_area.get(), melleknev4_input_area.get(), fonev4_entry_area.get(), melleknev5_input_area.get(), fonev5_entry_area.get(), melleknev6_input_area.get(),fonev6_entry_area.get(), melleknev7_input_area.get(), fonev7_entry_area.get()))
        submit_btn.place(x=40, y=480)

        top.mainloop()


    def madlib2():
        def finish_madlib2(tl: Toplevel, melleknev1, foglalkozas1, melleknev2, foglalkozas2, foglalkozas3, foglalkozas4, melleknev3, foglalkozas5):
            text = f'''Volt egyszer egy titokzatos {melleknev1} város, amelyről senki sem tudta, hol található. Egy nap azonban egy fiatal {foglalkozas1} útnak indult, hogy megtalálja az elveszett várost. Útközben találkozott egy {melleknev2} {foglalkozas2}-al/el/val/vel, aki segített neki átvészelni az erdőt, a hegyeket és a folyókat. Végül megérkeztek a városba, ahol egy titokzatos {foglalkozas3} várta őket és elárulta az elveszett város sötét titkait. A fiatal {foglalkozas4} és a {melleknev3} {foglalkozas5} elhatározták, hogy segítenek megmenteni a várost, mielőtt késő lenne.'''

            Label(tl, text='A sztori:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='red').place(
            x=130, y=300)
            Label(tl, text=text, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='red').place(x=0, y=300)

        top = Toplevel(bg='red')
        top.title("A titokzatos város")
        top.geometry('600x420')
        top.resizable(False, False)

        Label(top, text='A titokzatos város - Mad Libs', font=("Times", 17, 'bold'), bg='red').place(
            x=115, y=0)
        
        melleknev1 = Label(top, text = "Adjon meg egy melléknevet: ",bg='red').place(x = 40, y = 60) 
        foglalkozas1 = Label(top, text = "Adjon meg egy foglalkozást: ",bg='red').place(x = 40, y = 90)
        melleknev2 = Label(top, text = "Adjon meg egy melléknevet: ",bg='red').place(x = 40, y = 120)
        foglalkozas2 = Label(top, text = "Adjon meg egy foglalkozást: ",bg='red').place(x = 40, y = 150)
        foglalkozas3 = Label(top, text = "Adjon meg egy foglalkozást: ",bg='red').place(x = 40, y = 180)
        foglalkozas4 = Label(top, text = "Adjon meg egy foglalkozást: ",bg='red').place(x = 40, y = 210)
        melleknev3 = Label(top, text = "Adjon meg egy melléknevet: ",bg='red').place(x = 40, y = 240)
        foglalkozas5 = Label(top, text = "Adjon meg egy foglalkozást: ",bg='red').place(x = 40, y = 270)

        
        melleknev1_input_area = Entry(top, width = 30)
        melleknev1_input_area.place(x = 210, y = 60) 
        foglalkozas1_entry_area = Entry(top, width = 30)
        foglalkozas1_entry_area.place(x = 210, y = 90)
        melleknev2_input_area = Entry(top, width = 30)
        melleknev2_input_area.place(x = 210, y = 120)
        foglalkozas2_entry_area = Entry(top, width = 30)
        foglalkozas2_entry_area.place(x = 210, y = 150)
        foglalkozas3_input_area = Entry(top, width = 30)
        foglalkozas3_input_area.place(x = 210, y = 180)
        foglalkozas4_entry_area = Entry(top, width = 30)
        foglalkozas4_entry_area.place(x = 210, y = 210)
        melleknev3_input_area = Entry(top, width = 30)
        melleknev3_input_area.place(x = 210, y = 240)
        foglalkozas5_entry_area = Entry(top, width = 30)
        foglalkozas5_entry_area.place(x = 210, y = 270)
        submit_btn = Button(top, text="Bevitel", background="SteelBlue", font=('Times', 12, 'bold'), command=lambda: finish_madlib2(top, melleknev1_input_area.get(), foglalkozas1_entry_area.get(), melleknev2_input_area.get(), foglalkozas2_entry_area.get(), foglalkozas3_input_area.get(), foglalkozas4_entry_area.get(), melleknev3_input_area.get(), foglalkozas5_entry_area.get()))
        submit_btn.place(x=40, y=300)
        top.mainloop()

    def madlib3():
        def finish_madlib3(tl: Toplevel, adjective1, noun1, noun2, number, adjective2, celebrity, adjective3, verb1, verb2, adjective4):
            text = f'''A Formula 1 az én kedvenc {adjective1} sportom. A(z) {noun1} illata és a {noun2} hangja, ahogy a versenyzők {number} km/h sebességgel száguldanak el, igazán {adjective2}. A kedvenc versenyzőm {celebrity}, aki elképesztő {adjective3}-val/vel rendelkezik és mindig úgy tűnik, hogy a megfelelő időben {verb1}. Alig várom, hogy lássam, ki nyeri az idei szezonban a {adjective4} trófeát!'''
            Label(tl, text='A történet:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
                x=130, y=500)
            Label(tl, text=text, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Formula 1")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Formula 1 - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        adjective1 = Label(top, text="Adj meg egy mellékvenet: ", bg='lightblue').place(x=40, y=60)
        noun1 = Label(top, text="Adj meg egy főnevet: ", bg='lightblue').place(x=40, y=90)
        noun2 = Label(top, text="Adj meg egy főnevet: ", bg='lightblue').place(x=40, y=120)
        number = Label(top, text="Adj meg egy számot: ", bg='lightblue').place(x=40, y=150)
        adjective2 = Label(top, text="Adj meg egy mellékvenet: ", bg='lightblue').place(x=40, y=180)
        celebrity = Label(top, text="Adj meg egy hírességet: ", bg='lightblue').place(x=40, y=210)
        adjective3 = Label(top, text="Adj meg egy mellékvenet: ", bg='lightblue').place(x=40, y=240)
        verb1 = Label(top, text="Adj meg egy igét: ", bg='lightblue').place(x=40, y=270)
        verb2 = Label(top, text="Adj meg egy igét: ", bg='lightblue').place(x=40, y=300)
        adjective4 = Label(top, text="Adj meg egy mellékvenet: ", bg='lightblue').place(x=40, y=330)

        adjective1_input_area = Entry(top, width=30)
        adjective1_input_area.place(x=210, y=60)
        noun1_entry_area = Entry(top, width=30)
        noun1_entry_area.place(x=210, y=90)
        noun2_input_area = Entry(top, width=30)
        noun2_input_area.place(x=210, y=120)
        number_entry_area = Entry(top, width=30)
        number_entry_area.place(x=210, y=150)
        adjective2_input_area = Entry(top, width=30)
        adjective2_input_area.place(x=210, y=180)
        celebrity_entry_area = Entry(top, width=30)
        celebrity_entry_area.place(x=210, y=210)
        adjective3_input_area = Entry(top, width=30)
        adjective3_input_area.place(x=210, y=240)
        verb1_entry_area = Entry(top, width=30)
        verb1_entry_area.place(x=210, y=270)
        verb2_input_area = Entry(top, width=30)
        verb2_input_area.place(x=210, y=300)
        adjective4_entry_area = Entry(top, width=30)
        adjective4_entry_area.place(x=210, y=330)
        submit_btn = Button(top, text="Beküldés", background="SteelBlue", font=('Times', 12, 'bold'),
                            command=lambda: finish_madlib3(top, adjective1_input_area.get(), noun1_entry_area.get(),
                                                        noun2_input_area.get(), number_entry_area.get(),
                                                        adjective2_input_area.get(), celebrity_entry_area.get(),
                                                        adjective3_input_area.get(), verb1_entry_area.get(),
                                                        verb2_input_area.get(), adjective4_entry_area.get()))
        submit_btn.place(x=40, y=600)
        top.mainloop()

    def madlib4():
        def finish_madlib4(tl: Toplevel, játék_név, főnév2, szám1, főnév1, ePer3, személy, melléknév2, ige2, melléknév3):
            text = f'''A {játék_név} nevű játék a kedvencem. Szeretem, hogy egy {főnév2} segítségével kell {szám1} {főnév1}-t {ePer3ige}-ni. A legjobb része, hogy {személy} játszhatja a {melléknév2} karaktert, és mindig {melléknév3} {ige2} a legjobb pillanatban. Alig várom, hogy újra játszhassam a {játék_név}-t!'''
            Label(tl, text='A történet:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(
            x=130, y=500)
            Label(tl, text=text, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Társasjáték")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Társasjáték - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(
            x=115, y=0)

        játék_név = Label(top, text="Adj meg egy játéknevet: ", bg='lightblue').place(x=40, y=60)
        főnév2 = Label(top, text="Adj meg egy főnevet: ", bg='lightblue').place(x=40, y=90)
        szám1 = Label(top, text="Adj meg egy számot: ", bg='lightblue').place(x=40, y=120)
        főnév1 = Label(top, text="Adj meg egy főnevet: ", bg='lightblue').place(x=40, y=150)
        ePer3ige = Label(top, text="Adj meg egy E/3-as igét: ", bg='lightblue').place(x=40, y=180)
        személy = Label(top, text="Adj meg egy személyt: ", bg='lightblue').place(x=40, y=210)
        melléknév2 = Label(top, text="Adj meg egy melléknévet: ", bg='lightblue').place(x=40, y=240)
        ige2 = Label(top, text="Adj meg egy igét: ", bg='lightblue').place(x=40, y=270)
        melléknév3 = Label(top, text="Adj meg egy hogyan-ra válaszolló névmást: ", bg='lightblue').place(x=40, y=300)

        játék_név_input_area = Entry(top, width=30)
        játék_név_input_area.place(x=210, y=60)
        főnév2_entry_area = Entry(top, width=30)
        főnév2_entry_area.place(x=210, y=90)
        szám1_entry_area = Entry(top, width=30)
        szám1_entry_area.place(x=210, y=120)
        főnév1_entry_area = Entry(top, width=30)
        főnév1_entry_area.place(x=210, y=150)
        ePer3ige_entry_area = Entry(top, width=30)
        ePer3ige_entry_area.place(x=210, y=180)
        személy_entry_area = Entry(top, width=30)
        személy_entry_area.place(x=210, y=210)
        melléknév2_entry_area = Entry(top, width=30)
        melléknév2_entry_area.place(x=210, y=240)
        főnév2_entry_area = Entry(top, width=30)
        főnév2_entry_area.place(x=210, y=270)
        melléknév3_entry_area = Entry(top, width=30)
        melléknév3_entry_area.place(x=210, y=300)
        submit_btn = Button(top, text="Beküldés", background="SteelBlue",
                            font=('Times', 12, 'bold'),
                            command=lambda: finish_madlib4(top, játék_név_input_area.get(), főnév2_entry_area.get(),
                                                        szám1_entry_area.get(), főnév1_entry_area.get(),
                                                        ePer3ige_entry_area.get(), személy_entry_area.get(),
                                                        melléknév2_entry_area.get(), főnév2_entry_area.get(),
                                                        melléknév3_entry_area.get()))
        submit_btn.place(x=40, y=600)
        top.mainloop()

    def madlib5():
        def finish_madlib5(tl: Toplevel, noun1, adjective1, adjective2, noun2, number, verb1, noun3, verb2, adjective3):
            text = f'''A(z) {noun1} iskolában minden nap {adjective1} érzéssel kezdem a napot. Az osztályteremben {adjective2} {noun2} találhatók, és {number} darab szék vár ránk. Az első óra alatt mindig {verb1} {noun3}-t tanulunk, majd a szünetben lehetőségünk van {verb2} a {adjective3} udvaron.'''
            Label(tl, text='A történet:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='lightblue').place(x=130, y=500)
            Label(tl, text=text, font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='lightblue').place(x=0, y=500)

        top = Toplevel(bg='lightblue')
        top.title("Iskolai élet")
        top.geometry('600x700')
        top.resizable(False, False)

        Label(top, text='Iskolai élet - Mad Libs', font=("Times", 17, 'bold'), bg='lightblue').place(x=115, y=0)

        noun1 = Label(top, text="Ajd meg egy főnevet: ", bg='lightblue').place(x=40, y=60)
        adjective1 = Label(top, text="Ajd meg egy melléknevet: ", bg='lightblue').place(x=40, y=90)
        adjective2 = Label(top, text="Ajd meg egy melléknevet: ", bg='lightblue').place(x=40, y=120)
        noun2 = Label(top, text="Ajd meg egy főnevet: ", bg='lightblue').place(x=40, y=150)
        number = Label(top, text="Ajd meg egy számot: ", bg='lightblue').place(x=40, y=180)
        verb1 = Label(top, text="Ajd meg egy igét: ", bg='lightblue').place(x=40, y=210)
        noun3 = Label(top, text="Ajd meg egy főnevet: ", bg='lightblue').place(x=40, y=240)
        verb2 = Label(top, text="Ajd meg egy igét: ", bg='lightblue').place(x=40, y=270)
        adjective3 = Label(top, text="Ajd meg egy melléknevet: ", bg='lightblue').place(x=40, y=300)

        noun1_input_area = Entry(top, width=30)
        noun1_input_area.place(x=210, y=60)
        adjective1_input_area = Entry(top, width=30)
        adjective1_input_area.place(x=210, y=90)
        adjective2_input_area = Entry(top, width=30)
        adjective2_input_area.place(x=210, y=120)
        noun2_input_area = Entry(top, width=30)
        noun2_input_area.place(x=210, y=150)
        number_entry_area = Entry(top, width=30)
        number_entry_area.place(x=210, y=180)
        verb1_entry_area = Entry(top, width=30)
        verb1_entry_area.place(x=210, y=210)
        noun3_entry_area = Entry(top, width=30)
        noun3_entry_area.place(x=210, y=240)
        verb2_entry_area = Entry(top, width=30)
        verb2_entry_area.place(x=210, y=270)
        adjective3_entry_area = Entry(top, width=30)
        adjective3_entry_area.place(x=210, y=300)
        submit_btn = Button(top, text="Beküldés", background="SteelBlue", font=('Times', 12, 'bold'),
                            command=lambda: finish_madlib5(top, noun1_input_area.get(), adjective1_input_area.get(),
                                                        adjective2_input_area.get(), noun2_input_area.get(),
                                                        number_entry_area.get(), verb1_entry_area.get(),
                                                        noun3_entry_area.get(), verb2_entry_area.get(),
                                                        adjective3_entry_area.get()))
        submit_btn.place(x=40, y=600)
        top.mainloop()


    Button(root, text= 'A Jutalom', font ='arial 15', command= madlib1, bg = 'white').place(x=240, y=120)
    Button(root, text= 'A titokzatos város', font ='arial 15', command = madlib2, bg = 'white').place(x=210, y=180)
    Button(root, text= 'Formula 1', font ='arial 15', command = madlib3, bg = 'white').place(x=240, y=240)
    Button(root, text= 'Játék', font ='arial 15', command = madlib4, bg = 'white').place(x=257, y=300)
    Button(root, text= 'Iskola', font ='arial 15', command = madlib5, bg = 'white').place(x=255, y=360)

    root.mainloop()
