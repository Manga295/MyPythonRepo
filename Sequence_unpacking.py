p=(4,5) #sequence or a tuple
x,y =p
print(x)
print(y)

data =["manga","saroja",(1,2,3)]
a,b,c =data
print(a)
print(b)
print(c)

name ,mothers_name ,(age,price,quantity)=data
print(name)
print(mothers_name)
print(age)
print(price)
print(quantity)

a="hello"

l,m,n,o,p =a
print(l)
print(m)
print(n)
print(o)
print(p)


def drop_first_last(grades):#here we are writing a function so that we want to discard the first and the last grades and calculate the average of the middle values
    first , *middle ,last =grades
    return avg(middle)

record =('manga','email_mine@mywish.com',9876544423,0989872636)
name,email_id,*phone_numbers =record
print(name)
print(email_id)
print(phone_numbers)


*trailing_quats ,current_quat =sales_record
trailing_avg =sum(trailing_quats)/len(trailing_quats)
return avg_comparision(trailing_avg,current_quat)



record =[('foo',1,2),('bar',4),('hello',,3,5)]

def do_foo(x,y):
    print(x,y)
def do_bar(s):
    print(s)

for tag ,*args in record :
    if tag == 'foo':
        do_foo(*args)
    elseif tag == 'bar':
         do_bar(tag)






































