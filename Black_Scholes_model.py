from openbb_terminal.sdk import openbb
from math import log, sqrt, exp
from scipy.stats import norm

S = 106.25
X = 110
T = 18/252
r = 0.04
sigma = 70/100
d1 = (log(S/X)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))
d2 = (d1-sigma*sqrt(T))


Call_price = S*norm.cdf(d1)-X*exp(-r*T)*norm.cdf(d2)
Put_price = X*exp(-r*T)*norm.cdf(-d2)-(S*norm.cdf(-d1))

print(('Call: {}, Put: {}'.format(Call_price, Put_price)))


df=openbb.stocks.options.chains("AMD", expiration="2023-10-20")
df=df.loc[df['strike']==110]
print(df)


