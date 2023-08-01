def fibonacci():
    start_num = int(input("Start number: "))
    second_num = int(input("Second number; "))
    end_num = int(input("End loop number: "))

    for x in range(1, end_num):
        result = start_num+second_num
        print(start_num," + ",second_num, " = ", result)
        start_num,second_num=second_num,result

fibonacci()