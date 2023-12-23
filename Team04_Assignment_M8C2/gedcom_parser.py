from datetime import date

from prettytable import PrettyTable
class Individual:
    def __init__(self, id, name, gender, birthday, age, alive, deathday, child, spouse):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.age = age
        self.alive = alive
        self.deathday = deathday
        self.child = child
        self.spouse = spouse

class Family:
    def __init__(self, id, married, divorced, husbandId, husbandName, wifeId, wifeName, childrenId):
        self.id = id
        self.married = married
        self.divorced = divorced
        self.husbandId = husbandId
        self.husbandName = husbandName
        self.wifeId = wifeId
        self.wifeName = wifeName
        self.childrenId = childrenId

month_dict = {"JAN": '01',
            "FEB": '02',
            "MAR": "03",
            "APR": "04",
            "MAY": "05",
            "JUN": "06",
            "JUL": "07",
            "AUG": "08",
            "SEP": "09",
            "OCT": "10",
            "NOV": "11",
            "DEC": "12"}

def list_to_string(s):
    child = ""
    flag = True
    for i in s:
        if(flag == True):
            child = child+'\''+i+'\''
            flag = False
        else:
            child = child+ ','+'\''+i+'\''

        
    child = '{'+child+'}'
    return child
    
def individual_parser(file_name):
    file = open(file_name, encoding='utf-8-sig')
    flag = False
    individual = []
    id = ''
    date_flag = ' '
    for line in file:
        elements = line.split()
        if(elements[0] == '0'):
            if(len(elements) > 2):
                if(elements[2] == 'INDI'):                
                    id = elements[1].replace('@', "")
                    individual_obj = Individual(id,"","","",0,True,"NA",[],[])                
                    individual.append(individual_obj)
                # print(individual)
        if(elements[0] == '1'):
            if(elements[1] == 'NAME'):
                previous_name = individual.pop()
                previous_name.name = ' '.join(elements[2:])
                individual.append(previous_name)
            if(elements[1] == 'SEX'):
                previous_sex = individual.pop()
                previous_sex.gender = elements[2]
                individual.append(previous_sex)
            if(elements[1] == 'BIRT'):
                # print(date_flag)
                date_flag = date_flag.replace(date_flag,"BIRT") 
            if(elements[1] == 'DEAT'):
                date_flag = date_flag.replace(date_flag,"DEAT")
            if(elements[1] == 'FAMS'):
                previous_spouse = individual.pop()
                previous_spouse.spouse.append(elements[2].replace('@',""))
                individual.append(previous_spouse)
            if(elements[1] == 'FAMC'):
                previous_child = individual.pop()
                previous_child.child.append(elements[2].replace('@',""))
                individual.append(previous_child)
        if(elements[0] == '2'):
            if(elements[1] == 'DATE'):
                # print(date_flag)
                if(date_flag == 'BIRT'):
                    previous_birthdate = individual.pop()
                    previous_birthdate.birthday = elements[4]+'/'+month_dict[elements[3]]+'/'+elements[2]
                    previous_birthdate.alive = True
                    birthdate = date(int(elements[4]),int(month_dict[elements[3]]),int(elements[2]))
                    today = date.today()
                    previous_birthdate.age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                    individual.append(previous_birthdate)
                if(date_flag == 'DEAT'):
                    previous_deathdate = individual.pop()
                    previous_deathdate.deathday = elements[4]+'/'+month_dict[elements[3]]+'/'+elements[2]
                    previous_deathdate.alive = False
                    deathdate = date(int(elements[4]),int(month_dict[elements[3]]),int(elements[2]))
                    today = date.today()
                    previous_deathdate.age = deathdate.year - birthdate.year - ((deathdate.month, deathdate.day) < (birthdate.month, birthdate.day))
                    individual.append(previous_deathdate)
    file.close()
    return individual

