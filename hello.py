import sys
import sqlite3
import wikipedia


search = "Bill Clinton"

# con = sqlite3.connect('wikipedia_py')
# cur = con.cursor()
# cur = con.cursor()
# cur.execute('''CREATE TABLE famous_people
#            (ID integer primary key, name text, summary text)''')
# con.commit()
# con.close()




if wikipedia.search(search) == []:
    print("I dont not know this person")
    print("Did you mean " + wikipedia.suggest(search) + " ?")

else:
    
    sum = wikipedia.page(search).summary
   
    con = sqlite3.connect('wikipedia_py')
    cur = con.cursor()
    cur.execute("INSERT INTO famous_people (name, summary) VALUES (?, ?)", (search, sum))
    con.commit()
    con.close()



 
