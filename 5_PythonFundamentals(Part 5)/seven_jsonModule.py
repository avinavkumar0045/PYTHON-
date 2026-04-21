import json

py_obj  = {
    "name" : "Sharadha",
    "isTeacher" : None

}
json_str = json.loads(py_obj)

print(type(json_str), json_str)


