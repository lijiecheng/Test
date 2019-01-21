#!/usr/bin/python
# coding: utf-8

sentence = "Peter Piper picked a peck of picked peppers A peck of picked peppers Pepter Piper picked If Peter Piper picked a peck of pickled"

world_dict = {}

for word in sentence.split():
    if word not in world_dict:
        world_dict[word] = 1
        print(word)
    else:
        world_dict[word] +=1
        print(word)
        print(world_dict[word])