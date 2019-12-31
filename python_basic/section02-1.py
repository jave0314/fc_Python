# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

print() # 아무것도 없으면 줄바꿈

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcom To', end=' ')
print('the black paradise', end=' ')
print('piano notes')

print()

# format 사용 
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('Eunki', 7)) #%s : 문자, %d : 정수, %f : 실수