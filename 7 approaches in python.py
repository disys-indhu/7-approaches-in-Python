"types of accessing objects"
"approach 1" # directly giving values

name="indhumathi"

"approach 2" #object using

class friday:
    work="reading"
    def __init__(self):
        self.__tea=4
    def display(self):
        print(self.__tea)
obj=friday()
obj.display() #calling method

        
"approach 3" #indexing

saturday=("sleep","eat","movies","work")

print(saturday[2])


"approach 4" #dictionary 

sunday={"morning":"exercise","sleepy":"worried about tmrw","nyt":"sad"}

print(sunday["morning"])
             
print(sunday.keys())

print(sunday.values())

print(sunday.items())


"approach 5" # using for syntax

# syntax => for in : 

for i in saturday: #im is an object that any one i give and saturday is an object in approach 3
    print(i)

#print(saturday)

for im in sunday.values():
    print(im)

for ir in sunday.keys():
    print(ir)

for ik in sunday.items():
    print(ik)


"approach 6" # inside list there is dictionary

students=[{"id":22,"name":"indhumathi","branch":"cse"},{"id":23,"name":"vj","branch":"mech"},{"id":24,"name":"zumo","branch":"it"}]

print(students[0],students[1])

#another method using for

for i in students:
    if i["name"]=="indhumathi":
        print("indhumathi is there")
    if i["branch"]=="it":
        print("it is there")
   

"approach 7" #inside list there is a key called internship. inside key there is a list.inside list there is  two dictionary

funday=[{"internship":[{"empid":"51","empname":"mani","empphno":"1234567890"},{"empid":"52","empname":"megna","empphno":"1234567899"}],
"fulltime":[{"empid":"61","empname":"teju","empphno":"1234568890"},{"empid":"62","empname":"aarthi","empphno":"1234987890"}],
"contract":[{"empid":"71","empname":"ram","empphno":"1734567890"},{"empid":"62","empname":"janu","empphno":"1234967890"}]}]


for i in funday:
    if i["internship"][0]["empid"]=="51":
        print("internship ")
    if i["fulltime"][0]["empid"]=="61":
        print("fulltime")
    if i["contract"][0]["empid"]=="71":
        print("contract")

for i in funday:
    for j in i.values():
        for k in j:
            print(k) #all the three it will print



"approach 8" #another example "googlepay" home work 1)no.of customes to whom i pay and receive 2) contact information =>one one contact has one one dictionary,
#in my camera how many contacts is there,phn contact information

#how many photos are  there,phn photos information
#personal activity


    
