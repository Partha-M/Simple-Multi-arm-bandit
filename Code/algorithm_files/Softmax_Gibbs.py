import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
# **********************************************INITIALIZATION*****************************************************
time_step_no = 1000
total_arm = 10
total_bandit = 2000
T1_reward = [0] * time_step_no
optimal_T1_no = [0] * time_step_no
T2_reward = [0] * time_step_no
optimal_T2_no = [0] * time_step_no   # initialization of total reward and total no optimal arm pulled for different T
T3_reward = [0] * time_step_no
optimal_T3_no = [0] * time_step_no
T4_reward = [0] * time_step_no
optimal_T4_no = [0] * time_step_no
T1 = 0.01
T2 = 0.1
T3 = 1.0                             # different temperature (T) values
T4 = 1.5
arm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for bandit_run in range(0, total_bandit):
    q_str = np.random.normal(0, 1, total_arm)    # different bandit problem selected for each run
    optimal_arm = np.argmax(q_str)
    Q1, Q2, Q3, Q4 = np.zeros(total_arm), np.zeros(total_arm), np.zeros(10), np.zeros(total_arm)
    N1, N2, N3, N4 = np.zeros(total_arm), np.zeros(total_arm), np.zeros(10), np.zeros(total_arm)
    P_dist1, P_dist2, P_dist3, P_dist4 = np.ones(total_arm) * 0.1, np.ones(total_arm) * 0.1, np.ones(total_arm) * 0.1, np.ones(total_arm) * 0.1
    for time_steps in range(0, time_step_no):
        # ************************************** Soft-max for T = 0.01*************************************
        S1 = 0.0
        for i1 in range(0, total_arm):
            S1 += math.exp(Q1[i1] / T1)
        for i2 in range(0, total_arm):
            P_dist1[i2] = math.exp(Q1[i2]/T1) / S1   # Soft-max distribution calculation for T=0.01
        c1 = np.random.choice(arm, 1, p=P_dist1)     # sampling from soft-max distribution
        q1 = np.random.normal(q_str[c1], 1)
        T1_reward[time_steps] += q1
        N1[c1] += 1
        Q1[c1] = Q1[c1] + (q1 - Q1[c1]) / N1[c1]     # value update for T=0.01
        if c1 == optimal_arm:
            optimal_T1_no[time_steps] += 1
        # **************************************** Soft-max for T = 0.1*************************************
        S2 = 0.0
        for i3 in range(0, total_arm):
            S2 += math.exp(Q2[i3] / T2)
        for i4 in range(0, total_arm):
            P_dist2[i4] = math.exp(Q2[i4] / T2) / S2   # Soft-max distribution calculation for T=0.1
        c2 = np.random.choice(arm, 1, p=P_dist2)       # sampling from soft-max distribution
        q2 = np.random.normal(q_str[c2], 1)
        T2_reward[time_steps] += q2
        N2[c2] += 1
        Q2[c2] = Q2[c2] + (q2 - Q2[c2]) / N2[c2]       # value update for T=0.1
        if c2 == optimal_arm:
            optimal_T2_no[time_steps] += 1
        # ****************************************** Soft-max for T = 1*************************************
        S3 = 0.0
        for i5 in range(0, total_arm):
            S3 += math.exp(Q3[i5] / T3)
        for i6 in range(0, total_arm):
            P_dist3[i6] = math.exp(Q3[i6] / T3) / S3   # Soft-max distribution calculation for T=1.0
        c3 = np.random.choice(arm, 1, p=P_dist3)       # sampling from soft-max distribution
        q3 = np.random.normal(q_str[c3], 1)
        T3_reward[time_steps] += q3
        N3[c3] += 1
        Q3[c3] = Q3[c3] + (q3 - Q3[c3]) / N3[c3]       # value update for T=1.0
        if c3 == optimal_arm:
            optimal_T3_no[time_steps] += 1
        # ************************************** Soft-max for T = 1.5****************************************
        S4 = 0.0
        for i7 in range(0, total_arm):
            S4 += math.exp(Q4[i7] / T4)
        for i8 in range(0, total_arm):
            P_dist4[i8] = math.exp(Q4[i8] / T4) / S4  # Soft-max distribution calculation for T=1.5
        c4 = np.random.choice(arm, 1, p=P_dist4)      # sampling from soft-max distribution
        q4 = np.random.normal(q_str[c4], 1)
        T4_reward[time_steps] += q4
        N4[c4] += 1
        Q4[c4] = Q4[c4] + (q4 - Q4[c4]) / N4[c4]      # value update for T=1.5
        if c4 == optimal_arm:
            optimal_T4_no[time_steps] += 1
T1_reward[:] = [x / total_bandit for x in T1_reward]
T2_reward[:] = [x / total_bandit for x in T2_reward]                 # average reward calculation
T3_reward[:] = [x / total_bandit for x in T3_reward]
T4_reward[:] = [x / total_bandit for x in T4_reward]
optimal_T1_no[:] = [(x / total_bandit)*100 for x in optimal_T1_no]
optimal_T2_no[:] = [(x / total_bandit)*100 for x in optimal_T2_no]
optimal_T3_no[:] = [(x / total_bandit)*100 for x in optimal_T3_no]   # percentage optimal arm calculation
optimal_T4_no[:] = [(x / total_bandit)*100 for x in optimal_T4_no]
print(T1_reward)
print(optimal_T1_no)
print(T2_reward)
print(optimal_T2_no)
print(T3_reward)
print(optimal_T3_no)
print(T4_reward)
print(optimal_T4_no)
# ****************************************************PLOTTING*******************************************************
fig = plt.figure()
x = np.linspace(1, time_step_no+1, time_step_no)
sio.savemat('softmax_T.mat',{'time_steps2':x, 'average_rewards21':T1_reward,'optimal_action_percentage21':optimal_T1_no, 'average_rewards22':T2_reward,'optimal_action_percentage22':optimal_T2_no, 'average_rewards23':T3_reward,'optimal_action_percentage23':optimal_T3_no, 'average_rewards24':T4_reward,'optimal_action_percentage24':optimal_T4_no,})
plt.subplot(2, 1, 1)
plt.plot(x, T1_reward,"g", label="T = 0.01")
plt.plot(x, T2_reward,"r", label="T = 0.1")
plt.plot(x, T3_reward,"b", label="T = 1")
plt.plot(x, T4_reward,"c", label="T = 1.5")
plt.xlabel('Steps')
plt.ylabel('Average rewards')
plt.legend(loc="lower right")
plt.xlim(-10, time_step_no)
plt.ylim(0, 1.6)
plt.yticks((0, 0.5, 1.0, 1.5))
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.subplot(2, 1, 2)
plt.plot(x, optimal_T1_no,"g", label="T = 0.01")
plt.plot(x, optimal_T2_no,"r", label="T = 0.1")
plt.plot(x, optimal_T3_no,"b", label="T = 1")
plt.plot(x, optimal_T4_no,"c", label="T = 1.5")
plt.xlabel('Steps')
plt.ylabel('percentage optimal action')
plt.legend(loc="lower right")
plt.xlim(-10, time_step_no)
plt.ylim(0, 100)
plt.xticks((1, 0.25*time_step_no, 0.5*time_step_no, 0.75*time_step_no, time_step_no))
plt.show()
