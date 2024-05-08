import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pystan

data_df = pd.read_csv("./data/c10/data7a.csv")

rng = np.random.RandomState(160)

data_df.head()

#stanコード
stan_model = """
data{
    int<lower=0> N;
    real<lower=0> x[N];
    real<lower=0> y[N];
}
parameters{
    real mu_x;
    real<lower=0> sigma_x;
    real mu_y;
    real<lower=0> sigma_y;
}
model{
    mu_x ~ normal(0,100);
    sigma_x ~ cauchy(0,5);
    mu_y ~ normal(0,100);
    sigma_y ~ cauchy(0,5);
    for(n in 1:N){
        x[n] ~ normal(mu_x, sigma_x);
    }
    for(n in 1:N){
        y[n] ~ normal(mu_y, sigma_y);
    }
}
generated quantities{
    real delta;
    real delta_over;
    delta = mu_x - mu_y;
    delta_over =   delta > 0 ? 1 : 0;
}
"""

#stanコードのコンパイル
sm = pystan.StanModel(model_code=stan_model)

#データの引き渡し
stan_data = {"N":data_df.shape[0], "x":data_df["x"], "y":data_df["y"]}

#Let's stan!
fit = sm.sampling(data = stan_data, iter=2000, warmup=500, chains = 4, seed=123)

print(fit)
