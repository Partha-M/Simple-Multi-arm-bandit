import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
# **********************************************INITIALIZATION*****************************************************
time_step_no = 1000
total_arm = 10
total_bandit = 2000
greedy_reward = [0]*time_step_no            # initialization of total reward for different epsilon values
eps_1_reward = [0]*time_step_no
eps_01_reward = [0]*time_step_no
optimal_greedy_no = [0]*time_step_no
optimal_eps_1_no = [0]*time_step_no         # initialization of total no optimal arm pulled for different epsilon values
optimal_eps_01_no = [0]*time_step_no
for bandit_run in range(0, total_bandit):
    q_str = np.random.normal(0, 1, total_arm)  # different bandit problem selected for each run
    optimal_arm = np.argmax(q_str)
    N1, N2, N3, Q1, Q2, Q3 = np.zeros(total_arm), np.zeros(total_arm), np.zeros(total_arm), np.zeros(total_arm), np.zeros(total_arm), np.zeros(total_arm)
    for time_steps in range(0, time_step_no):
        # ******************************GREEDY ACTION SELECTION METHOD************************************
        a1_str = np.argmax(Q1)                # arm selected having highest Q value
        q = np.random.normal(q_str[a1_str], 1)
        greedy_reward[time_steps] += q        # total reward in each step (average calculated later)
        N1[a1_str] += 1                       # update of no of time action selected
        Q1[a1_str] = Q1[a1_str] + (q - Q1[a1_str]) / N1[a1_str]  # value update
        # ***********************************EPSILON GREEDY METHOD****************************************
        # EPSILON = 0.1
        rn = random.uniform(0, 1)
        if rn < .9:                                      # greedy arm selected for 0.9 times (exploitation)
            a2_str = np.argmax(Q2)
            q = np.random.normal(q_str[a2_str], 1)
            eps_1_reward[time_steps] += q
        else:
            a2_str = random.randrange(total_arm)         # random arm selection for 0.1 times (exploration)
            q = np.random.normal(q_str[a2_str], 1)
            eps_1_reward[time_steps] += q
        N2[a2_str] += 1
        Q2[a2_str] = Q2[a2_str] + (q - Q2[a2_str]) / N2[a2_str]
        # ************************************EPSILON = 0.01**************************************************
        if rn < .99:                                    # greedy arm selected for 0.99 times (exploitation)
            a3_str = np.argmax(Q3)
            q = np.random.normal(q_str[a3_str], 1)
            eps_01_reward[time_steps] += q
        else:
            a3_str = random.randrange(total_arm)        # random arm selection for 0.01 times (exploration)
            q = np.random.normal(q_str[a3_str], 1)
            eps_01_reward[time_steps] += q
        N3[a3_str] += 1
        Q3[a3_str] = Q3[a3_str] + (q - Q3[a3_str]) / N3[a3_str]
        if a1_str == optimal_arm:
            optimal_greedy_no[time_steps] += 1
        if a2_str == optimal_arm:
            optimal_eps_1_no[time_steps] += 1    # count of times optimal arm pulled
        if a3_str == optimal_arm:
            optimal_eps_01_no[time_steps] += 1
greedy_reward[:] = [x / total_bandit for x in greedy_reward]
eps_1_reward[:] = [x / total_bandit for x in eps_1_reward]                  # average reward calculation
eps_01_reward[:] = [x / total_bandit for x in eps_01_reward]
optimal_greedy_no[:] = [(x / total_bandit)*100 for x in optimal_greedy_no]
optimal_eps_1_no[:] = [(x / total_bandit)*100 for x in optimal_eps_1_no]    # percentage optimal arm calculation
optimal_eps_01_no[:] = [(x / total_bandit)*100 for x in optimal_eps_01_no]
print(greedy_reward)
print(eps_1_reward)
print(eps_01_reward)
print(optimal_greedy_no)
print(optimal_eps_1_no)
print(optimal_eps_01_no)
# ****************************************************PLOTTING*******************************************************
fig = plt.figure()
x = np.linspace(1, time_step_no+1, time_step_no)
sio.savemat('greedy_vs_e_greedy.mat',{'time_steps1':x, 'average_rewards11':greedy_reward,'optimal_action_percentage11':optimal_greedy_no,'average_rewards12':eps_1_reward,'optimal_action_percentage12':optimal_eps_1_no,'average_rewards13':eps_01_reward,'optimal_action_percentage13':optimal_eps_01_no})
plt.subplot(2, 1, 1)
plt.plot(x, greedy_reward,"g", label="epsilon=0 (greedy)")
plt.plot(x, eps_1_reward,"b", label="epsilon=0.1")
plt.plot(x, eps_01_reward,"r", label="epsilon=0.01")
plt.xlabel('Steps')
plt.ylabel('Average rewards')
plt.legend(loc="lower right")
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.xlim(-10, time_step_no)
plt.yticks((0, 0.5, 1.0, 1.5))
plt.subplot(2, 1, 2)
plt.plot(x, optimal_greedy_no,"g", label="epsilon=0 (greedy)")
plt.plot(x, optimal_eps_1_no,"b", label="epsilon=0.1")
plt.plot(x, optimal_eps_01_no,"r", label="epsilon=0.01")
plt.xlabel('Steps')
plt.ylabel('percentage optimal action')
plt.legend(loc="lower right")
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.xlim(-10, time_step_no)
plt.ylim(0, 100)
plt.show()