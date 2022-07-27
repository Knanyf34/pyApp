from teacher import Teacher

if __name__ == '__main__':
    jafar = Teacher('Jafa', 'Jafari', 123)
    print(jafar.get_emp_code())

    # jafar.emp_code = 445
    jafar.set_emp_code(11)
    print(jafar.get_emp_code())

    jafar.__emp_code = 23
    jafar.__emp_code = 56
