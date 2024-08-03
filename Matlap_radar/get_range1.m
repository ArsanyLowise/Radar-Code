function range=get_range1(pt,gRX,gTX,freq,pr,RCS,loss)
% This function delivers the received power out of the radar equation
pt = 30;           % transmit power in dBm
gRX = 10;          % RX antenna gain in dB
gTX = 10;          % TX antenna gain in dB
freq = 2.4;        % operating frequency in GHz
pr = 20;           %received power in dBm
RCS = 10;          % radar cross section in dBsm
loss = 5;          % total loss in dB 

c0=3e8;                 % speed of light
lamda=c0/(freq*1e9);    % wave length in meter

lamda_db=20*log10(lamda);   % converting to dB values
pi_db=30*log10(4*pi);       % converting to dB values
%range_db=40*log10(Rn);      % converting to dB values

% pr and pt must of same unit
range_db = pt + gRX + gTX + lamda_db + RCS - pi_db - pr -loss;
range=10^(range_db/40);

end