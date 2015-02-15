from yahoo_finance import Share
from pprint import pprint
from datetime import datetime

class stockLookUp():
	def __init__(self):
		stkSymbol = raw_input("Enter stock symbol: ")
		self.stkSymbol = stkSymbol
		stk = Share(stkSymbol)
		global companySymbol
		companySymbol = stkSymbol
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

	def stockInformation(self):
		with open('stockInformation.txt', 'w') as si:
			#General Information
			si.write('\n*********displaying general information for ' +  companySymbol + ' *********\n')
			for key, value in info.iteritems():
				if value == ' ' or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					si.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					si.write(wInfo)
			#Pricing Information 
			pInfo = {"Opening price " : openPrice, "Current price " : currentPrice, "Price change " : change, "Previous day close " : prevClose, "Day high " : dayHigh, "dayLow " : dayLow, "Year high " : yrHigh, "Year low " : yrLow}
			si.write('\n*********displaying stock price information for ' + companySymbol + ' *********\n')
			for key, value in pInfo.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					si.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					si.write(wInfo)
			#Ratios
			ratioInfo = {"Price earnings ratio " : PERatio, "Price earnings growth ratio " : PEGrowthRatio, "Short ratio " : shrtRatio}		
			si.write('\n*********displaying ratio information for ' + companySymbol + ' *********\n')
			for key, value in ratioInfo.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					si.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					si.write(wInfo)
			#MovingAverages
			movingAvgs = {"50 day moving average " : fiftyDayMA, "200 day moving averge " : twoHudDayMA}
			si.write('\n*********displaying moving average information for ' + companySymbol + ' *********\n')
			for key, value in movingAvgs.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					si.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					si.write(wInfo)
			#Dividend Information 
			divInfo = {"Dividend yield " : divYield}
			si.write('\n*********displaying dividend information ' + companySymbol + ' *********\n')
			for key, value in divInfo.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					si.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					si.write(wInfo)
			#Stock Financial Information
			stkfin = {"Earnings per share " : EPS, "EBITDA " : ebitda, "Book value " : bval, "Market capitalization " : mtkCap}
			si.write('\n*********displaying financial information for ' + companySymbol + ' *********\n')
			for key, value in stkfin.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					si.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					si.write(wInfo)
		si.close()
		print companySymbol + '\'s stock information has been written to the file stockInformation.txt'

stockX = stockLookUp()
stockX.stockInformation()
