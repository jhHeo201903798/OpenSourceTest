s = input().lower()#대소문자 구분을 없애기 위해 문자열을 입력과 동시에 모두 소문자로 변환
maxind = 0#가장 긴 회문이 들어 있는 인덱스 초기화
def circular(s):#회문인지를 판별하는 함수
    isCir = []#모든 글자가 대칭이어야 회문이기에 글자마다 일치하는지 true,false를 저장해줄 리스트
    for i in range(int(len(s)/2)):#문장의 절반을 기준으로
        if s[i] == s[len(s) - (i+1)]:#만약 글자가 대칭이라면
            isCir.append(True)#리스트에 True를 넣어줌
        else:
            isCir.append(False)
    if isCir.count(False) == 0:#만약 리스트의 모든 요소가 True라면
        return True
    else:#리스트에 False가 하나라도 있다면
        return False
			
cir = []#모든 회문의 부분자열 저장
maxcir = []#가장 긴 회문의 부분자열
for i in range(len(s)):#회문의 부분자열을 cir 리스트에 append
	for j in range(i,len(s)):
		if circular(s[i:j+1]):
			cir.append(s[i:j+1])
			
for i in range(1,len(cir)):#가장 긴 회문의 부분자열의 길이 구하기
	if len(cir[i]) > len(cir[maxind]):
		maxind = i

for i in range(len(cir)):#가장 긴 회문의 부분자열을 maxcir에 append
	if len(cir[i]) == len(cir[maxind]):
		if maxcir.count(cir[i]) == 0:#중복요소 제거
			maxcir.append(cir[i])

maxcir.sort()#사전순으로 정렬
print(' '.join(maxcir))
	


