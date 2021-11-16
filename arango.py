from pyArango.connection import *

conn = Connection(arangoURL='http://192.168.0.34:8529' ,username="root", password="ashu1995")

#db = conn.createDatabase(name="school")

print(dir(conn.databases['school']))
# db = conn["school"]

# studentsCollection = db.createCollection(name="student")

# doc1 = studentsCollection.createDocument()
# doc1["name"] = "John Smith"
# doc2 = studentsCollection.createDocument()
# doc2["firstname"] = "Emily"

# doc2["lastname"] = "Bronte"
# doc1._key = "johnsmith"
# doc1.save()

# students = [('Oscar', 'Wilde', 3.5), ('Thomas', 'Hobbes', 3.2), 
# ('Mark', 'Twain', 3.0), ('Kate', 'Chopin', 3.8), ('Fyodor', 'Dostoevsky', 3.1), 
# ('Jane', 'Austen',3.4), ('Mary', 'Wollstonecraft', 3.7), ('Percy', 'Shelley', 3.5), 
# ('William', 'Faulkner', 3.8), ('Charlotte', 'Bronte', 3.0)]

# for (first, last, gpa) in students:
#     doc = studentsCollection.createDocument()
#     doc['name'] = "%s %s" % (first, last)
#     doc['gpa'] = gpa 
#     doc['year'] = 2017
#     doc._key = ''.join([first, last]).lower() 
#     doc.save()