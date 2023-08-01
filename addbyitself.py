def addbyitself():
    start_num = int(input("Start number: "))
    end_num = int(input("End loop: "))    
    result = start_num
    print (result)
    for x in range(1,end_num):
        result = result + result
        print(result)

addbyitself()