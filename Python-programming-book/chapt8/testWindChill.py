
T=0
V=5
windChill = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
print(int(windChill))