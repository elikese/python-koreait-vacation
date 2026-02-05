# 리스트를 매개변수로 받아서 평균을 계산
# [60, 80, 100]
# [(60,50,90), (80,50,40), (50,90,60)]
def calc_avg(score_list):
    avg_sum = 0
    for score_tuple in score_list:
        avg = calc_score_tuple(score_tuple)
        avg_sum += avg

    avg = avg_sum / len(score_list)
    return avg

# 매개변수로 (60,50,90) 넘어올때 평균값을 리턴하는 함수
def calc_score_tuple(scores):
    score_sum = 0
    for score in scores:
        score_sum += score

    avg = score_sum / len(scores)
    return avg


# 주민번호를 매개변수로 전달받아
# 남성 -> "남성", 여성 -> "여성" 리턴
# 남성 1,3 / 여성 2,4 / 그외 외국인
pn_ex = "991122-4122334"
def get_gender(pn):
    gender_code = pn[7]
    gender_code = int(gender_code)
    if gender_code in [1, 3]:
        return "남성"
    elif gender_code in [2, 4]:
        return "여성"
    else:
        return "외국인"

print(get_gender(pn_ex)) # "남성"