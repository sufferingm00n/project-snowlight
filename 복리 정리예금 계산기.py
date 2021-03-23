M=int(input('원금을입력하세요:'))

r=int(input('금리를 입력하세요:'))

y=int(input('만기 시간을 입력하세요:'))

print('원리금:',M*(1+r/100)**y)
