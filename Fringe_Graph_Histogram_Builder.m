% x = rand(10000,1)*10000;
% hist(x)
% hold
% figure
% h = hist(x);
% loglog(h)

Emb_Full = importdata('Embeddedness_Full_Network.txt');
Emb_NFF = importdata('Embeddedness_Non-Fringe_Fringe.txt');
Emb_NFNF = importdata('Embeddedness_Non-Fringe_Non-Fringe.txt');
Deg_Full = importdata('Degree_Full_Network.txt');
Deg_Fringe = importdata('Degree_Fringe.txt');
Deg_NFF = importdata('Degree_Non-Fringe.txt');
Deg_NFNF = importdata('Degree_Non-Fringe_to_Non-Fringe.txt');

a = Emb_Full(:,1) ./ Emb_Full(:,2);
b = Emb_Full(:,1) ./ Emb_Full(:,3);
Norm_Emb_Full = [a;b];
a = Emb_NFF(:,1) ./ Emb_NFF(:,2);
b = Emb_NFF(:,1) ./ Emb_NFF(:,3);
Norm_Emb_NFF = [a;b];
a = Emb_NFNF(:,1) ./ Emb_NFNF(:,2);
b = Emb_NFNF(:,1) ./ Emb_NFNF(:,3);
Norm_Emb_NFNF = [a;b];

bin1 = max(Emb_Full(:,1))+1;
bin2 = max(Emb_NFF(:,1))+1;
bin3 = max(Emb_NFNF(:,1))+1;
bin4 = max(Deg_Full)+1;
bin5 = max(Deg_Fringe)+1;
bin6 = max(Deg_NFF)+1;
bin7 = max(Deg_NFNF)+1;

% bin8 = max(Norm_Emb_Full)+1;
% bin9 = max(Norm_Emb_NFF)+1;
% bin10 = max(Norm_Emb_NFNF)+1;

[Emb_Hist_Full,Emb_Hist_Full_Cent] = hist(Emb_Full(:,1),bin1);
[Emb_Hist_NFF,Emb_Hist_NFF_Cent] = hist(Emb_NFF(:,1),bin2);
[Emb_Hist_NFNF,Emb_Hist_NFNF_Cent] = hist(Emb_NFNF(:,1),bin3);
[Deg_Hist_Full,Deg_Hist_Full_Cent] = hist(Deg_Full(:,1),bin4);
[Deg_Hist_Fringe,Deg_Hist_Fringe_Cent] = hist(Deg_Fringe(:,1),bin5);
[Deg_Hist_NFF,Deg_Hist_NFF_Cent] = hist(Deg_NFF(:,1),bin6);
[Deg_Hist_NFNF,Deg_Hist_NFNF_Cent] = hist(Deg_NFNF(:,1),bin7);

% [Norm_Emb_Hist_Full,Norm_Emb_Hist_Full_Cent] = hist(Norm_Emb_Full,bin8);
% [Norm_Emb_Hist_NFF,Norm_Emb_Hist_NFF_Cent] = hist(Norm_Emb_NFF,bin9);
% [Norm_Emb_Hist_NFNF,Norm_Emb_Hist_NFNF_Cent] = hist(Norm_Emb_NFNF,bin10);
[Norm_Emb_Hist_Full,Norm_Emb_Hist_Full_Cent] = hist(Norm_Emb_Full,100);
[Norm_Emb_Hist_NFF,Norm_Emb_Hist_NFF_Cent] = hist(Norm_Emb_NFF,100);
[Norm_Emb_Hist_NFNF,Norm_Emb_Hist_NFNF_Cent] = hist(Norm_Emb_NFNF,100);

hold
subplot(2,1,1)
semilogy(Emb_Hist_Full_Cent,Emb_Hist_Full,'o')
title('Embeddedness - Full Network')
xlabel('Embeddedness')
ylabel('Edges')
subplot(2,1,2)
loglog(Emb_Hist_Full_Cent,Emb_Hist_Full,'o')
xlabel('Embeddedness')
ylabel('Edges')

