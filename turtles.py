"""turtlesdetails = ["cheese", "green", "CHEESE", "eseehc", "ESEEHC"]

turtlesdetails[2] = turtlesdetails[3]

print(turtlesdetails)"""

meloveturtle = ("cheese", "green", "CHEESE", "eseehc", "ESEEHC")

print(meloveturtle[1])

"""meloveturtle[1] = "ello"

print(meloveturtle)"""

for i in meloveturtle:
    print(i)


print(meloveturtle[2:4])

print(meloveturtle[1:])

myturtleinfo = ("turtle", "today", ["my backyard", "the glass house yk"])

print(myturtleinfo[2][0])

myturtleinfo[2][1] = "the smol pool in da backyard"

print(myturtleinfo)

name,dob,adress = myturtleinfo

print(name)

diswasmyturtleinfo = list(myturtleinfo)

print(diswasmyturtleinfo)