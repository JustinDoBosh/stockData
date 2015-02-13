from yahoo_finance import Share
from pprint import pprint
from datetime import datetime

class stockLookUp():
	def __init__(self):
		stkSymbol = raw_input("Enter stock symbol: ")
		self.stkSymbol = stkSymbol
		stk = Share(stkSymbol)
		#Gather info for the following stk symbol 
		global openPrice 
		openPrice= stk.get_open()
		global currentPrice 
		currentPrice = stk.get_price()
		global change 
		change = stk.get_change()
		global prevClose 
		prevClose = stk.get_prev_close()
		global avgDailyVol
		avgDailyVol = stk.get_avg_daily_volume()
		global mtkCap
		mtkCap = stk.get_market_cap()
		global bval
		bval = stk.get_book_value()
		global ebitda 
		ebitda = stk.get_ebitda()
		global divYield
		divYield = stk.get_dividend_yield()
		global EPS
		EPS = stk.get_earnings_share()
		global dayHigh
		dayHigh = stk.get_days_high()
		global dayLow
		dayLow = stk.get_days_low()
		global yrHigh
		yrHigh = stk.get_year_high()
		global yrLow
		yrLow = stk.get_year_low()
		global fiftyDayMA
		fiftyDayMA = stk.get_50day_moving_avg()
		global twoHudDayMA
		twoHudDayMA = stk.get_200day_moving_avg()
		global PERatio
		PERatio = stk.get_price_earnings_ratio()
		global PEGrowthRatio
		PEGrowthRatio = stk.get_price_earnings_growth_ratio()
		global shrtRatio 
		shrtRatio = stk.get_short_ratio()
		global info
		info = stk.get_info()

	def generalInfo(self):
		print "\n*********displaying general stock information*********\n"
		for key, value in info.iteritems():
			if value == " " or type(value) != str:
				print key + ": " + "No data to display"
			else:
				print key + ": " + value 
			print "\n"
	
	def pricingInfo(self):
		pInfo = {"Opening price " : openPrice, "Current price " : currentPrice, "Price change " : change, "Previous day close " : prevClose, "Day high " : dayHigh, "dayLow " : dayLow, "Year high " : yrHigh, "Year low " : yrLow}
		print "\n*********displaying stock price information*********\n"
		for key, value in pInfo.iteritems():
			if value == " " or type(value) != str:
				print key + ": " +"No data to display"
			else:
				print key + ": " + value 
			print "\n"

	def ratios(self):
		ratioInfo = {"Price earnings ratio " : PERatio, "Price earnings growth ratio " : PEGrowthRatio, "Short ratio " : shrtRatio}		
		print "\n*********displaying stock ratio information*********\n"
		for key, value in ratioInfo.iteritems():
			if value == " " or type(value) != str:
				print key + ": " + "No data to display"
			else:
				print key + ": " + value 
			print "\n"

	def movingAvg(self):
		movingAvgs = {"50 day moving average " : fiftyDayMA, "200 day moving averge " : twoHudDayMA}
		print "\n*********displaying stock moving average information*********\n"
		for key, value in movingAvgs.iteritems():
			if value == " " or type(value) != str:
				print key + ": " + "No data to display"
			else:
				print key + ": " + value 
			print "\n"

	def dividendInfo(self):
		divInfo = {"Dividend yield " : divYield}
		print "\n*********displaying stock dividend information*********\n"
		for key, value in divInfo.iteritems():
			if value == " " or type(value) != str:
				print key + ": " + "No data to display"
			else:
				print key + ": " + value 
			print "\n"

	def stockFinInfo(self):
		stkfin = {"Earnings per share " : EPS, "EBITDA " : ebitda, "Book value " : bval, "Market capitalization " : mtkCap}
		print "\n*********displaying stock financial information*********\n"
		for key, value in stkfin.iteritems():
			if value == " " or type(value) != str:
				print key + ": " + "No data to display"
			else:
				print key + ": " + value 
			print "\n"


stockX = stockLookUp()
stockX.generalInfo()
stockX.pricingInfo()
stockX.ratios()
stockX.movingAvg()
stockX.dividendInfo()
stockX.stockFinInfo()