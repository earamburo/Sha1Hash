__author__ = "Edwin Aramburo"


#A user_hash = b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
#B user_hash = 801cdea58224c921c21fd2b183ff28ffa910ce31
#C salted user_hash = ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
#Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e 
#this is concatenated before hashing with another word to produce the salted hash.
#D user_hash34302959e138917ce9339c0b30ec50e650ce6b40
#Hint: This hash constitutes two terms separated by one space

import hashlib
import sys
import time

#    password_list given, it is opened, and read
file = "/Applications/MAMP/htdocs/sha1_ass3_v2/src/password_list.txt"
#    this makes sure im reading the file by each line correctly
password_list = open(file,"r") 

#salted_hash = "ece4bb07f2580ed8b39aa52b7f7f918e43033ea1" 
#salted_term = "0744d60dd500c92c0d37c16174cc58d3c4bdd8e"
#salted_word = "slayer"


#def crack_salted(user_hash,salted_hash):
#    print user_hash
#
#def crack(user_hash,salted_term):
    
try_count = 0
password = "null"

user_hash = sys.argv[1]
salted_hash = sys.argv[2]

for line in password_list.readlines():

    #this will check if i am reading the correct file
#        print line.rstrip("\n")


    #transfer line in file to the test variable PREFERENCE
    test = line.rstrip("\n")
    #convert line to a hash
    hash_test = hashlib.sha1(bytes(test)).hexdigest()
#        this shows the correspondance between the word and how theyre hashed
#        print test
#        print hash_test

    #this will keep track of the time that it takes for the program to run
    start = time.time()

    #this will compare both hashes    
    if hash_test == user_hash and salted_hash == "null":
        try_count+=1
#            end_time = time.time()
        print "\nThis is your hash:"+ user_hash
        print "Password found: " + str(test) 
        print "Tried " + str(try_count) +" times in " + str(start) +"seconds"
        password = str(test)
        quit()
    #this is for the salted hash    
    elif hash_test == user_hash and salted_hash != "null":
#            end_time = time.time()
        print "\nThis is your hash:"+ user_hash
        print "Password found: " + str(test) 
        print "Tried " + str(try_count) +" times in " + str(start) +"seconds"
        password = str(test)
        break
        
    #if hashes dont match, increase count and on to the next line      
    elif hash_test != user_hash:
        try_count+=1
        print("No match, trying next password")
    elif try_count==1000000:
        print "Password not in database"

    
    
#checks if it stored the correct word   
#print password

time.sleep(3)

password_list = open(file,"r")

for line in password_list.readlines():
    
    
#    print line
    #checks if the word concatenated correctly
    new_term = password + line
    new_term = new_term.rstrip("\n")
    my_salted_hash = hashlib.sha1(bytes(new_term)).hexdigest()
#    print my_salted_hash

        
      
    
    if my_salted_hash == salted_hash:
        try_count+=1
        #end_time = time.time()
        print "\nThis is your hash:"+ salted_hash
        final_password = new_term.replace(password,"")
        print "Password found: " + final_password
        print "Tried " + str(try_count) +" times in " + str(start) +"seconds"
        quit()
        #if hashes dont match, increase count and on to the next line      
    elif my_salted_hash != salted_hash:
        try_count+=1
        print("No match, trying next password")
    elif test==null:
            print "blank line \n trying next line...."
print "Password not in database"           
    
    


    
#crack("b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3","")

#crack("f0744d60dd500c92c0d37c16174cc58d3c4bdd8e","ece4bb07f2580ed8b39aa52b7f7f918e43033ea1")

#crack_salted()