def family_parser(file_name):
    file = open(file_name, encoding='utf-8-sig')
    flag = False
    family = []
    id = ''
    date_flag = "PARTH"
    for line in file:
        elements = line.split()
        if(elements[0] == '0'):
            if(len(elements) > 2):
                if(elements[2] == 'FAM'):                
                    id = elements[1].replace('@', "")
                    family_obj = Family(id,"NA","NA","","","","",[])                
                    family.append(family_obj)
                    # print()
                # print(individual)
        if(elements[0] == '1'):
            # print(elements[1])
            if(elements[1] == 'HUSB'):
                # print(elements[1])
                previous_husb = family.pop()
                previous_husb.husbandId = elements[2].replace('@',"")
                family.append(previous_husb)
                # print(previous_husb)
            if(elements[1] == 'WIFE'):
                previous_wife = family.pop()
                previous_wife.wifeId = elements[2].replace('@',"")
                family.append(previous_wife)
            if(elements[1] == 'MARR'):
                # print(date_flag)
                date_flag = date_flag.replace(date_flag,"MARR")
                # print(date_flag) 
            if(elements[1] == 'DIV'):
                date_flag = date_flag.replace(date_flag,"DIV")
            if(elements[1] == 'CHIL'):
                previous_chil = family.pop()
                previous_chil.childrenId.append(elements[2].replace('@',""))
                family.append(previous_chil)
        if(elements[0] == '2'):
            if(elements[1] == 'DATE'):
                # print(date_flag)
                if(date_flag == 'MARR'):
                    previous_marrieddate = family.pop()
                    previous_marrieddate.married = elements[4]+'/'+month_dict[elements[3]]+'/'+elements[2]
                    # previous_marrieddate.alive = True
                    # marrieddate = date(int(elements[4]),int(month_dict[elements[3]]),int(elements[2]))
                    # today = date.today()
                    # previous_marrieddate.age = today.year - marrieddate.year - ((today.month, today.day) < (marrieddate.month, marrieddate.day))
                    family.append(previous_marrieddate)
                if(date_flag == 'DIV'):
                    # print(date_flag)
                    previous_divdate = family.pop()
                    previous_divdate.divorced = elements[4]+'/'+month_dict[elements[3]]+'/'+elements[2]
                    # previous_deathdate.alive = False
                    # divdate = date(int(elements[4]),int(month_dict[elements[3]]),int(elements[2]))
                    # today = date.today()
                    # previous_deathdate.age = deathdate.year - birthdate.year - ((deathdate.month, deathdate.day) < (birthdate.month, birthdate.day))
                    family.append(previous_divdate)
    file.close()
    
    return family

                    
ind = individual_parser("gedcom_test.ged")
fam = family_parser("gedcom_test.ged")
indi_list = []
fam_list = []


for i in range(len(ind)):
    # print(ind[i].name)
    
    if(len(ind[i].child) == 0):
        ind[i].child = 'NA'
    else:
        ind[i].child = list_to_string(ind[i].child)


    if(len(ind[i].spouse) == 0):
        ind[i].spouse = 'NA'
    else:
        ind[i].spouse = list_to_string(ind[i].spouse)
    indi_list.append([ind[i].id, ind[i].name, ind[i].gender, ind[i].birthday, ind[i].age, ind[i].alive, ind[i].deathday, ind[i].child, ind[i].spouse])

for i in range(len(fam)):
    # print(ind[i].name)
    
    if(len(fam[i].childrenId) == 0):
        fam[i].childrenId = 'NA'
    else:
        fam[i].childrenId = list_to_string(fam[i].childrenId)

for i in range(len(fam)):
    for j in range(len(ind)):
        if(fam[i].husbandId == ind[j].id):
            fam[i].husbandName = ind[j].name
        if(fam[i].wifeId == ind[j].id):
            fam[i].wifeName = ind[j].name

for i in range(len(fam)):
    fam_list.append([fam[i].id,fam[i].married,fam[i].divorced, fam[i].husbandId, fam[i].husbandName, fam[i].wifeId, fam[i].wifeName, fam[i].childrenId])

# print(fam_list)
individual_table = PrettyTable(['ID','Name','Gender','Birthday','Age', 'Alive', 'Death', 'Child', 'Spouse'])
family_table = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])

for i in range(len(indi_list)):
    individual_table.add_row(indi_list[i])

for j in range(len(fam_list)):
    family_table.add_row(fam_list[j])
#
print("Individual")
print(individual_table)
print(" ")
print("Family")
print(family_table)

                

