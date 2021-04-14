from tinydb import TinyDB,Query

db=TinyDB("database.json")

user1={"name":"Jamshid","age":19,"number":995577}
user2={"name":"Xurshid","age":10,"number":112233}
user3={"name":{"laqabi1":"sher","name":"sherzod"},"age":20}

db.truncate()
db.insert_multiple([user1,user2,user3])


