import hashlib 
import string

def someFunc():
    for i0 in list(range(10)) + list(string.ascii_lowercase + string.ascii_uppercase):
        for i1 in list(range(10)) + list(string.ascii_lowercase + string.ascii_uppercase):
            for i2 in list(range(10)) + list(string.ascii_lowercase + string.ascii_uppercase):
                for i3 in list(range(10)) + list(string.ascii_lowercase + string.ascii_uppercase):
                    #code = str(9-i0)+ str(9-i1)+ str(9-i2)+ "726300631"
                    code = str(i0)+str(i1)+"yW"+str(i2)+str(i3)+"3w" 
                    #print(code)
                    result = hashlib.md5(code.encode())
                    shash = result.hexdigest()
                    if(shash.startswith("002a8a8b23d03e70")):
                    #if(shash.startswith("351635d71448baca")):
                        print(code)
                        print(shash)
                        return
someFunc()
                                                
