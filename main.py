import re
import csv


def read_file():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def correct_names(lst):
    res = [' '.join(people[:3]).split(' ')[:3] + people[3:7] for people in lst]
    return res


def correct_numbers(new_lst):
    pattern = re.compile(r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})")
    substitution = r"+7(\2)\3-\4-\5"
    result = [[pattern.sub(substitution, row) for row in lst] for lst in new_lst]
    return result


def add_to_numbers(second_lst):
    pattern = re.compile(r"\(?доб.\s(\d{4})\)?")
    substitution = r"доб.\1"
    result2 = [[pattern.sub(substitution, row) for row in lst] for lst in second_lst]
    return result2


def merging_identical(corrected_lst):
    final_lst = []
    for initials in range(len(corrected_lst)):
        for doubles in range(len(corrected_lst)):
            if corrected_lst[initials][0] == corrected_lst[doubles][0]:
                corrected_lst[initials] = [i or j for i, j in zip(corrected_lst[initials], corrected_lst[doubles])]
        if corrected_lst[initials] not in final_lst:
            final_lst.append(corrected_lst[initials])
    return final_lst


def write_file(lst):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        file = datawriter.writerows(lst)
    return file


if __name__ == '__main__':
    list1 = read_file()
    list2 = correct_names(list1)
    list3 = correct_numbers(list2)
    list4 = add_to_numbers(list3)
    list5 = merging_identical(list4)
    write_file(list5)

