%Plotting comparison of UCB1, Espilon Greedy softmax and Median Elimination
% rename data file as the name of the loaded file 
clc
load('greedy_vs_e_greedy_1000.mat') % loadind data files for 1000 arm
load('softmax_T_1000')
load('UCB1_1000.mat')
load('Median_Elimination_1000.mat')
%%Comparision plots of greedy and epsilon greedy
figure(1)
plot(time_steps1,average_rewards11, 'b')
hold on
plot(time_steps1,average_rewards12,'r')
plot(time_steps,average_rewards13,'g')
xlim([-10 700000])
xticks([0 140000 280000 420000 560000 700000])
xlabel('Steps')
ylabel('Average Rewards')
title('Average rewards comparison of \epsilon -greedy for different \epsilon ')
lgd=legend('\epsilon = 0.0 (greedy)','\epsilon = 0.1', '\epsilon = 0.01');
lgd.FontSize = 10;
lgd.Location='south east';
hold off

%%Plots for softmax 
figure(2)
plot(time_steps2,average_rewards21, 'r')
xlim([-10 700000])
xticks([0 140000 280000 420000 560000 700000])
xlabel('Steps')
ylabel('Average Rewards')
title('Average rewards comparison of \epsilon -greedy for different \epsilon ')
lgd=legend('Softmax (T = 0.1)');
lgd.FontSize = 10;
lgd.Location='south east';

%%Plots of UCB1 for c= 2
figure(3)
plot(time_steps3,average_rewards32, 'b')
xlim([-10 700000])
xticks([0 140000 280000 420000 560000 700000])
xlabel('Steps')
ylabel('Average Rewards')
title('Average rewards comparison of \epsilon -greedy for different \epsilon ')
lgd=legend('UCB c=2');
lgd.FontSize = 10;
lgd.Location='south east';

%%Comparison plot of UCB1 epsilon greedy MEA and softmax
figure(4)
plot(time_steps1,average_rewards12, 'b')
hold on
plot(time_steps2,average_rewards21,'r')
plot(time_steps3,average_rewards32,'g')
plot(time_steps,average_rewards4,'color',[0.7 0.5 0.9])
xlim([-10 700000])
xticks([0 140000 280000 420000 560000 700000])
xlabel('Steps')
ylabel('Average Rewards')
title('Average rewards comparison of \epsilon -greedy,UCB1, Softmax and Median elimination  ')
lgd=legend('\epsilon -greedy (\epsilon = 0.1)','Softmax (T = 0.1)','UCB c=2','Median Elimination (\epsilon =0.8, \delta =0.3)');
lgd.FontSize = 10;
lgd.Location='south east';
hold off