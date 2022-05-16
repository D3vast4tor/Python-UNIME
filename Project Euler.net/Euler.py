import math,random,pprint,time
'''
def read_1000_digits():
    array = []
    with open("1000_digits.txt","r") as file_handler:
        f = file_handler.read(1000)
        for n in f:
            array.append(int(n))
    file_handler.close()
    return array    
        
def largs_prod_in_series(number):
    mass = 0
    start = 0
    stop = 12
    found = False
    
    while found != True:
        prod = 1
        for i in range(start,stop+1):
            prod *= number[i]
            if prod >= mass:
                mass = prod
        if stop == len(number)-1:
            return mass
        start += 1
        stop += 1

def Fibonacci_succession(nth_number):
    Succession = list()
    for i in range(0,nth_number):
        if i < 1:
            Succession.append(1)
        else:
            Succession.append( Succession[i-1] + Succession[i-2] )
    return Succession


def is_prime(n):
    for j in range(2,int(math.sqrt(n)) + 1):
        if (n % j) == 0:
            return False
    return True

def sum_prime(limit):
    sum = 0
    for i in range(2,limit):
        if is_prime(i) == True:
            sum += i
        else:
            pass
    return sum

def Large_sum():
    summ = 0
    summ = int(summ)
    with open('Large_sum.txt','r',newline = '\n') as file_handler:
        data = file_handler.read().split('\r\n')
        
        file_handler.close()
    for i in data:
        summ += int(i)   
    return summ

def is_palindrome(n):
    n = str(n)
    n = list(n)
    mid = int( n.__len__() / 2 )
    if(n[0:mid] == n[:mid-1:-1]):
        return True
    else:
        return False

def Largest_palindrome_product():
    Products = list()
    maxx = 0
    for i in range(100,1000):
        for j in range(100,1000):
            prod = 1
            prod = i*j
            if(is_palindrome(prod) == True):
                Products.append(prod)
    for products in Products:
        if(products >= maxx):
            maxx = products
    return maxx  

def is_pythagorean_triplet(a,b,c):
    if( a < b and b < c and math.sqrt(math.pow(a,2)+math.pow(b,2)) == c):
        return True
    else:
        return False
    
def special_pythagorean_triplet():
    for a in range(0,1001):
        for b in range(0,1001):
            for c in range(0,1001):
                if(is_pythagorean_triplet(a,b,c) == True and (a+b+c) == 1000):
                    print(a) # a = 200
                    print(b) # b = 375
                    print(c) # c = 425
                    return a*b*c # 31875000

def is_even(n):
    if (n % 2) == 0:
        return True
        return False
    else:
        return False
sequences = dict()

def Collaz_sequence(n):
    collection = list()
    while(n != 1):
        collection.append(n)
        if is_even(n) == True:
            n = int(n / 2)
        elif is_even(n) == False:
            n = int(( 3 * n ) + 1)
        else:
            break
    collection.append(1)
    return collection
    
def longest_collaz_sequence(Limit_starting_number):
    max = 0
    Db = dict()
    for i in range(1,Limit_starting_number + 1):
        temp = Collaz_sequence(i)
        sequences[i] = temp
        print(i)
        if len(temp) > max:
            max = len(temp)
            Db[max] = i
    return Db

def _2power_digit_sum(exponent):
    sum = 0
    res = 2**exponent
    for num in str(res):
        sum += int(num)
    return sum

class Numletcount:
    _numtolet1 = {
                1:"one",2:"two",3:"three",4:"four",
                5:"five",6:"six",7:"seven",8:"eight",
                9:"nine",11:"eleven",10:"ten",
                12:"twelve",13:"thirteen",14:"fourteen",
                15:"fifteen",16:"sixteen",17:"seventeen",
                18:"eighteen",19:"nineteen"
                }
    _numtolet2 = {
                2:"twenty",3:"thirty",4:"forty",
                5:"fifty",6:"sixty",7:"seventy",
                8:"eighty",9:"ninety"
    }
    def count_digits(self,n):
        return len(str(n))
    
    def convert2digits(self,n):
        out_num = ''
        n = str(n)
        count = 1
        for char in n:
            if int(char) == 0:
                pass
            elif count == 1 and int(n) >= 20:
                out_num += self._numtolet2[int(char)]
                count += 1
            elif count == 1 and int(n)<20:
                    out_num += self._numtolet1[int(n)]
                    break
            else:
                if int(char) == 0:
                    pass
                else:
                    out_num += self._numtolet1[int(char)]
                    count += 1
        return out_num
                
    
    def convert3digits(self,n):
        n = str(n)
        out_num = ''
        if int(n[0]) != 0:
            out_num+=self._numtolet1[int(n[0])]
            out_num+='hundredand'
            n = n[1:]
            out_num += self.convert2digits(self,n)
        return out_num
            
    def convert4digits(self,n):
        n = str(n)
        out_num = ''
        out_num += (self._numtolet1[int(n[0])] + 'thousand')
        n = n[1:]
        out_num += self.convert3digits(self,int(n))
        return out_num
        
    def convert_to_letter(self,n):
        if self.count_digits(self,n) == 1:
            return self._numtolet1[n]
        elif self.count_digits(self,n) == 2 and int(n) < 20:
            return self._numtolet1[int(n)]
        elif self.count_digits(self,n) == 2 and int(n)>= 20:
            return self.convert2digits(self,n)
        elif self.count_digits(self,n) == 3:
            return self.convert3digits(self,n)    
        elif self.count_digits(self,n) == 4:
            return self.convert4digits(self,n)
            
#####################################################################
#   IMPORTANT :                                                     #
#       In class Numletcount there's an error of +16 to the sum of  #
#       the number between 1 and 999(one and ninehundredninetynine) #
#                                                                   #
#####################################################################

def sort_increasing(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j
        while i > 0 and a[i-1] > key:
            a[i] = a[i-1]
            i -= 1
        a[i] = key 
    return a

def sort_decreasing(a):
    for j in range(len(a),1,-1):
        for j in range(1,len(a)):
            key = a[j]
        i = j
        while i > 0 and a[i-1] < key:
            if a[i] == 0:
                a[i] = a[len(a)-1]
                a[len(a)-1] = 0
            else:
                a[i] = a[i-1]
                i -= 1
        a[i] = key 
    return a
'''
triangulars = 1
def nt_triangularnum(n):
    global triangulars
    if n == 1:
        pass
    else:
        triangulars += int(n)
###################################     
#   Ci mette troppo tempo         #
#   non so se si può ottimizzare  #
#   una volta triangulars era una #
#   lista....l'inferno.           #
###################################   
def triang_num_with_at_least_n_divisors(n):
    global triangulars
    count = 1
    nt_triangularnum(1)
    while(True):
        count_div = 0
        temp = triangulars
        for i in range(1,temp + 1):
            if (temp % i) == 0:
                count_div += 1
        if(count_div >= n):
            return triangulars
        else:
            print(count_div)
            count += 1
            nt_triangularnum(count)
        
        
        
def main():
    print(triang_num_with_at_least_n_divisors(500))
        
    
   
if __name__ == '__main__':
    main()