my_dict = {"Employee":
               {"Dave":
                    {"ID": "001", "Salary": "2000", "Designation": "Team Lead"},
                "Ava":
                    {"ID": "002", "Salary": "1000", "Designation": "Team Jerk"}}
           }

print(my_dict["Employee"]["Dave"]["ID"])
print(type(my_dict))
