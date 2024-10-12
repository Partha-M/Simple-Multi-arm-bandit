import math
import numpy as np
import matplotlib.pyplot as plt
import statistics
import scipy.io as sio
# **********************************************INITIALIZATION*****************************************************
time_step_no = 22000
total_arm = 10
total_bandit = 2000
reward = [0]*time_step_no
epsilon = 0.55
delta = 0.3
for bandit_run in range(0, total_bandit):
    q_str = np.random.normal(0, 1, total_arm)          # different bandit problem selected for each run
    N1, Q1 = np.zeros(total_arm), np.zeros(total_arm)
    S = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])            # Arms defined as set to be mutable in each elimination round
    S1 = set()
    S2 = set()                                         # empty sets for use in elimination round
    epsilon1 = epsilon/4.0
    delta1 = delta/2.0                                 # epsilon and delta values for first iteration
    run_count = 0
    while len(S) != 1:                                 # stop when one arm is left
        total_run = math.ceil(2*math.log(3.0 / delta1) / (epsilon1 ** 2))   # number of times each arm is pulled
        arm_left = len(S)
        # ************************ SAMPLING OF EACH ARM FOR VALUE ESTIMATION******************************************
        for o in range(0, arm_left):
            each_arm1 = set.pop(S)
            S1.add(each_arm1)
            for run_no in range(0, total_run):                    # we sample each arm l (as in algorithm) times
                q1 = np.random.normal(q_str[each_arm1], 1)
                reward[run_count] = reward[run_count]+q1
                N1[each_arm1] = N1[each_arm1] + 1
                Q1[each_arm1] = Q1[each_arm1] + (q1 - Q1[each_arm1]) / N1[each_arm1]   # q value for each left arm
                run_count += 1                                      # keeping track of time steps
            S2.add(Q1[each_arm1])
        med = statistics.median(S2)                                 # median calculation
        # ******************************ELIMINATION OF POOR ARM BELOW MEDIAN*******************************************
        for i1 in range(0, arm_left):
            each_arm2 = set.pop(S1)                    # each arm is popped out of the set and only arm having Q value
            if Q1[each_arm2] >= med:                   # larger than median is kept in the set
                S.add(each_arm2)
        set.clear(S1)
        set.clear(S2)
        epsilon1 = 3*epsilon1 / 4.0
        delta1 = delta1/ 2.0                           # epsilon delta update for next round

    # *************************OPTIMAL ARM PULLING FOR REST OF TIME-STEPS******************************************
    for time_step in range(run_count, time_step_no):
        c2 = set.pop(S)
        q2 = np.random.normal(q_str[c2], 1)
        reward[time_step] = reward[time_step] + q2
        S.add(c2)
    print(bandit_run)
reward[:] = [x / total_bandit for x in reward]          # average reward calculation
print(reward)
# ****************************************************PLOTTING*******************************************************
x = np.linspace(1, time_step_no+1, time_step_no)
sio.savemat('Median_Elimination.mat', {'time_steps': x, 'average_rewards4': reward})
fig = plt.figure()
plt.plot(x, reward)
plt.xlabel('Steps')
plt.ylabel('Average rewards')
plt.xlim(-100, time_step_no)
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.show()
