%Plotting comparison Median Elimination for different epsilon and delta
%run each python file 10000 time steps
clc
load('greedy_vs_e_greedy.mat')  %loadind of data files for 10 arm
load('UCB1.mat')
load('softmax_T')
load('Median_Elimination.mat')


figure(1)
plot(time_steps1,average_rewards12,'b')
xlabel('steps')
ylabel('Average Rewards')
title('Comparison of average rewards of \epsilon -greedy, UCB1, Softmax and MEA')
hold on
plot(time_steps3,average_rewards31, 'g')
plot(time_steps2,average_rewards22,'r')
plot(time_steps4,average_rewards4,'color',[0.7 0.5 0.9])
xlim([-10 10000])
xticks([1 2500 5000 7500 10000])
lgd=legend('\epsilon = 0.1','UCB1 c=2','Softmax T=0.1', 'Median Elimination (\epsilon =0.8, \delta =0.3)');
lgd.FontSize = 10;
lgd.Location='south east';
hold off
