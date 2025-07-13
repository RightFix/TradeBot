from pybit.unified_trading import HTTP 
from pybit.exceptions import InvalidRequestError
import time

class code:
 def trading(k1,k2,k3):
  order_outputs = []
  if k1 != "" and k2 != "": 
   
   start_time = (time.time() * 1000)
   end_time  = time.time()
   crypto_data = {}
   order_filter_buy = {}
   order_filter_sell = {}
   crypto =  sorted(["GNOUSDT","DASHUSDT","AVAXUSDT","BANANAUSDT","METISUSDT","EGLDUSDT","INJUSDT","LINKUSDT","ETCUSDT","ILVUSDT","ENSUSDT","KSMUSDT","SOLUSDT","MKRUSDT","QNTUSDT", "GMXUSDT"])

   session = HTTP( demo = bool(k3), timeout = 3600,force_retry = True,   api_key = str(k1),  api_secret = str(k2))
    
   def trade(y):
    num_of_candle = 60  
    time_length = num_of_candle + 120 # also run time of bot in minutes
     
    crypto_data[crypto[y]] = session.get_kline(category="linear", symbol = crypto[y], interval=1, start= start_time, end= end_time,limit= time_length).get("result").get("list")
    
    order_filter_buy[crypto[y]] = 0 # value is negligible
    order_filter_sell[crypto[y]] = 1000000 # value is negligible
    
    while num_of_candle < time_length :
     # coins information and Trades
     candle_0_59 = crypto_data.get(crypto[y])
     
     candle_60 = candle_0_59[num_of_candle ]
   
     candles_high = max([float(candle_0_59[a][2]) for a in range(num_of_candle)])
   
     candles_low = min([float(candle_0_59[a][3]) for a in range(num_of_candle)])
     
    
     # Finding the perfect swing highs and lows
    
     candle_high = float(candle_60[2])
     candle_low = float(candle_60[3])
     candle_open = float(candle_60[1])
     candle_close = float(candle_60[4])
    
     seconds = float(candle_60[0]) / 1000
     candle_time = time.strftime('%H:%M:%S %d/%m/%Y', time.localtime(seconds))
    
     def unit(n):
      if n >= 1:
        if n < 3 and n> 0:
          return n
        elif n > 2 and n < 10:
          return -1
        else:
             return unit(n/10)
      else:
           return unit(n*10)           
    
     quantity = round(((unit(candle_low) * 100)/ candle_low ),5) /10
     Profit_value = (candle_low * 0.5) / (unit(candle_low) * 100 )
    
     # strategies used are as follows; trap stategy, swing high/low
     #buy
     if (candles_high < candle_high)  and (candle_close > candle_open) and (quantity  > 0)  and (Profit_value > 0) and (candle_high > (Profit_value + order_filter_buy[crypto[y]])):
      
        session.place_order( category="linear",  symbol = crypto[y],  side ="Buy", qty = str(quantity),  tpTriggerBy ="LastPrice",   triggerPrice = str(candle_high),  takeProfit = str(candle_high + Profit_value), triggerBy = "LastPrice", timeInForce = "IOC" ,  triggerDirection = 1, orderType="Limit" , price = str(candle_high ), positionIdx = 0)
       
        order_outputs.append(f"{candle_high} {crypto[y]} buy  {candle_time}")
        order_filter_buy[crypto[y]] = candle_high
        
     #sell
     elif (candles_low > candle_low) and (candle_close < candle_open) and (quantity  > 0 ) and (Profit_value > 0) and (candle_low < ( order_filter_sell[crypto[y]]- Profit_value)) :
           
       session.place_order( category="linear",  symbol = crypto[y],  side ="Sell", qty = str(quantity),  tpTriggerBy ="LastPrice",  triggerPrice = str(candle_low),  takeProfit = str(candle_low - Profit_value), triggerBy = "LastPrice", timeInForce = "IOC", triggerDirection = 2,orderType="Limit", price = str(candle_low), positionIdx= 0)
      
       order_outputs.append(f"{candle_low} {crypto[y]} sell {candle_time}")
       order_filter_sell[crypto[y]] = candle_low
    
     num_of_candle += 1 #iteration
     #return order_outputs
   # Run Bot
   
   for a in range(0,len(crypto)):
       try:
          trade(a)
       except InvalidRequestError:
             continue
   return order_outputs
   