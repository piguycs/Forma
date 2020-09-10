# Forma - V1.0.3 Added simpler file reading
Programming language for infrustructures

```C
//Forma version 1.0.4 numberswapper.endo//
double first, second, temp 
print ("\nEnter first number: ") 
input ("%lf", &first) 
print ("Enter second number: ") 
input ("%lf", &second) 
temp = first 
first = second 
second = temp 
print ("\nAfter swapping, firstNumber = %.2lf\n", first) 
print ("After swapping, secondNumber = %.2lf\n", second) 
```

# How to build a file in Endo?
`
$ python3 compile.py b file.endo
`
# How to debug a file in Endo?
`
$ python3 compile.py d file.endo
`
