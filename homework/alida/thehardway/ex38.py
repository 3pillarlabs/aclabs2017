ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not ten things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There are %d items now" % len(stuff))

print ("There we go", stuff)

print("Let's do some things with stuff.")

print (stuff[1]) #prints second item
print (stuff[-1]) #whoa. prints last item. fancy
print (stuff.pop()) #prints last item and pops it out of the list?
print (' '.join(stuff)) #whoa.
print ('#'. join(stuff[3:5])) #joins items on positions 4 and 5
