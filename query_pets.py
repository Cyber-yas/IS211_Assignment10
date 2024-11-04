import sqlite3


conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    person_id = input("Enter a person's ID number (or -1 to exit): ")
    if person_id == '-1':
        break

    cursor.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()

    if person:
        print(f"{person[1]} {person[2]}, {person[3]} years old")

        cursor.execute('SELECT p.name, p.breed, p.age FROM pet p '
                       'JOIN person_pet pp ON p.id = pp.pet_id '
                       'WHERE pp.person_id = ?', (person_id,))
        pets = cursor.fetchall()

        for pet in pets:
            print(f"{person[1]} owns {pet[0]}, a {pet[1]} that is {pet[2]} years old.")
    else:
        print("Error: Person not found.")

conn.close()
