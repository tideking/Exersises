python 3.7
usersages of "maketrans" and "translate"
reference:  https://blog.csdn.net/jpch89/article/details/86759980

1. maketrans: 
help(str.maketrans)
maketrans(x, y=None, z=None, /)
    Return a translation table usable for str.translate().
#可以看出maketrans就是制作一张转换表，好方便转换。
a. only one argument:
            object must be a dict
           for instance,    maketrans({'a':'A','b':'B'})
b. only two arguments:
            object1 and object2 must be strings of equal length
            for instance,   maketrans("ab","AB")
c. there are three arguments:
            object1 and object2 must be strings of equal length, and in the resulting dictionary, 
                        each character in 1 will be mapped to the character at the same position in 2
            object3 must be a string , will be mapped to None in the result.
            for instance,  rr = maketrans("ab","AB","VV")
                           "abbbVVaa".translate(rr)
                           result: ABBBAA   #VV are deleted
                           
2. translate:
help(str.translate)
translate(self, table, /)
    Replace each character in the string using the given translation table.
    # 使用指定的转换表来替换字符串中的每个字符
      table
        Translation table, which must be a mapping of Unicode ordinals to
        Unicode ordinals, strings, or None.
     for instance,
     table must be a dict.
     
     string.translate(table)
     "aa".translate({'a':'A'})
     results: "AA"
