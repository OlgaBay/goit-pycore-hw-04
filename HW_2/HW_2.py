# читає файл та повертає список словників з інформацією про кожного кота
def get_cats_info(path):
    cats_list = []

    try: 
        with open(path,'r',encoding="utf-8") as file:

            for cat_line in file:
                cat_line = cat_line.strip()

                if not cat_line:
                    continue

                try:
                    cat_id, name, age = cat_line.split(",")
                    cat_id = cat_id.strip()
                    name = name.strip()
                    age = age.strip()

                    if not cat_id or not name or not age:
                        continue

                    if not age.isdigit():
                        continue

                except ValueError:
                    continue

                cats_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_list.append(cats_dict)

    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    
    except IsADirectoryError:
        print("Вказаний шлях є директорією, а не файлом")
        return []
    
    except UnicodeDecodeError:
        print("Помилка декодування файлу")
        return []

    return cats_list

cats_info = get_cats_info("./HW_2/cat_info.txt")

print(cats_info)
