from for_runner import epsilonGreedy

# 実験条件の設定
ads = [0.04, 0.04, 0.04, 0.08]
try_cnt = 10000
verbose = True

epsilon = 0.1

epG = epsilonGreedy(ads, try_cnt, verbose, epsilon)
print(epG.playout())
