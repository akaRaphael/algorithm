# 파이썬의 간단한 파일 입출력 

# 일반적으로 파일 입출력의 과정은 다음과 같다. 
# - EOF(End of File)를 만날 때까지 반복적으로 한줄씩 파일을 읽어간다. 
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line: 
        break
    raw = line.split()
    print(raw)
f.close()

# - 그러나 파이썬에서는 with-as 키워드를 사용하여 다음과 같이 구현할 수 있다. 
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))

# - 우선 with-as 키워드를 사용하기에 파일을 close()하지 않아도 된다.
# - 더불어 file.readlines()가 EOF 까지만 파일을 자동으로 읽기 때문에, break도 필요하지 않다.