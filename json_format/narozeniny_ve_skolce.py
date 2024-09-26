
with open('kids.csv', 'r', encoding='utf-8') as file:
    the_kids = file.readlines()

clean_data = []
for the_kid in the_kids:
    clean_data.append(the_kid.strip("\n"))
print(clean_data)

kids_dict = {}
for kid in clean_data:
    kid_data = kid.split(',')
    name = kid_data[0].strip('""')
    classname = kid_data[1].strip('""')
    birthdate = kid_data[2].strip('""')
    birthmonth = birthdate[4:6]
    if birthmonth.startswith('0'):
        birthmonth = birthmonth[1]
    kids_dict[name] = {"classname": classname, "birthdate": birthdate, "birthmonth": int(birthmonth)}

print(kids_dict)

# sort kids based on their class
classes = {}
for kid in kids_dict:
    if kids_dict[kid]["classname"] not in classes:
        classes[kids_dict[kid]["classname"]] = {}
print(classes)
for kid in kids_dict:
    classes[kids_dict[kid]["classname"]][kid] = kids_dict[kid]["birthmonth"]
print(classes)

# sort kids based on their birth month in each class
classes_by_months = {}
for class_name in classes:
    current_class = classes_by_months[class_name] = {}
    for kid in classes[class_name]:
        month = classes[class_name][kid]
        if month not in current_class:
            current_class[month] = []
        current_class[month].append(kid)

print(classes_by_months)

classes_by_month_clean = {}


# write the result into new txt files
for class_name in classes_by_months:
    with open(f'{class_name}.txt', 'w', encoding='utf-8') as file:
        for month in sorted(classes_by_months[class_name]):
            file.write(f'{month}\n')
            for kid in classes_by_months[class_name][month]:
                file.write(f'{kid}\n')
            file.write('\n')

