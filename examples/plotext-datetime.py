import yfinance as yf
import plotext as plt

plt.date_form('d/m/Y')

start = plt.string_to_datetime('11/04/2022')
end = plt.today_datetime()
data = yf.download('goog', start, end)

prices = list(data["Close"])
dates = plt.datetimes_to_string(data.index)

plt.plot(dates, prices)

plt.title("Google Stock Price")
plt.xlabel("Date")
plt.ylabel("Stock Price $")
plt.show()