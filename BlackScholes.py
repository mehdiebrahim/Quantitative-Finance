import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm

print(np.log(245/294))

class BlackScholes:
	def __init__(self,S=0,X=0,T=0,sigma=0,t=0):

		self.stock = S
		self.strike = X
		self.maturity = T
		self.interest  = t
		self.sigma = sigma

	def d1(self):
		return (np.log(self.stock/self.strike) + ((self.interest + self.sigma**2/2)*self.maturity))/(self.sigma*np.sqrt(self.maturity))

	def d2(self):
		return (np.log(self.stock/self.strike) + ((self.interest - self.sigma**2/2)*self.maturity))/(self.sigma*np.sqrt(self.maturity))

	def call(self):
		N1 = norm.cdf(self.d1()) 
		N2 = norm.cdf(self.d2())
		Ce = N1*self.stock - N2*self.strike*np.exp(-self.interest*self.maturity)

		return Ce

	def put(self):

		N1 = ss.norm.cdf(-self.d1()) 
		N2 = ss.norm.cdf(-self.d2())
		Pe = N2*self.strike*np.exp(-self.interest*self.maturity) - N1*self.stock
		
		return Pe

def plots_call_vs_maturity(S,X,T,stock_prices,sigma,t):
	
	calls = []
	for stock in stock_prices:
		model = BlackScholes(S=stock,X=X,T=T,sigma=sigma,t=t)
		calls.append(model.call())


	return plt.plot(stock_prices,calls)

plots_call_vs_maturity(S=245,X=294,T=0.000002,stock_prices=np.arange(405,1,-1),sigma=0.2,t=0.1)
plt.axvline(294,linestyle='--')
plt.xlabel('time (days)')
plt.ylabel('Call option price')
plt.show()
