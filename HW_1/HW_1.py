# аналізує та повертає загальну та середню суму заробітної плати
def total_salary(path):
    salary_total = 0
    salary_average = 0
    count = 0
    
    try: 
        with open(path,'r',encoding="utf-8") as file:
            
            for salary_line in file:
                salary_line = salary_line.strip()

                if not salary_line:
                    continue

                try:
                    emp_salary = int(salary_line.split(",")[1])
                except (ValueError, IndexError):
                    continue

                #обчислюємо загальну суму
                salary_total += emp_salary
                count += 1

    except FileNotFoundError:
        print("Файл не знайдено")

    except IsADirectoryError:
        print("Вказаний шлях є директорією, а не файлом")

    except UnicodeDecodeError:
        print("Помилка декодування файлу")
        return 0, 0

    if count > 0:
        # обчислюємо середню суму
        salary_average = salary_total / count

    totals = salary_total, salary_average
    return totals

salary_total, salary_average = total_salary("./goit-pycore-hw-04/HW_1/salary.txt")

print(f"Загальна сума заробітної плати: {salary_total}, Середня заробітна плата: {salary_average}")



