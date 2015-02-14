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

	def generalInfo(self):
		with open('generalinfo.txt', 'w') as gi:
			gi.write('\n*********displaying general information for ' +  companySymbol + ' *********\n')
			for key, value in info.iteritems():
				if value == ' ' or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					gi.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					gi.write(wInfo)
				print "\n"
		gi.close()
		print "wrote general information to file.\n"


	def pricingInfo(self):
		with open('pricingInfo.txt', 'w') as pi:
			pInfo = {"Opening price " : openPrice, "Current price " : currentPrice, "Price change " : change, "Previous day close " : prevClose, "Day high " : dayHigh, "dayLow " : dayLow, "Year high " : yrHigh, "Year low " : yrLow}
			pi.write('\n*********displaying stock price information for ' + companySymbol + ' *********\n')
			for key, value in pInfo.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					pi.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					pi.write(wInfo)
				print "\n"
		pi.close()
		print "wrote pricing information to file.\n"


	def ratios(self):
		with open('stkRatios.txt', 'w') as sr:
			ratioInfo = {"Price earnings ratio " : PERatio, "Price earnings growth ratio " : PEGrowthRatio, "Short ratio " : shrtRatio}		
			sr.write('\n*********displaying ratio information for ' + companySymbol + ' *********\n')
			for key, value in ratioInfo.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					sr.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					sr.write(wInfo)
				print "\n"
		sr.close()
		print "wrote ratios to file.\n"


	def movingAvg(self):
		with open('movingAvgs.txt', 'w') as ma:
			movingAvgs = {"50 day moving average " : fiftyDayMA, "200 day moving averge " : twoHudDayMA}
			ma.write('\n*********displaying moving average information for ' + companySymbol + ' *********\n')
			for key, value in movingAvgs.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					ma.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					ma.write(wInfo)
				print "\n"
		ma.close()
		print "wrote moving averages to file.\n"


	def dividendInfo(self):
		with open('dividendInfo.txt', 'w') as di:
			divInfo = {"Dividend yield " : divYield}
			di.write('\n*********displaying dividend information ' + companySymbol + ' *********\n')
			for key, value in divInfo.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					di.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					di.write(wInfo)
				print "\n"
		di.close()
		print "wrote dividend information to file.\n"


	def stockFinInfo(self):
		with open('stkFinInfo.txt', 'w') as sfi:
			stkfin = {"Earnings per share " : EPS, "EBITDA " : ebitda, "Book value " : bval, "Market capitalization " : mtkCap}
			sfi.write('\n*********displaying financial information for ' + companySymbol + ' *********\n')
			for key, value in stkfin.iteritems():
				if value == " " or type(value) != str:
					wInfo = '\n' + key + ': ' + 'No data to display\n'
					sfi.write(wInfo)
				else:
					wInfo =  '\n' + key + ': ' + value + '\n' 
					sfi.write(wInfo)
				print "\n"
		sfi.close()
		print "wrote stock financial information to file.\n"

stockX = stockLookUp()
stockX.generalInfo()
stockX.pricingInfo()
stockX.ratios()
stockX.movingAvg()
stockX.dividendInfo()
stockX.stockFinInfo()