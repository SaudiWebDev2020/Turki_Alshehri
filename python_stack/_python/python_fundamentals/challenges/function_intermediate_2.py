x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]





z[0]['x'] = 15
print(z)
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30
print(z)

#--------------------------------------------------------


def iterateDictionary(li):
    for x in range(0,len(li), 1):
        print("first_name -", li[x]['first_name'] + ", last name -", li[x]['last_name'])


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'} ]
iterateDictionary(students) 


#--------------------------------------------------------


def iterateDictionary2(key, li):
    for x in range(0,len(li), 1):
        print(li[x][key])


iterateDictionary2('first_name', students)


#--------------------------------------------------------



def printInfo(dict):
    for x in dict:
        print(len(dict[x]),x)
        for y in dict[x]:
            print(y)





dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)