#Danica and Mustafa
#ISAT 340

#import the builtin sqlite3 module
import sqlite3

#create or comment to an existing database
conn = sqlite3.connect("celebrities.db")

#get a cursor to work with the database
cursor = conn.cursor()

#create a table called "celebs"
celebstable = "create table celebs(celebID integer NOT NULL PRIMARY KEY, firstname text, lastname text, age integer, email text, photo text, bio text)"
cursor.execute(celebstable)
conn.commit()

#create a table called "members"
memberstable = "create table members(memberID integer NOT NULL PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"
cursor.execute(memberstable)
conn.commit()

#data supplied as tuple of tuples ? placeholders
insertceleb = "insert into celebs values (?,?,?,?,?,?,?)"
celebdata = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us","https://s3.amazonaws.com/isat3402021/aj.jpg","Angelina Jolie DCMG is an American actress and filmmaker. The recipient of numerous accolades, including an Academy Award and three Golden Globe Awards, she has been named Hollywood's highest-paid actress multiple times."),(2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg","William Bradley Pitt is an American actor and film producer. He is the recipient of numerous accolades, including an Academy Award, a British Academy Film Award, and two Golden Globe Awards for his acting."),(3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg","Snow White is the titular protagonist of Disney's first animated feature-length film, Snow White and the Seven Dwarfs. She is a young princess, the 'Fairest One of All', whose beauty is defined by her inherent kindness and purity."),(4,"Darth","Vader",29,"dv@darkside.me","https://s3.amazonaws.com/isat3402021/dv.jpg", "Darth Vader is a fictional character in the Star Wars franchise. The character is the primary antagonist in the original trilogy and, as Anakin Skywalker, is a primary protagonist in the prequel trilogy. Star Wars creator George Lucas has collectively referred to the first six episodic films of the franchise as 'the tragedy of Darth Vader'."),(5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg", "Taylor Alison Swift is an American singer-songwriter. Her discography spans genres and her narrative songwriting, which is often inspired by her personal life, has received widespread media coverage and critical praise."),(6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", "Beyoncé Giselle Knowles-Carter is an American singer, songwriter, and actress. Born and raised in Houston, Texas, Beyoncé performed in various singing and dancing competitions as a child. She rose to fame in the late 1990s as the lead singer of Destiny's Child, one of the best-selling girl groups of all time."),(7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg", "Selena Marie Gomez is an American singer, actress, and producer. Born and raised in Texas, Gomez began her acting career on the children's television series Barney & Friends. In her teenage years, she rose to prominence for herlead role as Alex Russo in the Disney Channel television series Wizards of Waverly Place."),(8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "Wardell Stephen Curry II is an American professional basketball player for the Golden State Warriors of the National Basketball Association. He plays the point guard position, and is widely regarded as one of the greatest point guards of all time. Many analysts and players have called him the greatest shooter in NBA history."))
cursor.executemany(insertceleb, celebdata)
conn.commit()

#insert data into members table using ? as placeholders
insertmembers = "insert into members values (?,?,?,?,?,?)"
membersdata = ((1,"Danica", "Tran", 21, "tran3dx@dukes.jmu.edu", "I am a 3rd year JMU student, majoring in ISAT...."),(2, "Mufasa", "Hafeez", 21, "hafeezmx@dukes.jmu.edu", "I was born and raised in Alexandria, Virginia...."))
cursor.executemany(insertmembers, membersdata)
conn.commit()

#create table called "member_login" 
member_login = "create table member_login(memberID integer NOT NULL PRIMARY KEY, username text, password text)"
cursor.execute(member_login)
conn.commit()

#insert data into member_login table with ? placeholders
insertusername = "insert into member_login values (?,?,?)"
insertpassword = ((1, "danica", "danica"),(2, "mufasa", "mufasa"))
cursor.executemany(insertusername, insertpassword)
conn.commit()

#close the connection
conn.commit()
conn.close()
