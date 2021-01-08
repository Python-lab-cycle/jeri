#Accept an integer n and compute n+nn+nnn.
Input  : 2 + 22 + 222 + 2222 + 22222
i=int(input("Enter a number:")
      num= (i+ ((i*10)+i)) + ((i*100)+(i*10)+i))
    print(num)
