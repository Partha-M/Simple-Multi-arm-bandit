% MATLAB PLOTS
clc
load('greedy_vs_e_greedy.mat')  %loadind of data files for 10 arm
load('UCB1.mat')
load('softmax_T')

%%Comparision plots of greedy and epsilon greedy
figure(1)
plot(time_steps1,average_rewards11,'g')
xlabel('steps')
ylabel('Average Rewards')
title('Average rewards for different values of \epsilon')
hold on
plot(time_steps1,average_rewards12, 'b')
plot(time_steps1,average_rewards13,'r')
xlim([-10 1000])
xticks([1 250 500 750 1000])
lgd=legend('\epsilon = 0 (greedy)','\epsilon = 0.1','\epsilon = 0.01');
lgd.FontSize = 10;
lgd.Location='south east';
hold off
figure(2)
plot(time_steps1,optimal_action_percentage11, 'g')
xlabel('steps')
ylabel('% optimal action')
title('Percentage of optimal action')
hold on
plot(time_steps1,optimal_action_percentage12, 'b')
plot(time_steps1,optimal_action_percentage13,'r')
xlim([-10 1000])
xticks([1 250 500 750 1000])
ylim([0 100])
hold off
lgd=legend('\epsilon = 0 (greedy)','\epsilon = 0.1','\epsilon = 0.01');
lgd.FontSize = 10;
lgd.Location='south east';

%%Comparision plots softmax for different T
figure(3)
plot(time_steps2,average_rewards21,'g')
xlabel('steps')
ylabel('Average Rewards')
title('Average rewards for different T')
hold on
plot(time_steps2,average_rewards22, 'b')
plot(time_steps2,average_rewards23,'r')
plot(time_steps2,average_rewards24,'c')
xlim([-10 1000])
xticks([1 250 500 750 1000])
lgd=legend('T = 0.01','T = 0.1','T = 1','T = 1.5');
lgd.FontSize = 10;
lgd.Location='south east';
hold off
figure(4)
plot(time_steps2,optimal_action_percentage21, 'g')
xlabel('steps')
ylabel('% optimal action')
title('Percentage of optimal action for different T')
hold on
plot(time_steps2,optimal_action_percentage22, 'b')
plot(time_steps2,optimal_action_percentage23,'r')
plot(time_steps2,optimal_action_percentage24,'c')
xlim([-10 1000])
xticks([1 250 500 750 1000])
hold off
lgd=legend('T = 0.01','T = 0.1','T = 1','T = 1.5');
lgd.FontSize = 10;
lgd.Location='south east';

%%Plots of UCB1 for c= 1 and c=2
figure(5)
plot(time_steps3,average_rewards31,'g')
xlabel('steps')
ylabel('Average Rewards')
title('Average rewards for UCB1 ')
hold on
plot(time_steps3,average_rewards32, 'r')
xlim([-10 1000])
xticks([1 250 500 750 1000])
lgd=legend('UCB c=1','UCB c=2');
lgd.FontSize = 10;
lgd.Location='south east';
hold off
time_steps2=linspace(1,1001,1000);
figure(6)
plot(time_steps3,optimal_action_percentage31, 'g')
xlabel('steps')
ylabel('% optimal action')
title('Percentage of optimal action for UCB1')
hold on
plot(time_steps3,optimal_action_percentage32, 'r')
xlim([-10 1000])
xticks([1 250 500 750 1000])
ylim([0 100])
hold off
lgd=legend('UCB c=1','UCB c=2');
lgd.FontSize = 10;
lgd.Location='south east';

%%Comparison plot of UCB1 epsilon greedy and softmax
figure(7)
plot(time_steps1,average_rewards12,'g')
xlabel('steps')
ylabel('Average Rewards')
title('Comparison of average rewards of \epsilon -greedy, UCB1, Softmax')
hold on
plot(time_steps3,average_rewards31, 'b')
plot(time_steps2,average_rewards22,'r')
xlim([-10 1000])
xticks([1 250 500 750 1000])
lgd=legend('\epsilon = 0.1','UCB1 c=2','Softmax T=0.1');
lgd.FontSize = 10;
lgd.Location='south east';
hold off
figure(8)
plot(time_steps1,optimal_action_percentage12, 'g')
xlabel('steps')
ylabel('% optimal action')
title('Percentage of optimal action for \epsilon -greedy, UCB1, Softmax')
hold on
plot(time_steps3,optimal_action_percentage31, 'b')
plot(time_steps2,optimal_action_percentage22,'r')
xlim([-10 1000])
xticks([1 250 500 750 1000])
ylim([0 100])
hold off
lgd=legend('\epsilon = 0.1','UCB1 c=2','Softmax T=0.1');
lgd.FontSize = 10;
lgd.Location='south east';

