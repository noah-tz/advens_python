
#1
#without using with statement:
cont = True
try:
    file = open('c:\hi', 'w')
except:
    print("cannot access file")
    cont = False
else:
    try:
        file.write('hello world')
    except:
        print("cannot write to file")
finally:
    if cont == True:
        file.close()
        
#2
#using the with statement
try:
    with open('c:\hi', 'w') as file:
        file.write('hello world !')
except:
    print("something failed with accessing the file")
    
#Notice that unlike the first two implementations, there is no need to call file.close()
#when using with statement. The with statement itself ensures proper acquisition and
#release of resources. An exception during the file.write() call in the first
#implementation can prevent the file from closing properly which may introduce several bugs
#in the code, i.e. many changes in files do not go into effect until the file is properly
#closed. The second approach in the above example takes care of all the exceptions but
#using the with statement makes the code compact and much more readable. Thus, with
#statement helps avoiding bugs and leaks by ensuring that a resource is properly released
#when the code using the resource is completely executed. The with statement is popularly
#used with file streams, as shown above and with Locks, sockets, subprocesses and telnets
#etc.