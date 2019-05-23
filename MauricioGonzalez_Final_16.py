import numpy as np
a=[4,10,12,80,50,40]
b=[100,5,80,50,50,200]
t=[73,28,59,52,39,137]
def modelo(x,y,a,b,t):
    v=[]
    for i in range(len(a)):
        v.append(np.sqrt(((x-a[i])**2)+((y-b[i])**2))/t[i])
    return v
def logprob(vi,x,y,sig,a,b,t):
    x=np.asarray(x)
    y=np.asarray(y)
    vi=np.sqrt(x**2+y**2)/t
    d = vi-np.asarray(modelo(x,y,a,b,t))
    d = d/sig
    d = -0.5 * np.sum(d**2)
    return d
def MCMC_polynomial(v,a,b,x,y,t, e=1 , n_steps=50000):
    xr=[]
    for i in range(len(a)):
        xr.append(((x-a[i])**2)+((y-b[i])**2))
    yr=t
    sig=1
    f=np.random.rand(e+1,n_steps)
    f=f.astype(float)
    logpos=[logprob(f[0],xr,yr,sig,a,b,t)]
    sca=np.random.rand(e+1)
    for i in range(1,n_steps):
        for j in range(e+1):
            propuesta = f[:,i-1]+np.random.normal(loc=0.0, scale=sca[j])
            logposv=logprob(f[:,i-1],xr,yr,sig,a,b,t)
            logposn=logprob(propuesta,xr,yr,sig,a,b,t)
            r = min(1,np.exp(logposn-logposv))
            alpha = np.random.random()
            if(alpha<r):
                f[:,i]=propuesta
                logpos.append(logposn)
            else:
                f[:,i]=(f[:,i-1])
                logpos.append(logposv)
    return (np.mean(f,axis=1))
print(MCMC_polynomial(10,a,b,200,200,t, e=1 , n_steps=50000))
