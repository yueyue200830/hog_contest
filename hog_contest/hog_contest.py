"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""

import datetime

PLAYER_NAME = 'Love chips and coke' # Change this line!

probility = [[0 for column in range(101)]for row in range(101)]
visited = [[0 for column in range(101)]for row in range(101)]
rolls = [[0 for column in range(101)] for row in range(101)]
num_count = [[0 for column in range(61)] for row in range(11)]


def final_strategy(score, opponent_score):
    start = datetime.datetime.now()
    get_strategy()
    end = datetime.datetime.now()
    print("time cost", end-start)

    f = open("output.txt", 'w+')
    """
    print("[", file=f)
    for i in range(101):
        print("[", end='',file=f)
        for j in range(101):
            if j == 0:
                print("{0}".format(rolls[i][j]), end='', file=f)
            else:
                print(", {0}".format(rolls[i][j]), end='', file=f)
        print("],", file=f)
    print("]", file=f)
    """
    return rolls[score][opponent_score]

def get_strategy():
    def search(s1, s2):
        # 有分数为100以上的时候
        #print("search", s1, s2)
        if s1 >= 100 and s2 >= 100:
            probility[100][100] = 1
            visited[100][100] = 1
            rolls[100][100] = 1
            return 100
        if s1 >= 100:
            probility[100][s2] = 1
            visited[100][s2] = 1
            rolls[100][s2] = 1
            return 1
        if s2 >= 100:
            probility[s1][100] = 0
            visited[s1][100] = 1
            rolls[s1][100] = 1
            return 0
        #print("not finished")
        # 如果有访问过
        if visited[s1][s2]:
            return probility[s1][s2]
        visited[s1][s2] = 1
        # 从投0-10
        for roll in range(11):
            # 投0的情况
            if roll == 0:
                new_s1 = s1 + free_bacon(s2)
                pro2 = 0
                if new_s1 >= 100:
                    pro2  = 1
                else:
                    new_s2 = s2
                    if is_swap(new_s1, new_s2):
                        new_s1, new_s2 = new_s2, new_s1
                    pro2 = get_opponent(new_s1, new_s2)
                probility[s1][s2] = pro2
                rolls[s1][s2] = roll
            else:
                new_s1 = s1 + 1
                pro = 0
                if new_s1 >= 100:
                    pro = num_count[roll][1]
                else:
                    new_s2 = s2
                    if is_swap(new_s1, new_s2):
                        new_s1, new_s2 = new_s2, new_s1
                    pro = get_opponent(new_s1, new_s2) * num_count[roll][1]
                for increasement in range(max(2,roll), roll*6+1):
                    new_s1 = s1 + increasement
                    if new_s1 >= 100:
                        pro += num_count[roll][increasement]
                    else:
                        new_s2 = s2
                        if is_swap(new_s1, new_s2):
                            new_s1, new_s2 = new_s2, new_s1
                        pro2 = get_opponent(new_s1, new_s2)
                        pro += pro2 * num_count[roll][increasement]
                    #print("pro2=", pro)
                pro /= 6 ** roll
                #print("roll=", roll, pro)
                if pro > probility[s1][s2]:
                    probility[s1][s2] = pro
                    rolls[s1][s2] = roll
        return probility[s1][s2]
    def get_opponent(s1, s2):
        roll2 = search_opponent(s1, s2)
        pro2 = 0
        if roll2 == 0:
            new_s2 = s2+free_bacon(s1)
            if new_s2 >= 100:
                pro2 = 1
            else:
                if is_swap(s1, new_s2):
                    pro2 = search(s1, new_s2)
                else:
                    pro2 = search(new_s2, s1)
            #print(pro2)
        else:
            new_s2 = s2 + 1
            if new_s2 >= 100:
                pro = num_count[roll][1]
            else:
                if is_swap(s1, new_s2):
                    pro = search(s1, new_s2) * num_count[roll2][1]
                else:
                    pro = search(new_s2, s1) * num_count[roll2][1]
            for inc in range(max(2, roll2), roll2*6+1):
                new_s2 = s2 + inc
                if new_s2 >= 100:
                    pro2 += num_count[roll2][inc]
                else:
                    if is_swap(s1, s2+inc):
                        pro2 += search(s1, s2+inc) * num_count[roll2][inc]
                    else:
                        pro2 += search(s2+inc, s1) * num_count[roll2][inc]
                #print(pro2)
            pro2 /= 6.0 ** roll2
        #print("opp",s1, s2, pro2)
        return 1-pro2
    #用于搜索对手的值
    def search_opponent(s1, s2):
        if s1 >= 100:
            return 0
        if visited[s2][s1]:
            return rolls[s2][s1]
        #对对方的投的值搜索
        search(s2, s1)
        return rolls[s2][s1]
    def counting_num():
        for j in range(1, 7):
            num_count[1][j] = 1
        for i in range(2, 11):
            for j in range(i * 6 + 1):
                num_count[i][j] = 0
                if j == 1:
                    num_count[i][j] = 6 ** i - 5 ** i
                elif j >= i:
                    for k in range(max(0, j-6), j-1):
                        if k == 1:
                            continue
                        num_count[i][j] += num_count[i-1][k]
    counting_num()
    """
    for i in range(11):
        for j in range(61):
            print(i, j, num_count[i][j])
    """
    #从后往前遍历search
    for i in range(200, 1, -1):
        for j in range(max(0, i-100), min(101,i+1)):
            if not visited[i-j][j]:
                search(i-j, j)
            print("pro=", i-j, j, rolls[i-j][j], probility[i-j][j])
    rolls[0][0] = 0

def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    result = False
    while player_score and opponent_score:
        if player_score % 10 == opponent_score % 10:
            result = True
            break
        player_score //= 10
        opponent_score //= 10
    return result

def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    points = min(score % 10, score // 10) + 1
    return points
