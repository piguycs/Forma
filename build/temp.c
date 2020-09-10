#include <stdio.h> 
;

 int main() { ;
 double first, second, temp ;

 printf ("Numberswapper.endo\n") ;

 printf ("Enter first number: ") ;

 scanf ("%lf", &first)    ;

 printf ("Enter second number: ") ;

 scanf ("%lf", &second)    ;
 temp = first ;
 first = second ;
 second = temp ;

 printf ("\nAfter swapping, firstNumber = %.2lf\n", first) ;

 printf ("After swapping, secondNumber = %.2lf\n", second) ;
   } 
  ;
  ;
