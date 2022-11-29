# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:36:39 2022

@author: nelso

Date: 11/21/2022
Title: intro to dictionaries
"""

"""
Quick Reference D = {} creates an empty dictionary
D = {key1:value1, ...} creates a non-empty dictionary
D[key] returns the value thats mapped to by key. (What if there’s no such key?)
D[key] = newvalue maps newvalue to key. Overwrites any previous value. Remember - newvalue can be any valid Python data structure.
del D[key] deletes the mapping with that key from D.
len(D) returns the number of entries (mappings) in D.
x in D, x not in D checks whether the key x is in the dictionary D.
D.keys() - returns a list of all the keys in the dictionary.
D.values() - returns a list of all the values in the dictionary.
"""

"""
set up a dicionary
have a function to add to the dictionary 
have a function to remove an item from the dictionary
have a function that selects all items in the dictionary with a particular property
have a function that selects all items whose have some property
"""




class dictFcns(object):
    '''class for working with dictionaries
        this assume we have a dictionary with which to work'''
    def __init__ (self, name):
        self._name = name
        
    def printDictName(self):
        print('dict name = ', self._name)

    def getDictionary(self, dictName):
        self._dict = dictName
        print(dictName)
    
    def printDictionary(self, dictName):
        
        keys = dictName.keys()
        for k in keys:
            print(dictName[k])
        print(self._dict)

    def printValue(self, keys):
        for key in keys:
            print('\n key = ',key ,self._dict[key])
            #print(self._dict[key])
        print()


    #crn = '90502', title = 'basket101', description = 'weaving', numberofstudents= 41
    def addItem(self, crn, title, description, numberofstudents):
        self._dict[crn]=[crn, title, description, numberofstudents]
        #self._dict.update(crn [title, description, numberofstudents])
    
    def removeItem(self,key):
        del self._dict[key]
        
        
    def Avgnumbstuds(self):
        tempsum= 0
        keys = self._dict.keys()  #keys = self._name.keys()
        for key in keys:
            x = self._dict[key]
            print(x[2])
            tempsum+=x[2]
        n= len(x)
        return tempsum/n
            

  

if __name__ == '__name__':
      #%%   
    classesDict = {'76341': ['math115', 'statistics', 23], '37445': ['math115','statistics',30],
                   '77445':['math160','integral calculus',14]}
    
    
    myClasses = dictFcns("Dj.J classes taught")
    myClasses.printDictName()
    #myClasses = dictFcns.getDictionary()
    
    myClasses.getDictionary(classesDict)
    
    print("\nprint the dictionary")
    myClasses.printDictionary(classesDict)
    
    print("\n values fro two crns")
    myClasses.printValue(['77445','37445'])# myClasses.printValue('77445')
    
    print('\n add crn 90251')
    myClasses.addItem('90251','basket 101', 'fundementals of weaving', 51)
    #dictItem = {'90251': 'basket 101', 'fundementals of weaving', 51}
    
    print('print the new dictionary')
    myClasses.printDictionary(classesDict)
    
    print('\n remove a crn')
    myClasses.removeItem('90251')
    
    print('\n print the result dictionary after removing 90251')
    myClasses.printDictionary(classesDict)

    print('\nfind the average number of students in each class')
    avgnostudents = myClasses.Avgnumbstuds()
    print(f"avergae num students = {avgnostudents: .2f}")














