% Parameters
Fs = 1000;          % Sampling frequency (Hz)
T = 1/Fs;           % Sampling period (s)
L = 1500;           % Length of signal
t = (0:L-1)*T;      % Time vector

% Signal generation: A 50 Hz sine wave and a 120 Hz sine wave
f1 = 50;            % Frequency of first sine wave (Hz)
f2 = 120;           % Frequency of second sine wave (Hz)
signal = 0.7*sin(2*pi*f1*t) + sin(2*pi*f2*t);

% Adding noise to the signal
noise = 2*randn(size(t));
noisySignal = signal + noise;

% Plot the noisy time-domain signal
figure;
subplot(2,1,1);
plot(t, noisySignal);
title('Noisy Time-Domain Signal');
xlabel('Time (s)');
ylabel('Amplitude');

% Compute the FFT of the noisy signal
Y = fft(noisySignal);

% Compute the two-sided spectrum P2. Then compute the single-sided spectrum P1
P2 = abs(Y/L);      % Two-sided spectrum
P1 = P2(1:L/2+1);   % Single-sided spectrum
P1(2:end-1) = 2*P1(2:end-1);

% Define the frequency domain f
f = Fs*(0:(L/2))/L;

% Plot the single-sided amplitude spectrum
subplot(2,1,2);
plot(f, P1);
title('Single-Sided Amplitude Spectrum of Noisy Signal');
xlabel('Frequency (Hz)');
ylabel('Amplitude');
