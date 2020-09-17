# Forma - THIS IS THE PYTHON IMPLEMENTATION, PLEASE USE WITH CAUTION AS IT IS VERY OUTDATED AND MAY MALFUNCTION FOR NO REASON.
> For the C++ implementation please go to https://github.com/HUSKI3/FormaC

A programming language made for simplicity and ease of use. Forma is a C++ derivative with a pythonic syntax, it still maintains a few parts of the C++ language.

> This language is very very WIP

# Mini Guide/Docs
### How to compile
To compile you need to use the python script in the source code. Python 3.8 is recomended for this.
```sh
python3 compile.py b yourfile.endo
```
### Variables
In Forma there are multiple ways to store data, they are called variable types. Each of them are:
  - String - for storing words, sentences or any data that is in text format
  - Integers - for storing numbers, these can be positive, negative or zero, but no decimal places cause thats floats
  - Floats - for storing numbers with a decimal point (get it? floating point? yeah fun)
  - Char - Char can be used to store characters
  - Arrays - lists are for storing multiple variables in one place, something like [string,int,andsoforth]
  - Dictionaries - like lists but have keys to locate the data in the list, ie. {1: 'apple', 2: 'ball'}, the numbers are keys in this case, but they can also be strings.

### Built-in functions

Forma has multiple built in functions:

* `print << "Hello world!" ` - displays the data which is inserted into the function using <<
* `input >> x` - this will take input from your keyboard and store it in the variable x 
* `if (x == 0) {` - if else, works like in C++
* `import math.lib` - WIP, imports will be added soon
* `// this is a comment //` - although comments arent a function, they must be used with care, if they are not closed the proram will give an error and refuse to compile

Built-in operators in Forma:
```c++
x = 15
y = 4

//Output: x + y = 19//
print << 'x + y =' << x+y 

//Output: x - y = 11//
print << 'x - y =' << x-y)

//Output: x * y = 60//
print << 'x * y =' << x*y)

//Output: x / y = 3.75//
print 'x / y =' << x/y)
```

More functions can be imported or created.

### Installing packages

Soon

### Example of a small program
```c++
// EXAMPLE.ENDO //
using namespace std
main() {    
float n1, n2, n3
print << "Enter three numbers: "
input >> n1 >> n2 >> n3
if (n1 >= n2 && n1 >= n3)
{    
print << "Largest number: " << n1
}
if (n2 >= n1 && n2 >= n3)
{    
print << "Largest number: " << n2
}
if (n3 >= n1 && n3 >= n2)
{    
print << "Largest number: " << n3
}
else
{
print << "\nExecution finished!\n"
}
}
```


