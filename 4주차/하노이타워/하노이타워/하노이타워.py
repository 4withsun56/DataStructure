#P-1 하노이 타워 알고리즘을 구현하시오.
import time

def hanoi_tower(n,fr,tmp,to):
    if(n==1):
        print("원판 1:%s-->%s"%(fr,to))

    else:
        hanoi_tower(n-1,fr,to,tmp)
        print("원판 %d: %s-->%s"%(n,fr,to))
        hanoi_tower(n-1,tmp,fr,to)
    hanoi_tower.counter+=1



n=int(input("하노이 타워의 높이를 입력하세요:"))

hanoi_tower.counter=0

start_time=time.time()
hanoi_tower(n,'A','B','C')
finish_time=time.time()-start_time

print("n=%d  걸린시간:%f    함수호출횟수:%d" %(n,finish_time,hanoi_tower.counter))

