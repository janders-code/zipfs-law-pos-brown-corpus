df <- read.csv("C:/Users/kaleb/Downloads/ling450/word_data.csv")
df$log_freq <- log(df$frequency)
df$category <- relevel(factor(df$category), ref = "function")

model <- lm(length ~ log_freq * category, data = df)

# normality of residuals  qq plot
qqnorm(residuals(model))
qqline(residuals(model))

# normality histogram
hist(residuals(model), breaks = 40, main = "Residuals", xlab = "Residual")

# linearity and homoscedasticity - residuals vs fitted
plot(fitted(model), residuals(model),
     xlab = "Fitted Values",
     ylab = "Residuals",
     main = "Residuals vs Fitted")
abline(h = 0, col = "red")