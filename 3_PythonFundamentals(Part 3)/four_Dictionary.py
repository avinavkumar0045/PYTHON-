info = {
    "name" : "Avinav",
    "section":"A2",
    "age" : 21
}
print(type(info))
print(info)
print(info["name"])

print(info.keys())
print(info.values())
print(info.items())
print( info.get("name"))
info.update({"no." : 2344})#update
print(info)
