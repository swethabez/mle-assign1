# stock-predictor

Week 12:

1. How does the Prophet Algorithm differ from an LSTM? Why does an LSTM have poor performance against ARIMA and Profit for Time Series?

The LSTM prediction is based on a set of last values, we are therefore less prone to variance due to seasonality and already consider the current trend. Prophet however, ** models the time series as an additive system and identifies trends & seasonalities. Prophet also requires less hyperparameter tuning as it is specifically designed to detect patterns in business time series. LSTM’s require lot more volume of data and computing resources to train.

While LSTMS’s do not rely on specific assumptions of stationarity its disadvantage is that LSTM based RNNs are difficult to interpret and it is challenging to gain intuition into their behavior. Also, careful hyperparameter tuning is required in order to achieve good results.

2. What is exponential smoothing and why is it used in Time Series Forecasting?
Exponential smoothing is a forecasting technique that assigns larger weights to more recent observations while assigning exponentially decreasing weights as the observations get increasingly distant - hence long term forecasts tend to be unreliable.

* simple exponential smoothing: set parameter (alpha between 0 and 1) for univariate series with no trend and seasonality patterns determined.
* double exponential smoothing: smoothing with linear trend. Introduce parameter beta (b), which controls the decay of the influence of change in trend -still no seasonality
* triple exponential smoothing: used on data with both linear trends and seasonal patterns. Apply exponential smoothing three times – level smoothing, trend smoothing, and seasonal smoothing using gamma (g) to control the influence of the seasonal component. 
* 
* 3. What is stationarity? What is seasonality? Why Is Stationarity Important in Time Series Forecasting?

Stationarity means that the statistical properties of a process generating a time series do not change over time - meaning the way the series changes does not change over time. When forecasting or predicting the future, most time series models assume that each point is independent of one another. The best indication of this is when the dataset of past instances is stationary. 

Seasonality is the re-occuring pattern at a fixed and known frequency based on a time of the year, week, or day.


4. How is seasonality different from cyclicality? Fill in the blanks:
seasonality is predictable, whereas cyclicality is not.


