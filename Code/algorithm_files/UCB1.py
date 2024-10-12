import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
# **********************************************INITIALIZATION*****************************************************
time_step_no = 1000
total_arm = 10
total_bandit = 2000
UCB_reward1 = [0]*time_step_no         # initialization of total reward for different c values
optimal_UCB_no1 = [0]*time_step_no
UCB_reward2 = [0]*time_step_no         # initialization of total no optimal arm pulled for different c values
optimal_UCB_no2 = [0]*time_step_no
c1 = 1.0
c2 = 2.0
for bandit_run in range(0, total_bandit):
    q_str = np.random.normal(0, 1, total_arm)   # different bandit problem selected for each run
    optimal_arm = np.argmax(q_str)
    N1, Q1, CB1 = np.zeros(total_arm), np.zeros(total_arm), np.zeros(total_arm)
    N2, Q2, CB2 = np.zeros(total_arm), np.zeros(total_arm), np.zeros(total_arm)
    for time_steps in range(0, time_step_no):
        # ***************************************UCB1 for c=1*****************************************************
        for arm in range(0, total_arm):
            if N1[arm] == 0:
                CB1[arm] = 99999999       # for N(a)=0, a is maximizing action
            else:
                CB1[arm] = c1 * math.sqrt(math.log(time_steps) / N1[arm])
        a1_str = np.argmax(Q1 + CB1)
        q1 = np.random.normal(q_str[a1_str], 1)
        UCB_reward1[time_steps] += q1     # total reward in each step (average calculated later)
        N1[a1_str] += 1                   # update of no of time action selected
        Q1[a1_str] = Q1[a1_str] + (q1 - Q1[a1_str]) / N1[a1_str]
        if a1_str == optimal_arm:
            optimal_UCB_no1[time_steps] += 1  # count of times optimal arm pulled
        # ***************************************UCB1 for c=2*****************************************************
        for arm in range(0, total_arm):
            if N2[arm] == 0:
                CB2[arm] = 99999999      # for N(a)=0, a is maximizing action
            else:
                CB2[arm] = c2 * math.sqrt(math.log(time_steps) / N2[arm])
        a2_str = np.argmax(Q2 + CB2)
        q2 = np.random.normal(q_str[a2_str], 1)
        UCB_reward2[time_steps] += q2    # total reward in each step (average calculated later)
        N2[a2_str] += 1                  # update of no of time action selected
        Q2[a2_str] = Q2[a2_str] + (q2 - Q2[a2_str]) / N2[a2_str]
        if a2_str == optimal_arm:
            optimal_UCB_no2[time_steps] += 1  # count of times optimal arm pulled
UCB_reward1[:] = [x / total_bandit for x in UCB_reward1]                 # average reward calculation
UCB_reward2[:] = [x / total_bandit for x in UCB_reward2]
optimal_UCB_no1[:] = [(x / total_bandit)*100 for x in optimal_UCB_no1]
optimal_UCB_no2[:] = [(x / total_bandit)*100 for x in optimal_UCB_no2]   # percentage optimal arm calculation
print(UCB_reward1)
print(optimal_UCB_no1)
print(UCB_reward1)
print(optimal_UCB_no1)
# ****************************************************PLOTTING*******************************************************
fig = plt.figure()
x = np.linspace(1, time_step_no+1, time_step_no)
sio.savemat('UCB1.mat', {'time_steps3': x, 'average_rewards31': UCB_reward1, 'optimal_action_percentage31': optimal_UCB_no1, 'average_rewards32':UCB_reward2,'optimal_action_percentage32':optimal_UCB_no2})
plt.subplot(2, 1, 1)
plt.plot(x, UCB_reward1, "b", label="UCB  c=1")
plt.plot(x, UCB_reward2, "r", label="UCB  c=2")
plt.xlabel('Steps')
plt.ylabel('Average rewards')
plt.legend(loc="lower right")
plt.xlim(-10, time_step_no)
plt.ylim(-0.1, 1.6)
plt.yticks((0, 0.5, 1.0, 1.5))
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.subplot(2, 1, 2)
plt.plot(x, optimal_UCB_no1, "b", label="UCB c=1")
plt.plot(x, optimal_UCB_no2, "r", label="UCB c=2")
plt.xlabel('Steps')
plt.ylabel('percentage optimal action')
plt.legend(loc="lower right")
plt.xlim(-10, time_step_no)
plt.ylim(0, 100)
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.show()