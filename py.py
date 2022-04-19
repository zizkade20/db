import tkinter as tk
import sqlite3


window = tk.Tk()
window.title("Fortnite")
window.geometry("580x700")


con = sqlite3.connect("databaze.db")

c = con.cursor()

'''
c.execute("""
    CREATE TABLE person_info (
        jmeno text,
        prijmeni text,
        pohlavi text,
        mobil integer,
        rodne_cislo integer
    )

""")
'''

def Submit():
    r_cislo = rodne_cislo.get()
    r_cisloo = int(r_cislo)
    if len(r_cislo) == 10 and r_cisloo % 11 == 0:
        con = sqlite3.connect("databaze.db")
        c = con.cursor()

        c.execute("""INSERT INTO person_info VALUES (:jmeno, :prijmeni, :pohlavi, :mobil, :rodne_cislo)""",
            {
                'jmeno': jmeno.get(),
                'prijmeni': prijmeni.get(),
                'pohlavi': pohlavi.get(),
                'mobil': mobil.get(),
                'rodne_cislo': rodne_cislo.get()
            }
        )

        con.commit()
        con.close()

        jmeno.delete(0, tk.END)
        prijmeni.delete(0, tk.END)
        pohlavi.delete(0, tk.END)
        mobil.delete(0, tk.END)
        rodne_cislo.delete(0, tk.END)


def Show():

    con = sqlite3.connect("databaze.db")
    c = con.cursor()

    c.execute("SELECT * FROM person_info")
    records = c.fetchall()

    print_records = ""
    for record in records:
        print_records += "\n" + str(record[0]) + " " + str(record[1]) + "\n" + str(record[2]) + "\n+420 " + str(record[3]) + "\n" + str(record[4]) + "\n\n"

    zaznam_label = tk.Label(window, text=print_records)
    zaznam_label.grid(row=13, column=1, columnspan=2)

    con.commit()
    con.close()


def Delete():
    record_id = delete_box.get()
    if len(record_id) > 0:

        con = sqlite3.connect("databaze.db")
        c = con.cursor()

        c.execute("DELETE FROM person_info WHERE rodne_cislo = " + record_id)

        con.commit()
        con.close()

        delete_box.delete(0, tk.END)


def Update():
    con = sqlite3.connect("databaze.db")
    c = con.cursor()

    record_id = edit_box.get()
    c.execute("""UPDATE person_info SET
        jmeno = :jmeno,
        prijmeni = :prijmeni,
        pohlavi = :pohlavi,
        mobil = :mobil
        WHERE rodne_cislo = :rodne_cislo
        """,

        {
            'jmeno': edit_jmeno.get(),
            'prijmeni': edit_prijmeni.get(),
            'pohlavi': edit_pohlavi.get(),
            'mobil': edit_mobil.get(),
            'rodne_cislo': edit_rodne_cislo.get(),
        })


    con.commit()
    con.close()


def Edit():
    record_id = edit_box.get()
    if len(record_id) > 0:
        editor = tk.Tk()
        editor.title("Edit záznamu")
        editor.geometry("480x300")

        con = sqlite3.connect("databaze.db")
        c = con.cursor()

        c.execute("SELECT * FROM person_info WHERE rodne_cislo = " + record_id)
        records = c.fetchall()

        global edit_jmeno
        global edit_prijmeni
        global edit_pohlavi
        global edit_mobil
        global edit_rodne_cislo

        edit_jmeno = tk.Entry(editor, width=30)
        edit_jmeno.grid(row=0, column=1, padx=20)
        edit_jmeno_label = tk.Label(editor, text="Jméno")
        edit_jmeno_label.grid(row=0, column=0)

        edit_prijmeni = tk.Entry(editor, width=30)
        edit_prijmeni.grid(row=1, column=1, padx=20)
        edit_prijmeni_label = tk.Label(editor, text="Příjmení")
        edit_prijmeni_label.grid(row=1, column=0)

        edit_pohlavi = tk.Entry(editor, width=30)
        edit_pohlavi.grid(row=2, column=1, padx=20)
        edit_pohlavi_label = tk.Label(editor, text="Pohlaví")
        edit_pohlavi_label.grid(row=2, column=0)

        edit_mobil = tk.Entry(editor, width=30)
        edit_mobil.grid(row=3, column=1, padx=20)
        edit_mobil_label = tk.Label(editor, text="Mobil")
        edit_mobil_label.grid(row=3, column=0)

        edit_rodne_cislo = tk.Entry(editor, width=30)
        edit_rodne_cislo.grid(row=4, column=1, padx=20)
        edit_rodne_cislo_label = tk.Label(editor, text="Rodné číslo")
        edit_rodne_cislo_label.grid(row=4, column=0)


        for record in records:
            edit_jmeno.insert(0, record[0])
            edit_prijmeni.insert(0, record[1])
            edit_pohlavi.insert(0, record[2])
            edit_mobil.insert(0, record[3])
            edit_rodne_cislo.insert(0, record[4])

        update_button = tk.Button(editor, text="uložit změny", command=Update)
        update_button.grid(row=5, column=1, pady=20)

        con.commit()
        con.close()


jmeno = tk.Entry(window, width=30)
jmeno.grid(row=0, column=1, padx=20)
jmeno_label = tk.Label(window, text="Jméno")
jmeno_label.grid(row=0, column=0)

prijmeni = tk.Entry(window, width=30)
prijmeni.grid(row=1, column=1, padx=20)
prijmeni_label = tk.Label(window, text="Příjmení")
prijmeni_label.grid(row=1, column=0)

pohlavi = tk.Entry(window, width=30)
pohlavi.grid(row=2, column=1, padx=20)
pohlavi_label = tk.Label(window, text="Pohlaví")
pohlavi_label.grid(row=2, column=0)

mobil = tk.Entry(window, width=30)
mobil.grid(row=3, column=1, padx=20)
mobil_label = tk.Label(window, text="Mobil")
mobil_label.grid(row=3, column=0)

rodne_cislo = tk.Entry(window, width=30)
rodne_cislo.grid(row=4, column=1, padx=20)
rodne_cislo_label = tk.Label(window, text="Rodné číslo")
rodne_cislo_label.grid(row=4, column=0)

delete_box = tk.Entry(window, width=30)
delete_box.grid(row=8, column=1)
delete_label = tk.Label(window, text="zadejte rodné číslo,\nkteré chcete smazat")
delete_label.grid(row=8, column=0)

edit_box = tk.Entry(window, width=30)
edit_box.grid(row=10, column=1)
edit_label = tk.Label(window, text="zadejte rodné číslo,\nu kterého chcete změnit údaje")
edit_label.grid(row=10, column=0)


odeslat = tk.Button(window, text="odesat", command=Submit)
odeslat.grid(row=5, column=1, columnspan=2, pady=10, padx=10, ipadx=115)

odeslat = tk.Button(window, text="zobrazit záznamy", command=Show)
odeslat.grid(row=12, column=1, columnspan=2, pady=10, padx=10, ipadx=80)

delete = tk.Button(window, text="smazat záznam", command=Delete)
delete.grid(row=9, column=1, columnspan=2, pady=10, padx=10, ipadx=85)

delete = tk.Button(window, text="upravit záznam", command=Edit)
delete.grid(row=11, column=1, columnspan=2, pady=10, padx=10, ipadx=86)



con.commit()

con.close()

window.mainloop()


