def total_salary(path:str)->tuple:
    """
    Analyze information about monthly salaries of developers
    
    :param path: Path to txt file
    :type path: str
    :return: Total amout of all salaries and avarage salary
    :rtype: tuple
    """
    total_money = 0
    num_of_people = 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                _, salary = line.split(',')
                num_of_people += 1
                total_money += int(salary)           
        return total_money, total_money / num_of_people
    
    except FileNotFoundError:
        return print('No such a file was found. Double check the path to a file')
    except UnicodeDecodeError:
        return print('Encoding error or file damaged.')
    except Exception as e:
        return print(e, "Given file is not structured correctly")

total, average = total_salary("text/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
