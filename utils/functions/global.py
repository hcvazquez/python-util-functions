aglobal = 0

def read_global(): 
    print(aglobal)
    
def write_global_error(): 
    try:
        aglobal += 1
        print(aglobal)
    except Exception as e:
        print(e)

def write_global(): 
    global aglobal
    aglobal += 1
    print(aglobal)
    
def write_enclosing_global():
    aglobal = 10
    def write_global():
        nonlocal aglobal
        aglobal += 1
        print(aglobal)
    write_global()
    
if __name__ == '__main__':
    read_global()
    write_global_error()
    write_global()
    write_enclosing_global()
