import random


class epsilonGreedy:
    def __init__(self, ads, try_cnt, verbose, epsilon):
        self.ads = ads
        self.try_cnt = try_cnt
        self.verbose = verbose
        self.epsilon = epsilon

    # 設定された確率にしたがってクリックされたかの結果を出す関数
    def getClick(self, index):
        if self.ads[index] > random.random():
            return 1
        else:
            return 0

    # 現在の環境をもとに、ε-Greedyでどの広告を表示するか行動を決める関数
    def decideAd(self, epsilon, show_count, click_count):
        # まだ1回も表示していない広告があれば表示する
        for i in range(4):
            if show_count[i] <= 0:
                return i
        # 確率epsilonで4つの広告のうちランダムな広告を選択する
        if random.random() < epsilon:
            return random.randint(0, 3)
        # 4つの広告のクリック確率（最尤推定値）を算出し、最大となった広告を選択する
        self.average_click = [0.0, 0.0, 0.0, 0.0]
        for i in range(4):
            self.average_click[i] = float(self.click_count[i]) / \
                                          self.show_count[i]
        return self.average_click.index(max(self.average_click))

    # ε-Greedyで表示する広告を決め、クリックされたかどうか結果を集計に加える関数
    def showAd(self, epsilon, show_count, click_count):
        index = self.decideAd(epsilon, show_count, click_count)
        self.show_count[index] += 1
        profit = self.getClick(index)
        self.click_count[index] += profit
        return profit

    # 指定されたepsilonパラメータでε-Greedyに従い指定された回数広告表示を繰り返す関数
    def playout(self):
        random.shuffle(ads)
        self.total_click = 0
        self.show_count = [0, 0, 0, 0]
        self.click_count = [0, 0, 0, 0]
        for i in range(self.try_cnt):
            self.total_click += self.showAd(self.epsilon, self.show_count,
                                            self.click_count)
        return self.total_click, self.ads, self.show_count, self.click_count


# 実験を実行する関数を定義する


# 実験条件の設定
ads = [0.04, 0.04, 0.04, 0.08]
try_cnt = 10000
verbose = True

epsilon = 0.1

epG = epsilonGreedy(ads, try_cnt, verbose, epsilon)
print(epG.playout())
