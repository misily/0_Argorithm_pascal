def pascal(a, b): # a 몇번째 줄인지 , b 몇번째 원소인지
    if a <= 0 or b <= 0 :
        # print(a, b)
        return 0
    if a == 1 or a == b:
        # print(a, b)
        return 1
    else : 
        # print(f'{a}번줄, {b}번 원소')
        return pascal(a-1, b-1) + pascal(a-1, b)


def pascal_list(n): # 파스칼삼각형의 n번 줄을 만드는 함수
    p_list = []
    for i in range(n):
        p_list.append(pascal(n, i + 1)) 
    return p_list


print(pascal_list(8))