sample_dict = {"class_a": {"student": {"name": "misha",
                                       "marks": {"math": 90, "history": 85}}}}
print(sample_dict)
print(sample_dict["class_a"]["student"]["name"])
print(sample_dict["class_a"]["student"]["marks"]["history"])
sample_dict["class_a"]["student1"] = {"name": "Max",
                                      "marks": {"math": 80, "history": 100}}
print(sample_dict)
sample_dict.update({"class_b": {"student": {"name": "artem",
                                            "marks": {"math": 20, "history": 50}},
                                "student1": {"name": "Santa",
                                             "marks": {"math": 40, "history": 86}}}})
print(sample_dict)
sample_dict["class_a"]["student"]["marks"].update({"physics": 39})
sample_dict["class_a"]["student1"]["marks"].update({"physics": 74})
sample_dict["class_b"]["student"]["marks"].update({"physics": 100})
sample_dict["class_b"]["student1"]["marks"].update({"physics": 80})
print(sample_dict)
med_a_stud = round((sample_dict["class_a"]["student"]["marks"]["math"] +
                    sample_dict["class_a"]["student"]["marks"]["history"] +
                    sample_dict["class_a"]["student"]["marks"]["physics"]) / len(sample_dict["class_a"]["student"]["marks"]), 2)
# средняя оценка ученика
med_a_stud1 = round((sample_dict["class_a"]["student1"]["marks"]["math"] +
                     sample_dict["class_a"]["student1"]["marks"]["history"] +
                     sample_dict["class_a"]["student1"]["marks"]["physics"]) / len(sample_dict["class_a"]["student1"]["marks"]), 2)

med_b_stud = round((sample_dict["class_b"]["student"]["marks"]["math"] +
                    sample_dict["class_b"]["student"]["marks"]["history"] +
                    sample_dict["class_b"]["student"]["marks"]["physics"]) / len(sample_dict["class_b"]["student"]["marks"]), 2)

med_b_stud1 = round((sample_dict["class_b"]["student1"]["marks"]["math"] +
                     sample_dict["class_b"]["student1"]["marks"]["history"] +
                     sample_dict["class_b"]["student1"]["marks"]["physics"]) / len(sample_dict["class_b"]["student1"]["marks"]), 2)
print('Лучшим студентом является:',
      max({med_a_stud: 'Misha',
          med_a_stud1: 'Max',
          med_b_stud: 'Artem',
          med_b_stud1: 'Santa'}.items()))
medium_grades_a = round((med_a_stud + med_a_stud1)/len(sample_dict["class_a"]), 2)
medium_grades_b = round((med_b_stud + med_b_stud1)/len(sample_dict["class_b"]), 2)
medium_classes = {medium_grades_a: 'class_a', medium_grades_b: 'class_b'}
medium_grades_classes = round(((medium_grades_a + medium_grades_b) / 2), 2)
print('Средний балл классов:', medium_grades_classes)
print('Лучшим классом является:', max(medium_classes.items()))
