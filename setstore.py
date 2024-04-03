# my_copy_set = set()
# print(my_copy_set)
# my_copy_set.add(789654)
# my_copy_set.add({789654,4574985,340928409}) # TypeError: unhashable type: 'set'
# print(my_copy_set)

# print("""
#      remove(elem)
#          Remove element elem from the set. Raises KeyError if elem is not contained in the set.
#        """)
# print(my_copy_set)
# my_copy_set.remove(789654)
# print(my_copy_set)
# my_copy_set.remove(789654) #KeyError: 789654

# print("""
#      discard(elem)
#          Remove element elem from the set if it is present.
#        """)
# print(my_copy_set)
# my_copy_set.discard(789654)
# print(my_copy_set)
# my_copy_set.discard(789654)
# print(my_copy_set)

# print("""
# #     pop()
# #         Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
# #       """)
# my_copy_set.add(789654)
# my_copy_set.add(11111)
# my_copy_set.add(2222)
# print(my_copy_set)
# my_copy_set.pop()
# print(my_copy_set)

# print("""
#      clear()
#      Remove all elements from the set.
#        """)
# print(my_copy_set)
# my_copy_set.clear()
# print(my_copy_set)


# set_val = set() # empty set 
# set_val1 = {1,1,1,1,1,1,1,1,"test",frozenset(["val1","vall2"])} # set([1,2,3,4])

# set_val1 = {1,2}
# set_val2= {2,3}

# print(set_val1.union(set_val2))
# print(set_val1.intersection(set_val2))
# print(set_val1.difference(set_val2))
# set_val1.update(set_val2)
# set_val1.difference_update(set_val2)
# set_val1.intersection_update(set_val2)
# set_val1.symmetric_difference_update(set_val2)
# print(set_val1)

# print(set_val.isdisjoint(set_val1))
# print(set_val.issubset(set_val1))
# print(set_val1.issuperset(set_val))
 
# print(set_val)
# set_val.add(1)
# print(set_val)

# print(set_val)
# set_val.remove(1)
# print(set_val)


# print(set_val)
# set_val.discard(11)
# print(set_val)

# set_val.add(2)
# print(set_val)
# set_val.pop()
# print(set_val)

my_set = { 1,2,3,43,4,5,5,6,7,7,7,8,8,8,8,"gaurav","Pune",
             ("dbda,hpcsa","diot","dac"),frozenset({"dbda,hpcsa","diot","dac"})
         }

print( len(my_set))
my_subset1={100,200,300}
my_subset2={1,2,3,300}
print(my_set)




#print("x in s --Test x for membership in s.")
#print(100 in my_subset1)
#print(frozenset({"dbda,hpcsa","diot","dac"}) in my_set)
#print(("dbda,hpcsa","diot","dac") in my_set)
#print("dbda" in my_set)
#print("Pune" in my_set)

#print("x not in s --Test x for non-membership in s.")
#print(100 not in my_subset1)


#print("isdisjoint(other) --Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.")
#print(my_set.isdisjoint(my_subset1))
#print(my_set.isdisjoint(my_subset2))

#############################################################

print(my_subset1)
print(my_subset2)
print(my_set)
print(my_subset1.issubset(my_set))
print(my_subset2.issubset(my_set))

#############################################################

print(""" 
       issuperset(other)
         set >= other
         Test whether every element in other is in the set.

         set > other
         Test whether the set is a proper superset of other, that is, set >= other and set != other.
       """)

print(my_set.issuperset(my_subset1))
print(my_set.issuperset(my_subset2))

##############################################################









