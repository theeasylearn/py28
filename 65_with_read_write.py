#as exercise implement exception handling and also write perfect number into perfect.txt file 
import prime_number as p 
read_file = "numbers.txt"
prime_file = "prime.txt" #this file will store only prime numbers 
with open(read_file,'r') as numbers:
    with open(prime_file,'w') as writer:
        for line in numbers:
            num = int(line)
            result = p.isPrime(num)
            if result == True:
                #write this number into file
                writer.write(str(num) + "\n")
print('task complete')