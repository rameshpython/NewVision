# print("hii how are you \rwhat\'s going on")
# print("hello hii wat\ry")


name = "Sri sri Venkata siva shankara varaprasad"

#checking 'name' variable has the 'siva' word

if "siva" in name:
    splitted_name = name.split()
    lenth_value = len(splitted_name)
    print(splitted_name)
    # add_r_to_name="\r"
    # new_string = splitted_name[0]+splitted_name[1]+splitted_name[2]+splitted_name[3]+add_r_to_name+splitted_name[4]+" "+splitted_name[5]
    #
    # print(new_string)

    print(splitted_name[lenth_value-2]+"\U0001F923"+splitted_name[lenth_value-1])





#Expected output/Requirement : name should come "Shankara Varaprasad"