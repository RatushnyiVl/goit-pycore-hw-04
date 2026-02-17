def get_cats_info(path:str) -> list:
    """
    Handle cats raw data and return readable information
    
    :param path: Path to txt file
    :type path: str
    :return: List of Cats with their ID, Name and Age
    :rtype: list
    """
    result = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                id, name, age = line.split(',')
                info = {'id': id,
                        'name': name, 
                        'age': age.rstrip('\n')}
                result.append(info)
        return result
    except FileNotFoundError:
        return print('No such a file was found. Double check the path to a file')
    except UnicodeDecodeError:
        return print('Encoding error or file damaged')
    except Exception as e:
        return print(e, "Given file is not structured correctly")

cats_info = get_cats_info('text/cats.txt')
print(cats_info)
