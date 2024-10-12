%Plotting comparison Median Elimination for different epsilon and delta
%rename  the data file name in python for different epsilon delta
clc
load('Median_Elimination1.mat')
avg_r1=average_rewards4;
load('Median_Elimination2.mat')
avg_r2=average_rewards4;
load('Median_Elimination3.mat')
avg_r3=average_rewards4;

figure(1)
plot(time_steps4,avg_r1, 'b')
hold on
plot(time_steps4,avg_r2, 'g')
plot(time_steps4,avg_r4,'r')
xlim([-10 22000])
xticks([1 5000 10000 15000 20000])
xlabel('steps')
ylabel('Average Rewards')
title('Average rewards comparison Median Elimination for different \epsilon and \delta  ')
lgd=legend('\epsilon =0.55, \delta =0.30','\epsilon =0.65, \delta =0.25',  '\epsilon =0.80, \delta =0.30');
lgd.FontSize = 10;
lgd.Location='south east';
hold off