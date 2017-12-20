#File: main.py

from crunchcvi import *
import numpy as np

#Original Value
var1 = [60872.5,-99.99,0,-0.0742912,-0.0428617,-0.0301138,-0.496233,0.0196179,0.0263789,0.0316833,0.0239428,-0.0150093,2.44708,2.35505,0.512218,0.700784,0.855286,0.108917,0.208144,7.555,811.587,43.76,27380.3,10985.3,259,-4123.33,30.53,42.92,0.83,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]



#Flow on
var1 = [78282.5,-99.99,0,-0.070397,-0.0480576,-0.00259852,-0.482633,-0.00131634,0.0166402,0.0233463,0.0135805,-0.0263371,2.45774,2.37367,-99.99,0.765793,-99.99,-99.99,0.0745195,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
#Desired Output
output = [78282.5,-0.081,1.064,1.974,79.255,0.025,0,0,0,0,0,0,0,10.000,1.000,0.000,-83.974,0.000]
flowonoff = True
valvepositions = [0,0,0,0]
cvimode = False

'''
#Flow off
var1 = [78305.5,-99.99,0,-0.0735723,-0.040608,0.00646869,-0.488037,0.00348683,0.00632153,0.0191653,0.0118715,-0.0246281,2.46558,2.377074,-99.99,0.532216,-99.99,-99.99,0.0642347,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
output = [78305.500,0.000,0.000,0.000,0.000,0.000,0,0,0,0,0,0,0,10.000,1.000,0.000,-83.974,0.000]
flowonoff = False
valvepositions = [0,0,0,0]
cvimode = False
'''#Off Again

'''
#Flow on, test mode, valve 1 and 2 on
var1 = [78340.500,-99.99,0,-0.0767782,-0.0403943,-0.0131006,-0.491059,0.00770872,-0.00128012,0.0204471,0.0127871,-0.0301823,2.45049,2.37364,0.868481,-99.99,1.17739,-99.99,0.113873,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
output = [78340.500,-0.081,1.059,1.968,79.022,0.029,0,1,1,0,0,0,0,10.000,1.000,0.000,-83.974,0.000]
flowonoff = True
valvepositions = [0,1,1,0]
cvimode = False
#Seems to be off compared to rest
'''


'''
#Flow on, test mode, all valves on, CVI mode to total
var1 = [78370.5,-99.99,0,-0.0739998,-0.0537975,-0.011536,-0.492822,-0.00129339,0.0109237,0.02121,0.0101091,-0.0295644,2.45621,2.36038,0.540937,0.734752,0.945017,0.108874,0.403034,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
output = [78370.5,-0.081,1.052,1.960,78.679,0.000,1,1,1,1,1,0,0,10.000,1.000,0.000,-83.974,0.000]
flowonoff = True
valvepositions = [1,1,1,1]
cvimode = True
#Flows are correct, variables at end are wrong....?
'''


#Flow on, CVI mode to cvi, TDL On
var1 = [78470.5,-99.99,0,-0.0681376,-0.0563926,0.00943004,-0.485442,0.00214072,0.022746,0.0242618,0.0143435,-0.0278935,2.46137,2.36268,0.697071,0.410852,0.670648,0.108651,0.12196,5.086,821.973,33.8967,19949.7,11266.7,282,-4126,26.2067,30.2633,0.886,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
output = [78470.5,-0.081,1.057,1.966,78.910,0.024,0,0,0,0,0,0,0,10.000,1.000,13.233,2.033,5.086]
flowonoff = True
valvepositions = [0,0,0,0]
cvimode = False #(False is CVI, True is Total)




'''
#Flow on, CVI mode to cvi, TDL on, pump on
var1 = [78531.5,-99.99,0,-0.0788595,-0.0558583,0.685207,1.08903,1.98742,1.9909,1.99583,1.97874,1.87055,2.46571,2.37894,0.760185,0.687982,0.917672,-99.99,0.0563866,4.85133,819.7,37.74,19109.3,11096,272,-4128,27.07,34.08,0.890333,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
output = [78531.5,-0.081,1.055,1.963,79.301,2.036,0,0,0,0,0,0,0,0.100,1.000,10.306,1.605,4.851]
flowonoff = True
valvepositions = [0,0,0,0]
cvimode = False
'''

input = var1

#data = bytes(var1,'utf_8')

#input = data.decode(encoding='utf-8')
#input = input.split(',')
#input = [float(i) for i in input]


#tdl_cals = [[-0.20000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.33675999999999995,0.00000000000000000,0.00000000000000000,0.00000000000000000],[-0.03415301800000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00144543240000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
tdl_cals = [[0.00000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
C0 = [0.472500,0.084000,0.013000,0.499000,0.097000,0.000000,0.000000,-1.374000,0.000000,0.000000,-5.816600,-245.864050,-245.864050,-245.864050,-245.864050,-245.864050]
C1 = [2.866000,1.032000,0.396600,1.021000,1.958000,0.020000,3.000000,1.419940,1.000000,1.000000,342.050000,2358.886300,2358.886300,2358.886300,2358.886300,2358.886300]	
C2 = [0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.0353620,997.5559000,997.5559000,997.5559000,997.5559000,997.5559000]
more = [1.0000,9.8400,0.3175,0.0000,0.4000]

opc_cal = [10.55600, 22.22200]

counterflowexcess = 0.5


#input, cvfxlimits, counterflowexcess, cvfxoptions, nullsignals, flowonoff, cvimode, C0, C1, C2, more, tdl_cals, opc_cal):
cvfxoptions = [[0, 0, 0, 0], [0, 0, 0, 0], [3.0, 3.0, 3.0, 3.0], [0, 0, 0, 0], [0, 0, 0, 0], [20.0, 20.0, 20.0, 20.0]]
nullsignals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

output, calibrated = cvioutput( input , [0,2,5,2], counterflowexcess, cvfxoptions, nullsignals, flowonoff , cvimode, C0, C1, C2, more, tdl_cals, opc_cal)


data = np.round(np.r_[ output[0], output[49:54], 0, 0, 0, 0, output[1], 0, 0, output[39], output[45], output[47:49], output[37] ],3)

#data = np.r_[ output[0], output[49:54], 0, 0, 0, 0, output[1], 0, 0, output[39], output[45], output[47:49], output[37] ]
dataout = [ "{:.3f}".format(x) for x in data ]
dataout = ','.join(dataout)
#dataout = str(dataout).strip('[]')
#dataout = dataout.replace(" ","")
dataout+='\n'			
dataout = bytes(dataout,'utf_8')

print(dataout)

#data = cvioutput( input , flowonoff, valvepositions, cvimode)
#print(bytes(str(data).replace('\n','').strip('[]'),'utf_8'))