from stockquant.quant import *		# 导入必要的模块

config.loads('config.json')			# 载入配置文件

tick = Market.tick("sh600519")
print(tick)