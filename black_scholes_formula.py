import math
# Standard Normal Cumulative Distribution Function
# Returns the probability that a value is less than or equal to z
def phi(z):
    return 0.5*(1+math.erf(z/math.sqrt(2)))

# r: risk-free Interest Rate
# S: Spot Price
# T: Time to Maturity
# V: Volatility
# K: Strike Price

def black_scholes(r,S,T,V,K):
    d_1=(math.log(S/K)+(r+(V**2)/2)*T)/(V*math.sqrt(T))
    d_2=(math.log(S/K)+(r-(V**2)/2)*T)/(V*math.sqrt(T))

    Call=S*phi(d_1)-K*math.exp(-r*T)*phi(d_2)
    Put=K*math.exp(-r*T)*phi(-d_2)-S*phi(-d_1)
    return(Call, Put)