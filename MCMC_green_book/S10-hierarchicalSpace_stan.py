# %%
import numpy as np
import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt
#import pystan
# import pyper

df = pd.read_csv("./data/c11/d.csv")
print(df)


plt.plot(df.index,df.y)
plt.show()

print(df.describe())


model11_3 = """
data {
   int<lower=1> N_site;
   int<lower=0> Y[N_site];
}

parameters {
   real beta;
   real r[N_site];
   real<lower=0> s_r;
}

model {
   for (j in 2:N_site){
      r[j] ~ normal(r[j-1], s_r);
   }
   for (j in 1:N_site){
      Y[j] ~ poisson_log(beta + r[j]);
    }
}

generated quantities {
   real<lower=0> Y_mean[N_site];
   for (j in 1:N_site){
      Y_mean[j] <- exp(r[j]);
      }
}
"""
Y=df.y

stan_data = {"N_site":50,"Y":Y}

# MCMCサンプリングのステップ数
iter_count= 1500

# MCMCサンプリングの反復数の指定(WinBUGSではデフォルト3)
chain_count = 3

# MCMCサンプリングの最初の何ステップの結果を使わないとするか(burnin)
warmup_count = 100

# MCMCサンプリングのステップのうち、何個飛ばしでサンプリング結果を記録するか
thin_count = 3

fit = pystan.stan(model_code=model11_3,
                  data=stan_data,
                  iter=iter_count,
                  chains=chain_count,
                  thin=thin_count,
                  warmup=warmup_count)


print(fit)

#%%
