## Prime Number Checker
This is a Python function that checks if a given number is prime or not. The function utilizes a combination of two different algorithms for prime checking: the Sieve of Eratosthenes and the Trial Division approach.

## How It Works
### Sieve of Eratosthenes
The Sieve of Eratosthenes is an ancient algorithm used to find all prime numbers up to a specified integer. It works by iteratively marking the multiples of each prime number, starting from 2. This process efficiently identifies all prime numbers within a given range.

### Trial Division Approach
The Trial Division approach is a simple algorithm that checks whether a number is divisible by any integer other than 1 and itself. It iterates through all possible divisors up to the square root of the number being checked, making it an effective method for determining primality.

## Usage
To use the prime number checker function, simply pass the number you want to check as an argument to the function. It will return a boolean value indicating whether the number is prime or not.

```python
from main import is_prime
number = 23
result = is_prime(number)
print(f"{number} is prime: {result}")
```

## Contributing
If you'd like to contribute to this project or have suggestions for improvement, please feel free to submit a pull request or open an issue.

Contact
If you have any questions or feedback, feel free to reach out to me at [abusisiaya@gmai.com].
