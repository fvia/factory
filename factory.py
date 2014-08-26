#!/usr/bin/env python

import readline

class World:
   def __init__(self):
        pass   
 

class Employee:
   def __init__(self,x,y,id,name):
       self.x = x
       self.y = y
       self.id = id
       self.name = name
       self.targetx = x
       self.targety = y  
       self.item = None  
 
   def goto(self,x,y):
       self.targetx = x
       self.targety = y  
   
   def move(self):
       """
        
       """
       if self.x > self.targetx:
            self.x = self.x - 1 
            return
       if self.x < self.targetx:
            self.x = self.x + 1 
            return
       if self.y > self.targety:
            self.y = self.y - 1 
            return
       if self.y < self.targety:
            self.y = self.y + 1 
            return

   def pick(self,x,y ):
       pass
   
   def drop(self,x,y):
       pass    
  
   def step(self):
       self.move()
       
   def __str__(self):
       return "({},{}) {}-{}".format( self.x,self.y,self.id,self.name )   

class Coil:
   def __init__(self,x,y,id,name):
       self.x = x
       self.y = y
       self.id = id
       self.name = name 
       self.piked_by = None


   def step(self):
       pass 

   def __str__(self):
       return "({},{}) {}-{}".format( self.x,self.y,self.id,self.name )   
#####################################
if __name__ == '__main__':

    TheItems= [] 


    luque =  Employee(10,10,101,"luque" )
    luque.goto(12,12)
    TheItems.append(luque)

    paco =  Employee(10,12,101,"paco" )
    paco.goto(15,15)
    TheItems.append(paco)

    b52 = Coil(20,10,552, "B52" )
    TheItems.append(b52)

    for x in range(1000):
        for i in TheItems:
            i.step()
            print(i) 
        str_command = input("step {}:".format(x))
        if str_command == 'quit':
            break   
        str_command = str_command + " 0 0 0 0" 
        quien, que, x, y, resta  =  str_command.split(" ",4)
        print("quien:{}  que:{} x:{} y:{}".format(quien,que,x,y))
        # TODO  clear \n from input        
        quienIter = filter( lambda K: K.name == quien  , TheItems )
        objQuien = next( quienIter, None  )        
        print("objQuien", objQuien )
        if objQuien:
            if que in ["pick", "drop", "goto"]:
                getattr(objQuien,que)(int(x),int(y))
            else:
                print ("unknow method,  pick drop goto ")  
        else:
            print("unknow employee")      
