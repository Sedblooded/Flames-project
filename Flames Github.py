import time

popped={'F':'You are not friends','L':'You guys are not lovers','A':'You guys are not affectionate','M':'You guys are not Married','E':'You guys are not Enemies','S':'You guys are not siblings'}
result={'F':'You are friends','L':'You guys are lovers','A':'You guys are affectionate','M':'You guys are Married','E':'You guys are Enemies','S':'You guys are siblings'}

B=str(input('enter the guys name='))
G=str(input('enter the girls name='))

boy=list(B.lower())         #making it all lower case so that we can cancel the common letters
girl=list(G.lower())

while ' ' in boy:                                   #removing all the empty spaces
    boy.pop(boy.index(' '))
while ' ' in girl:
    girl.pop(girl.index(' '))

for i in boy:                                     #removing all the matched characters
    if i in girl:
        boy.pop(boy.index(i))
        girl.pop(girl.index(i))
trans=boy + girl                                  #i dont really mean it, it is just fun and games
num=len(trans)   #list of unmatched characters     
time.sleep(1)                             #added time for that extra bit of suspense
flames=['F','L','A','M','E','S']
a=0                               #stores the index of the previously removed character
for love in range(6,1,-1):
    s=num%love-1                 #index no of the element to be removed
    print(popped[flames[(s+a)%love]])    #element which is getting popped, just to see which is getting popped
    flames.pop((s+a)%love)
    a=s                              #this is so that after restart the loop and land on a value,and u move to the next 'a'th element
    time.sleep(2)                    #cooldown time, to build suspence       
print(result[flames[0]])
