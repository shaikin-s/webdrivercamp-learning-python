Exercise

0. What function would you use to print the type of an object?
print(type(object))

1. How do you get the variable identifier (which is the memory address in the CPython implementation)?
id(variable)

2. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = 100
No

3. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = 89
Yes

4. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = a
Yes

5. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = a + 1
No

6. What does this print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
True

7. What does this print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
True

8. What does this print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
True

9. What does this print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
False

10. What does this  print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
True

11. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
False

12. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
True

13. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
False

14. What does this print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
[1, 2, 3, 4]

15. What does this print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
[1, 2, 3]

16. What does this print?
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
1

17. What does this print?
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
[1, 2, 3, 4]

18. What does this print?
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
[1, 2, 3]

19. What would these lines print?
>>> dict_ = {"WebDriver": "Camp"}
>>> dict_copy = dict_
print(dict_ == dict_copy)
True
print(dict_ is dict_copy)
True
>>> dict_copy = dict_.copy()
print(dict_ == dict_copy)
True
print(dict_ is dict_copy)
False

19. What would these lines print?
>>> list_ = [1, 2, 3, 4, 5]
>>> list_copy = list_
print(list_ == list_copy)
True
print(list_ is list_copy)
True
>>> list_copy = list_.copy()
print(list_ == list_copy)
True
print(list_ is list_copy)
False

20. Tuple or not?
a = ()
Yes

21. Tuple or not?
a = (1, 2)
Yes

22. Tuple or not?
a = (1)
Yes

23. Tuple or not?
a = (1, )
b = 1,
Yes
Yes

24. What does this script print?
a = (1)
b = (1)
a is b
True

25. What does this script print?
a = (1, 2)
b = (1, 2)
a is b
False

26. What does this print?
a = ()
b = ()
a is b
True

27. What does this print?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
13992679593242425256757755543789

28. What does this print?
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
139926795932424
