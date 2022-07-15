import random as rnd


def createDict():
    listDict=list()
    dictionary=dict()
    for i in range (10):
        dictionary={
            "id": i,
            "age": rnd.randint(1,100)
        }
        listDict.append(dictionary)
    return listDict


def printOrder(listDict):
    listAge=list()
    listDictOrder=list()
    for i in listDict:
        listAge.append(i.get('age'))
    listAge.sort(reverse=True)
    for i in listAge:
        listDictOrder.append(next(x for x in listDict if x["age"] == i))
    print("persona mas vieja : ", listDictOrder[0])
    print("persona mas joven : ", listDictOrder[9])
  
printOrder(createDict())
