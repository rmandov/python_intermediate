def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "armando", "lastname": "velasco"}

    super_list = [
        {"firstname": "armando", "lastname": "velasco"},
        {"firstname": "elsa", "lastname": "bueso"},
        {"firstname": "lalo", "lastname": "onganiza"},
        {"firstname": "elva", "lastname": "ginon"},
        {"firstname": "susana", "lastname": "horia"},
        {"firstname": "benito", "lastname": "camelo"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2], 
        "floating_nums": [1.1, 4.5, 6.3, 5.6, 3.2]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])

if __name__ == '__main__':
    run()