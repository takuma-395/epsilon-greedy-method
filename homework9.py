import random


# 実験条件の設定
ads = [0.04, 0.04, 0.04, 0.08]
try_cnt = 10000
verbose = True

"""
設定された確率にしたがってクリックされたかの結果を出す関数
"""


def getClick(index):
    if ads[index] > random.random():
        return 1
    else:
        return 0


"""
現在の環境をもとに、ε-Greedyでどの広告を表示するか行動を決める関数
"""


def decideAd(epsilon, show_count, click_count):
    # まだ1回も表示したことがない広告があれば選択する
    for i in range(4):
        if show_count[i] <= 0:
            return i

    # 確率epsilonで4つの広告のうちランダムな広告を選択する
    if random.random() < epsilon:
        return random.randint(0, 3)

    # 4つの広告のクリック確率（最尤推定値）を算出し、最大となった広告を選択する
    average_click = [0.0, 0.0, 0.0, 0.0]
    for i in range(4):
        average_click[i] = float(click_count[i]) / show_count[i]
    return average_click.index(max(average_click))


"""
ε-Greedyで表示する広告を決め、クリックされたかどうか結果を集計に加える関数
"""


def showAd(epsilon, show_count, click_count):
    index = decideAd(epsilon, show_count, click_count)
    show_count[index] += 1
    profit = getClick(index)
    click_count[index] += profit
    return profit


"""
指定されたepsilonパラメータでε-Greedyに従い指定された回数広告表示を繰り返す関数
"""


def playout(epsilon):
    random.shuffle(ads)
    total_click = 0
    show_count = [0, 0, 0, 0]
    click_count = [0, 0, 0, 0]
    for i in range(try_cnt):
        total_click += showAd(epsilon, show_count, click_count)
    if verbose:
        print("click probability : %s" % (ads))
        print("show count        : %s" % (show_count))
        print("click count       : %s" % (click_count))
        print("total click:%d" % (total_click,))
    return total_click


if __name__ == "__main__":
    epsilon = 0.7
    score = playout(epsilon)
