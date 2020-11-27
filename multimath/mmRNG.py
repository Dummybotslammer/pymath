#This is a math module
import time

#generates random integers:
def randInt(seed= time.time()): #parameters: outLimit[int], seed(int or float)
    if "." in str(seed): 
        seed = str(seed).split(".")
        #print(seed)
        r = seed[1] #So now seed[1] is our actual seed that we are using
        
        #redundant code:
        #if outLimit !=  0:
            #rand = rand[0:outLimit] #gives us all the characters of the string. It combines all the characters from index a, b-1
            #print("test"+ rand)

        r = int(r)**2

    else:
        r = seed**2*1405/10

    return round(r)


def rand(seed=time.time()):
    r = seed #This just fixes the problem. I dont know why tho. Just trust me.
    if "." in str(seed):
        seed = str(seed).split(".")
        
        if len(seed[0]) > len(seed[1]):
            r = seed[0] # this is the actual seed we are using

        else:
            r = seed[1]

    r = float(r)*float(str(r)[0])
    r =  r/10*len(str(r))
    #r[round(len(r)/2)] = "."
    #r = int(r)

    return r


def randBool(seed=time.time()):
    r = seed**2 
    if "." in str(seed):
        seed = str(seed).split(".")
        r = int(seed[0])**2
        print(str(r))

    r = str(r)
    r = r[0]
    r = int(r)
    print("test:" + str(r))
    if r > 5:
        return True

    else:
        return False