figure
subplot(2,1,1)
semilogy(Norm_Emb_Hist_Full_Cent,Norm_Emb_Hist_Full,'o')
title('Normalized Embeddedness - Full Network')
xlabel('Normalized Embeddedness')
ylabel('Edges')
subplot(2,1,2)
loglog(Norm_Emb_Hist_Full_Cent,Norm_Emb_Hist_Full,'o')
xlabel('Normalized Embeddedness')
ylabel('Edges')

figure
subplot(2,1,1)
semilogy(Emb_Hist_NFF_Cent,Emb_Hist_NFF,'o')
title('Embeddedness - Non-Fringe to Fringe')
xlabel('Embeddedness')
ylabel('Edges')
subplot(2,1,2)
loglog(Emb_Hist_NFF_Cent,Emb_Hist_NFF,'o')
xlabel('Embeddedness')
ylabel('Edges')

figure
subplot(2,1,1)
semilogy(Norm_Emb_Hist_NFF_Cent,Norm_Emb_Hist_NFF,'o')
title('Normalized Embeddedness - Non-Fringe to Fringe')
xlabel('Normalized Embeddedness')
ylabel('Edges')
subplot(2,1,2)
loglog(Norm_Emb_Hist_NFF_Cent,Norm_Emb_Hist_NFF,'o')
xlabel('Normalized Embeddedness')
ylabel('Edges')

figure
subplot(2,1,1)
semilogy(Emb_Hist_NFNF_Cent,Emb_Hist_NFNF,'o')
title('Embeddedness - Non-Fringe to Non-Fringe')
xlabel('Embeddedness')
ylabel('Edges')
subplot(2,1,2)
loglog(Emb_Hist_NFNF_Cent,Emb_Hist_NFNF,'o')
xlabel('Embeddedness')
ylabel('Edges')

figure
subplot(2,1,1)
semilogy(Norm_Emb_Hist_NFNF_Cent,Norm_Emb_Hist_NFNF,'o')
title('Normalized Embeddedness - Non-Fringe to Non-Fringe')
xlabel('Normalized Embeddedness')
ylabel('Edges')
subplot(2,1,2)
loglog(Norm_Emb_Hist_NFNF_Cent,Norm_Emb_Hist_NFNF,'o')
xlabel('Normalized Embeddedness')
ylabel('Edges')

figure
subplot(2,1,1)
semilogy(Deg_Hist_Full_Cent,Deg_Hist_Full,'o')
title('Degree - Full Network')
xlabel('Degree')
ylabel('Nodes')
subplot(2,1,2)
loglog(Deg_Hist_Full_Cent,Deg_Hist_Full,'o')
xlabel('Degree')
ylabel('Nodes')

figure
subplot(2,1,1)
semilogy(Deg_Hist_Fringe_Cent,Deg_Hist_Fringe,'o')
title('Degree - Fringe Network')
xlabel('Degree')
ylabel('Nodes')
subplot(2,1,2)
loglog(Deg_Hist_Fringe_Cent,Deg_Hist_Fringe,'o')
xlabel('Degree')
ylabel('Nodes')

figure
subplot(2,1,1)
semilogy(Deg_Hist_NFF_Cent,Deg_Hist_NFF,'o')
title('Degree - Non-Fringe Network')
xlabel('Degree')
ylabel('Nodes')
subplot(2,1,2)
loglog(Deg_Hist_NFF_Cent,Deg_Hist_NFF,'o')
xlabel('Degree')
ylabel('Nodes')

figure
subplot(2,1,1)
semilogy(Deg_Hist_NFNF_Cent,Deg_Hist_NFNF,'o')
title('Degree - Non-Fringe to Non-Fringe')
xlabel('Degree')
ylabel('Nodes')
subplot(2,1,2)
loglog(Deg_Hist_NFNF_Cent,Deg_Hist_NFNF,'o')
xlabel('Degree')
ylabel('Nodes')

