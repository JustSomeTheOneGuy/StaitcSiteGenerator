sentence = "This is a sentence `by the way` eheheheh"
delimiter = "`"


if type(sentence.count(delimiter)/2) == int:
    print("yep, that works")
print("nope")
print(type(sentence.count(delimiter)/2))
print(type(2/2))
print(type(3/2))


new_sentence = sentence.split("`")
print(new_sentence)