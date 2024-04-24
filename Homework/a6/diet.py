# Assignment 6, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def mealCal(meal: List[str], recipes: List[str], db: List[str]) -> float:
    new_rec = set()
    carbo = 4
    protein = 4
    fat = 9
    new_lst = ''
    nutrition = ''
    num_of_ing = ''
    num_ing = []
    nun =[]
    mun = []
    total: float = 0
    k = 0
    for i in recipes:
        split_i = i.split(':',1)
        sub_string = split_i[0]
        ssub_string = split_i[1]
        if sub_string in meal:
            new_lst = new_lst + ',' + ssub_string
    n = new_lst.split(',')
    n.remove('')
    for i in db:
        split_i = i.split(':',1)
        subb_string = split_i[0]
        ssubb_string = split_i[1]
        if subb_string in new_lst:
            nutrition = nutrition + ',' + ssubb_string
    nu = nutrition.split(',')
    nu.remove('')
    for i in n:
        sp = i.split('*', 1)
        sub = sp[1]
        num_ing.append(sub)
    for i in nu:
        nun.append(int(i))
    length = len(nun)
    x = length//3
    for i in num_ing:
        mun.append(int(i))
    for i in range(0,length,3):
        total += ((nun[i]*carbo)+(nun[i+1]*protein)+(nun[i+2]*fat))*mun[k]
        k += 1
    return(float(total))

mealCal(["T-Bone", "T-Bone", "Green Salad1"],["Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
"Green Salad1:Cabbage*10,Carrot*2,Pineapple*5","T-Bone:Carrot*2,Steak Meat*1"],
["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5",
"Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"])