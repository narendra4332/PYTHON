# Nested Dictionary - nested dictionary means putting a dictionary inside another dictionary.
#its a collection of dictionaries into one single dictionary

# employes ={
#     'employe1':{'name':'narendra','id':123},
#     'employe2':{'name':'raja','id':124},
#     'employe3':{'name':'Shankar','id':125}
# }

# print(employes,"\n")
# print(employes['employe1'],"\n")
# print(employes['employe1']['name'],"\n")


# for a,obj in employes.items():
#     print("\n",a,':')

#     for b in obj:
#         print(b+':',obj[b],)

# employes['employe1']['name']="Abhi"
# print("\n",employes)


client1={
    "name" : "narendra",
    "phone": 6264213443,
    "city": "bhopal"
}
client2={
    "name" : "Shankar",
    "phone": 6264213443,
    "city": "vidish"
}
client3={
    "name" : "Keshav",
    "phone": 6264213443,
    "city": "indor"
}

client={
    "client1":client1,
    "client2":client2,
    "client3":client3
}

print(client)