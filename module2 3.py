my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while   zero < len(my_list):
        if my_list[zero] == 0:
                zero += 1
                continue
        if my_list[zero] == -5:
                zero += 1
                break


        print(my_list[zero])
        zero += 1




