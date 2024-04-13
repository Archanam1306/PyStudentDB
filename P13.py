#program 13
import pickle
def create():
    W=[]
    n=int(input('Enter the no.of students:'))
    f=open('Student.dat','wb')
    for i in range(n):
        d={}
        d['Roll no']=int(input('Enter the roll no:'))
        d['Name']=input('Enter the name:')
        d['Stream']=input('Enter the stream:')
        d['Total']=int(input('Enter the total:'))
        pickle.dump(d,f)
        W+=[d]
    f.close()
    return W
def toppers():
    f1=open('Student.dat','rb')
    b1={}
    c1={}
    C=0
    b=0
    try:
        while True:
            k=pickle.load(f1)
            if k['Stream']=='BIO' and k['Total']>=b:
                b=k['Total']
                b1[k['Roll no']]=k
            if k['Stream']=='CSC' and k['Total']>=C:
                C=k['Total']
                c1[k['Roll no']]=k
    except EOFError:
        print('\n\tTopper details:')
        for i in b1:
            if b1[i]['Total']==b:
                print('\t\tTopper in BIO:',b1[i])
        for j in c1:
            if c1[j]['Total']==C:
                print('\t\tTopper in CSC:',c1[j])
        f1.close()

def inc():
    f2=open('Student.dat','rb+')
    try:
        while True:
            pos=f2.tell()
            d=pickle.load(f2)
            if d['Stream']=='CSC':
                d['Total']+=3
            if d['Stream']=='BIO':
                d['Total']-=2
            f2.seek(pos)
            pickle.dump(d,f2)
    except EOFError:
        f2.close()
O=create()
ch='y'
while ch=='y':
    print('\n\t\t\tMENU')
    print('\t\t\t*******')
    print('\t\t1.Topper details')
    print('\t\t2.Increment CSC by 3 & Decrement BIO by 2')
    opt=int(input('Enter your option:'))
    if opt==1:
        toppers()
    elif opt==2:
        print('The original data:')
        inc()
        for j in O:
            print('\t\t',j)
        print('\n')
        f4=open('Student.dat','rb+')
        print('The new data:')
        try:
            while True:
                g=pickle.load(f4)
                print('\t\t',g)
        except EOFError:
            f4.close()
    ch=input('\nWould you like to continue(y/n)?')
    if ch!='y':
        print('\t\tPROGRAM TERMINATED')
        print('\t\t*************************')
        break
            

             
