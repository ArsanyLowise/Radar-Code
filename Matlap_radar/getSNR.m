function [s2nr]=getSNR(pt,gRX,gTX,NF,freq,fft_bin,Rn,T,RCS,loss)
pt = 30;           % transmit power in dBm
gRX = 10;          % RX antenna gain in dB
gTX = 10;          % TX antenna gain in dB
NF = 3;            % noise figure in dB
freq = 2.4;        % operating frequency in GHz
fft_bin = 1e6;     % effective bandwidth of the receiver in Hz
T = 293;           % ambient temperature (room temperature in Kelvin)
Rn = 1000;         % range in meters
RCS = 10;          % radar cross section in dBsm
loss = 5;          % total loss in dB
% SNR in dB 

c0=3e8;                     % Speed of light in m/s
lamda = c0/(freq*1e9);      % wave length in m
k=1.38*10^(-23);            % k: Boltzmann constant in Ws/K

% factor: 10*log10(lamda^2/(((4*pi)^3*k*BW))
factor= 10*log10(lamda^2/(((4*pi)^3*k*T*fft_bin)))-10*log10(Rn^4)+RCS; % here noise floor is included

lamda_db=20*log10(lamda);
pi_db=30*log10(4*pi);
bw_db=10*log10(fft_bin);
KT_db=10*log10(k*T);
noise_floor_dB=bw_db+KT_db;
range_db=40*log10(Rn);

display(['Gtx in dB:' num2str(gTX)]);
display(['Grx in dB:' num2str(gRX)]);
display(['NF in dB:' num2str(NF)]);
display(['Pt in dBm (3) :' num2str(pt)]);
display(['RCS in dBsm:' num2str(RCS)]);

display(['20*log10(lamda):' num2str(lamda_db)]);
display(['30*log10(4*pi):' num2str(pi_db)]);
display(['10*log10(BW):' num2str(bw_db)]);
display(['10*log10(k*T):' num2str(KT_db)]);
display(['Noise floor [10*log10(BW)+10*log10(k*T)]:' num2str(noise_floor_dB) ' dBwatt']);
display(['40*log10(Rn):' num2str(range_db)]);
display(['factor' num2str(factor)]);

% if pt is in dBm, noise floor must be also in dBm, that's why comes '-30'
s2nr=pt-30 +gRX +gTX -loss -NF +factor;

end