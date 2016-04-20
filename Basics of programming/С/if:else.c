/*
Напишите функцию fizzbuzz, которая принимает в качестве параметра число limit типа int. В функции должен быть цикл, который проверяет цифры от 1 до limit, и:

если число делится на 3 без остатка, то на экран выводится слово 'Fizz'
если число делится на 5 без остатка, то на экран выводится слово 'Buzz'
если число делится и на 3, и на 5 без остатка, то на экран выводится слово 'FizzBuzz'
в противном случае на экран выводится само число
Пример вывода:

1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
*/


//Мое решение
#include <stdio.h>

void fizzbuzz(int);

int main(void)
{
    fizzbuzz(20);
    return 0;
}

// BEGIN (write your solution here)
void fizzbuzz(int limit) {
  
  int i;

  for (i = 1; i <= limit; ++i) {
    if (i%15 == 0)
      printf(" FizzBuzz ");
  
    else if (i%5 == 0)
      printf(" Buzz ");
    
    else if (i%3 == 0)
      printf(" Fizz ");
    
    else
      printf(" %d ", i);
  }
}

// END

//Решение учителя
void fizzbuzz(int limit)
{
    int i;

    for (i=1; i<=limit; ++i) {
        if (!(i % 15))
            printf("FizzBuzz");
        else if (!(i % 3))
            printf("Fizz");
        else if (!(i % 5))
            printf("Buzz");
        else
            printf("%d", i);

        printf(" ");
    }
}