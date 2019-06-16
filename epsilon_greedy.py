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

    def result(self, try_num):
        results = []
        for i in range(try_num):
            results.append(self.playout()[0])
        all_click = 0
        for result in results:
            all_click += result
        # print(all_click)
        return all_click / len(results)


# 実験条件の設定
ads = [0.04, 0.04, 0.04, 0.08]
try_cnt = 10000
verbose = True

fin_results = []
exp_count = 500

epsilons = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for epsilon in epsilons:
    epG = epsilonGreedy(ads, try_cnt, verbose, epsilon)
    fin_results.append(epG.result(exp_count))
print(fin_results)
