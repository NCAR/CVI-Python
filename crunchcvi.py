#File: crunchcvi.py

import time
import math
import numpy as np

def cvioutput( input, flowonoff, valvepositions, cvimode, C0, C1, C2, more, tdl_cals ):
	'''
	//C0, C1, C2 are three separate 16 element calibration arrays
	//data is passed in from ORIGINAL input array from index 3 – 18.
	//INPUT array is of the form
	/*
	time
	cvtas
	counts
	cvf1
	cvfx0
	cvfx1
	cvfx2
	cvfx3
	cvfx4
	cvfx5
	cvfx6
	cvfx7
	cvfx8
	cvpcn
	cvtt
	cvtp
	cvts
	cvtcn
	cvtai
	H2OR
	ptdlR
	ttdlR
	TDLsignal
	TDLlaser
	TDLline
	TDLzero
	TTDLencl
	TTDLtec
	TDLtrans
	opc_cnts
	opc_flow_raw
	opc_pres_raw
	ext1
	ext2
	H2O-PIC
	18O
	HDO
	*/
	/*
	"data" and "calibrated" arrays are of the form:
	cvf1
	cvfx0
	cvfx1
	cvfx2
	cvfx3
	cvfx4
	cvfx5
	cvfx6
	cvfx7
	cvfx8
	cvpcn
	cvtt
	cvtp
	cvts
	cvtcn
	cvtai
	*/
	/*
	calcoeffs array is of the form (23 elements), parenthesis denote separate naming
	C0cvf1
	C1cvf1
	C2cvf1
	C0cvfx0
	C1cvfx0
	C2cvfx0
	C0cvfx1
	C1cvfx1
	C2cvfx1
	C0cvfx2
	C1cvfx2
	C2cvfx2
	C0cvfx3
	C1cvfx3
	C2cvfx3
	C0cvfx4
	C1cvfx4
	C2cvfx4
	RHOD (rhod)
	CVTBL (cvtbl)
	CVTBR (cvtbr)
	CVOFF1 (cvoff1)
	CVOFF2 (LTip)	
	
	//TDL_data is as follows
	/*
	H2OR
	ptdlR
	ttdlR
	TDLsignal
	TDLlaser
	TDLline
	TDLzero
	TTDLencl
	TTDLtec
	TDLtrans
	*/
	
	//zerocorrectedflows is the pressure and temperature corrected flows of the form.
	/*
	cvfx0c
	cvfx1c
	cvfx2c
	cvfx3c
	cvfx4c
	cvfx5c
	cvfx6c
	cvfx7c
	cvfx8c
	cvf1Z
	*/
	'''


	#input = input.decode(encoding='utf-8')
	#input = input.split(',')
	#input = [float(i) for i in input]
	#37 elements in the input array
	data = input[3:19] #if data <= -99, use stored value from before
	data_default = [-0.071,-0.050,-0.025,-0.497,0.008,0.019,0.025,0.016,-0.025,2.463,2.365,0.766,0.715,0.956,0.110,0.881]
	for i in range(0,15):
		if data[i]<=-99 : data[i] = data_default[i]#0#0.0001
	tdl_data = input[19:29] #if tdl_data <= -1, use stored value from before, except for TDLzero which if equal to -99.99, use stored value.
	tdl_default = [0.402,817.033,43.943,1680.670,10840.300,272,-4115.330,35.093,43.267,35.093]
	for i in range(0,10):
		if tdl_data[i]<=-1: tdl_data[i] = tdl_default[i]#tdl_data[i] = 0.0001#0.0001#0.0001

	opc_data = input[29:33]
	
	opc_cal = [10.55600, 22.22200]
	opc_press = opc_cal[0] + opc_cal[1]*opc_data[2] #opc_data[2] corresponds to opc_pres_raw	
	
	C0 = [0.472500,0.084000,0.013000,0.499000,0.097000,0.000000,0.000000,-1.374000,0.000000,0.000000,-5.816600,-245.864050,-245.864050,-245.864050,-245.864050,-245.864050]
	C1 = [2.866000,1.032000,0.396600,1.021000,1.958000,0.020000,3.000000,1.419940,1.000000,1.000000,342.050000,2358.886300,2358.886300,2358.886300,2358.886300,2358.886300]	
	C2 = [0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.0353620,997.5559000,997.5559000,997.5559000,997.5559000,997.5559000]
	more = [1.0000,9.8400,0.3175,0.0000,0.4000]
	NullSignal = [0]*16
	NullSignal[7] = 1
	NullSignal[8] = 1
	NullSignal[9] = 1
	
	calcoeffs = [0]*23
	for i in range(0,6):
		calcoeffs[i*3] = C0[i]
		calcoeffs[(i*3)+1] = C1[i]
		calcoeffs[(i*3)+2] = C2[i]

	#clusters of three are
	#c0cvf1...c2cvf1
	#c0cvfx0..c2cvfx0
	#..............
	#c0cvfx4..c2cvfx4
		
	for i in range(18,23):
		calcoeffs[i] = more[i-18]
		
	calibrated = [0]*16	
	for i in range(0,16):
		calibrated[i] = C0[i] + C1[i]*data[i] + C2[i]*data[i]**2#data[i]*C2[i]
		
	cvfxtempinput = [20,20,20,20] #cvfx5...cvfx8    # USER INPUT
		
	opc_flow = C0[5] + opc_data[1]*C1[5] #opc_data[1] corresponds to opc_flow_raw	
	calibrated[5] = opc_flow*(calibrated[10]/1013.23)*(294.26/(cvfxtempinput[1]+273.15)) #cvfxtemp[i] corresponds to cvfx6temp (user input)

	#USER INPUTS
	cvfxtempsource = [1]*4 #[True]*4
	cvfxsw = [0]*4 #[True]*4
	cvfxmode = [1]*4 #[True]*4
	#cvfxmode = [1]*4 #[True]*4
	cvfxdatatype = [0]*4 #[True]*4
	cvfxalt = [1,3,3,3] 
	
	cvfxdatatype[1] = 1
	
	cvfxsw[0] = 1
	
	# /* USER INPUTS
	#cvfxtempsource is a 4 element boolean array denoting "Front Panel" or "cnt1"
	#cvfxsw is a 4 element boolean for IS THE INSTRUMENT CONNECTED?
	#cvfxmode is a 4 element boolean for "Front Panel" vs "DAQ_Input"
	#cvfxdatatype is a 4 element boolean for "volume" or "mass" (on is volume, off is mass)
	#cvfxalt is a 4 element float array for altitude?
	#cvfxtempinput is a 4 element temperature input
	#*/
	
	#OUTPUTS
	cvfxtemp = [0]*4#cvfxtempinput #[0]*4
	cvfxaux = [0]*4
	
	for i in range(0,4):
		if cvfxtempsource[i] == 1 :
			cvfxtemp[i] = calibrated[14]
			#cvfxtempsource[i] = calibrated[14] #calibrated[14] is cvtcn
		else:
			cvfxtemp[i] = cvfxtempinput[i];
		if cvfxsw[i] == 0 :
			cvfxaux[i] = 0
		else:
			if cvfxmode[i] == 1 :
				cvfxaux[i] = C0[i+6] + data[i+6]*C1[i+6] + data[i+6]*data[i+6]*C2[i+6]
			if cvfxmode[i] == 0 :
				cvfxaux[i] = cvfxalt[i] #user entry
			if cvfxdatatype[i] == 1 :
				cvfxaux[i] = cvfxaux[i]*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[i]+273.15)) #calibrated[10] is cvpcn	
		calibrated[i+6] = cvfxaux[i]
		
	for i in range(0,16):
		if NullSignal[i] == 1:
			calibrated[i] = 0
	
	shroud = 1
	H = 300
	L = 4
	location = 1
	cutsize = 0#5
	
	wspd = input[1]
	
	cvtascc = 0
	if shroud*location*wspd >= L and shroud*location*wspd <= H :
		cvtascc = shroud*location*wspd*100
	if cvtascc <= 0 :
		cvtascc = 0.0001
			
	zerocorrectedflows = [0]*10
	
	summedzerocorrectedflow = 0
	summedflow = 0
	
	for i in range(1,10):
		if calibrated[10] > 0 :
			zerocorrectedflows[i] = ( calibrated[i]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
		else :
			zerocorrectedflows[i] = ( calibrated[i]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
		if zerocorrectedflows[i] < 0 :
			zerocorrectedflows[i] = 0.0001
		summedflow = summedflow + calibrated[i+1]
		summedzerocorrectedflow = summedzerocorrectedflow + zerocorrectedflows[i]	
		
	zerocorrectedflows[0] = calibrated[0]#calibrated[i]
	if zerocorrectedflows[0] < 0 :
		zerocorrectedflows[0] = 0.0001
		
	#calcoeffs[21] === cvoff1c
	
	if calibrated[10] > 0 :
		cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
	else :
		cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
	
	
	cvcfact=(cvtascc*math.pi*(calcoeffs[20]**2))/(cvftc*1000.0/60) #calcoeffs[20] corresponds to cvtbr;
	if cvcfact<1 :
		cvcfact=1
		
		
	rhoa=calibrated[10]/(2870.12*(calibrated[11]+273.15)) #calibrated[10 & 11] correspond to cvpcn and cvtt respectively
	gnu=(0.0049*calibrated[11]+1.718)*0.0001
	cvrNw=cutsize*10**(-4)
	reNw=(2*cvrNw*cvtascc*rhoa)/gnu
	
	
	#print(cvrNw, cvtascc, rhoa, gnu, reNw)
	#cvl=CVTBL*cvf3/cvf1Z;
	
	if calibrated[0] < 0 :
		cvl = calcoeffs[19]*(0.0001 - summedflow)/zerocorrectedflows[0];
	else :
		cvl = calcoeffs[19]*(calibrated[0] - summedflow)/zerocorrectedflows[0]

	cutsizelooplimit = 10
	cvrad = 0
	
	#zerocorrectedflows[9] corresponds to cvf1Z;
	#calcoeffs[19] corresponds to cvtbl
	#calibrated[0] corresponds to cvf1
	
	#if cvtascc == 0 : 
		#cvtascc = 0.0001
	
	while True:
	    #cvri=i*1*10**(-4);
		#rei=2 * cvtassc * cvri *rhoa/gnu;
		#cvsi=cvri*14.6969*rhod * ((0.408248*rei**(1/3)) + atan(2.44949*rei**(-1/3)) - 0.5*pi)/(3*rhoa);
		#cvli=cvsi-LTip;	
		#calcoeffs[18] corresponds to rhod;
		#calcoeffs[22] corresponds to LTip;
		cvrad += 1
		cvri=(cvrad/10)*1*10**(-4)
		rei= 2 * cvtascc * cvri *rhoa/gnu
		#if rei == 0 : rei = 0.0001    #HAD TO ADD CHECK TO GET TO WORK
		cvsi=cvri*14.6969*calcoeffs[18] * ((0.408248*rei**(1/3)) + math.atan(2.44949*rei**(-1/3)) - 0.5*math.pi)/(3*rhoa)
		cvli=cvsi-calcoeffs[22]
		if cvrad/10 == cutsizelooplimit or cvli >= cvl :
			break
	cvrad = cvrad/10
	
	if cvrad < 0 or cvrad > 100 : cvrad = -99.99
	
	cvft=summedflow-calcoeffs[21]
		
	#tdl_data[1] corresponds to press
	#tdl_data[2] corresponds to temp
	#calcoeffs[20] corresponds to cvtbr;
	denom=(cvft*1000.0/60)*(1013.23/tdl_data[1])*((tdl_data[2]+273.15)/294.26)
	cfact_tdl=(cvtascc*math.pi*(calcoeffs[20]**2))/denom
	if cfact_tdl<1 : cfact_tdl=1;
	

	#TDL1_cals		
	#C0	C1	C2	C3
	#param_0	-0.20000000000000001	1.33675999999999995	-0.03415301800000000	0.00144543240000000
	#param_1	0.00000000000000000	0.00000000000000000	0.00000000000000000	0.00000000000000000
	#param_2	0.00000000000000000	0.00000000000000000	0.00000000000000000	0.00000000000000000
	#param_3	0.00000000000000000	0.00000000000000000	0.00000000000000000	0.00000000000000000
	
	#tdl_cals is a 2 dimensional 4x4 array with first index denoting which cal, and the second index denoting which parameter
	#tdl_poly_coeffs is a 4 element array containing poly coefficients
	
	
	#Matrix = [[0 for x in range(w)] for y in range(h)] 
	#tdl_cals = [[-0.20000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.33675999999999995,0.00000000000000000,0.00000000000000000,0.00000000000000000],[-0.03415301800000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00144543240000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
	#tdl_cals = [[0.00000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
	#myArray=[[1,2],[3,4]]
	tdl_poly_coeffs = [0]*4
	
	tdl_poly_coeffs[0]=tdl_cals[0][0]+tdl_cals[0][1]*tdl_data[1]+tdl_cals[0][2]*tdl_data[1]*tdl_data[1]+tdl_cals[0][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	tdl_poly_coeffs[1]=tdl_cals[1][0]+tdl_cals[1][1]*tdl_data[1]+tdl_cals[1][2]*tdl_data[1]*tdl_data[1]+tdl_cals[1][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	tdl_poly_coeffs[2]=tdl_cals[2][0]+tdl_cals[2][1]*tdl_data[1]+tdl_cals[2][2]*tdl_data[1]*tdl_data[1]+tdl_cals[2][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	tdl_poly_coeffs[3]=tdl_cals[3][0]+tdl_cals[3][1]*tdl_data[1]+tdl_cals[3][2]*tdl_data[1]*tdl_data[1]+tdl_cals[3][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	
	#C0=C0_0+C0_1*TDL_P+C0_2*TDL_P*TDL_P+C0_3*TDL_P*TDL_P*TDL_P;
	#C1=C1_0+C1_1*TDL_P+C1_2*TDL_P*TDL_P+C1_3*TDL_P*TDL_P*TDL_P;
	#C2=C2_0+C2_1*TDL_P+C2_2*TDL_P*TDL_P+C2_3*TDL_P*TDL_P*TDL_P;
	#C3=C3_0+C3_1*TDL_P+C3_2*TDL_P*TDL_P+C3_3*TDL_P*TDL_P*TDL_P;
		
	#RHO_TDL=C0+C1*TDL_H2O+C2*TDL_H2O*TDL_H2O+C3*TDL_H2O*TDL_H2O*TDL_H2O;
	RHO_TDL=tdl_poly_coeffs[0]+tdl_poly_coeffs[1]*tdl_data[0]+tdl_poly_coeffs[2]*tdl_data[0]*tdl_data[0]+tdl_poly_coeffs[3]*tdl_data[0]*tdl_data[0]*tdl_data[0]
	RHOO_TDL=RHO_TDL/cfact_tdl
	
	
	
	#OUTPUT FILE ONLY Calculations
		#FIRST CALCULATION (CVRH just goes to output file) 
		#CVRH is CVI relative humidity in the TDL line   */
	#TTDLK=(tdl_data[2]+273.15);                                /*First, Correct temp in C to K */
		#SATVP is saturation vapor pressure (g/m3) from Goff-Gratch and RAF Bull. 9 */
	#tdl_data[2] is ttdlR
	TTDLK=tdl_data[2]+273.15#;                                /*First, Correct temp in C to K */
    #          /*SATVP is saturation vapor pressure (g/m3) from Goff-Gratch and RAF Bull. 9 */
#tdl_data[2] = 43.760
	SATVP=10**(23.832241-5.02808*math.log10(TTDLK)-1.3816E-7*(10**(11.334-0.0303998*TTDLK))+0+8.1328E-2*(10**(3.49149-1302.8844/TTDLK))-2949.076/TTDLK);

	cvrh=100*RHO_TDL*TTDLK/(SATVP*216.68);
	
	
	#SATVP=10**(23.832241-5.02808*math.log(tdl_data[2]+273.15)-1.3816*10**(-7)*(10**(11.334-0.0303998*(tdl_data[2]+273.15)))+0+8.1328*10**(-2)*(10**(3.49149-1302.8844/(tdl_data[2]+273.15)))-2949.076/(tdl_data[2]+273.15))
	#Piece above may be natural log or base 10? Below ln was defined whereas log was defined above.
	#cvrh=100*RHO_TDL*(tdl_data[2]+273.15)/(SATVP*216.68)
		
	if RHO_TDL<=  0.0 : Z= -10
	else : Z = math.log(((tdl_data[2]+273.15))*RHO_TDL/1322.3);

	cvdp = 273.0*Z/(22.51-Z) #/*CVDP is CVI Dew Point, Z is intermediate variable*/

	#Indicator in LabView
	cvrho_tdl = RHO_TDL
	
	#Indicator in LabView
	cvrhoo_tdl=cvrho_tdl/cfact_tdl
	if cvrhoo_tdl>50  : cvrhoo_tdl=99
	if cvrhoo_tdl<-50 : cvrhoo_tdl=-99
	
	#Indicator in LabView
	#opc_press_mb=opc_cal_press_in*10;
	#cfact = cvcfact
	#SI = 1
	#opc_cnts = opc_data[0]
	#opc_flow = opc_data[1]
	#opcc =(opc_cnts*60)/(opc_flow*SI*1000);
	#opcco=opcc/cfact;
	#opcc_Pcor=opcc*cvpcn/opc_press_mb;
	#opcco_Pcor=opcco*cvpcn/opc_press_mb;
	opc_press_mb = opc_press*10
	opcc = (opc_data[0]*60)/(opc_data[1]*1*1000)
	opcco = opcc/cvcfact
	opcc_Pcor = opcc*calibrated[10]/opc_press
	opcco_Pcor = opcco*calibrated[10]/opc_press

	cvf3 = calibrated[0] - summedflow #Indicator in Labview Plot
	
	#Indicator in LabView
	#cnct = input[2]
	#CVDIV = 1
	#cvfx1C = zerocorrectedflows[1]
	#cvcnc1=(cnct*CVDIV/(cvfx1C*1000/60));
	#cvcnc1=cvcnc1*exp(cvcnc1*cvfx1C*4.167*10**(-6));
	cvcnc1 = (input[2]*1/(zerocorrectedflows[2]*1000/60))
	cvcnc1 = cvcnc1*math.exp(cvcnc1*zerocorrectedflows[2]*4.167*10**(-6))
	
	
	#Indicator in LabView
	#CFACT = cvcfact
	#CVCNC1 = cvcnc1
	cvcnc01 = cvcnc1/cvcfact
	#CVCNCO1=CVCNC1/CFACT;

	
	dsmtime = input[0]
	
	#USER INPUTS
	cvfxlimits = [0,2,5,2]#5,2,5]
	cvfxwr = [0]*5 #Element 1 is a dud?
	
	#flowonoff = False#True
	cvfxnw = 0
	
	#calibrated[10] is cvpcn
	#calibrated[14] is cvtcn
	#Seems a little funny as this requires it to be inside of the bounds to be zero (otherwise it is calculated)
	if flowonoff:
		if (zerocorrectedflows[1] <= (cvfxlimits[0] + 0.05)) and (zerocorrectedflows[1] >= (cvfxlimits[0] - 0.05)) :
			cvfxnw = cvfxlimits[0]*(calibrated[10]/1013.25)*(294.26/(calibrated[14]+273.15))
			cvfxwr[0] = (cvfxnw-calcoeffs[3])/calcoeffs[4] #will be 6 and 7 on next iteration.
		else :
			cvfxwr[0] = 0.0
	
	#Starting at cvfx2 to cvfx4 (index 2 to 3 on calibrated)
	for i in range(1,4) : # int i = 1 ; i < 4; i++ ) {
		if flowonoff:
			if (zerocorrectedflows[i+2] <= cvfxlimits[i] + 0.05) and (zerocorrectedflows[i+2] >= cvfxlimits[i] - 0.05) :
				cvfxwr[i] = 0.0;
			else :
				cvfxnw = cvfxlimits[i] * (calibrated[10]/1013.25)*(294.26/(calibrated[14] + 273.15))
				#cvfx0wr = ( cvfxnw – c0cvfx0) / c1cvfx0;
				cvfxwr[i] = ( cvfxnw - calcoeffs[(i+2)*3] ) / calcoeffs[(i+2)*3+1] #will be 9 (12) and 10 (13) on next iteration.
			
	#print(cvfxwr)
	
	counterflowexcess = 0.5
	cvf3cw = counterflowexcess
	setvalue = False#True
	#cvimode = False #(False is CVI, True is Total)
	
	if flowonoff and not cvimode :
		if not setvalue :
			cvf3w=cvf3cw*(calibrated[10]/1013.25)*294.26/(calibrated[14]+273.15)
			cvf1w=cvf3w + summedflow + calcoeffs[21] - calibrated[5]  #cvoff1 is equivalent to calcoeffs[21]
			#cvf1w=cvf3w+cvfx0+cvfx1+cvfx2+cvfx3+cvfx4+cvfx5+cvfx6+cvfx7+cvfx8 +cvoff1;
			cvf1wr=( cvf1w - calcoeffs[0])/calcoeffs[1]
		else:
			#calcoeffs[18] is equivalent to RHOD
			#calcoeffs[22] is equivalent to LTip
			#calcoeffs[19] is equivalent to cvtbl
			#calibrated[10] is equivalent to cvpcn
			#calibrated[11] is equivalent to cvtt
			if reNw > 0 : 
				cvsNw=cvrNw*14.6969*calcoeffs[18]*((0.408248*reNw**(1/3))+math.atan(2.44949*reNw**(-1/3))-0.5*math.pi)/(3*rhoa)
			else: 
				cvsNw = 100
			cvlw=cvsNw-calcoeffs[22]
			cons=calcoeffs[19]/cvlw
			cvf1cw=-cvftc*cons/(1-cons)
			cvf1w=cvf1cw*(calibrated[10]/1013.25)*(294.26/(calibrated[11]+273.15))
			cvf1wr=(cvf1w - calcoeffs[0])/calcoeffs[1]  # //setvalueversion
	else:
		cvf1wr = 0.0
	if cvf1wr >= 5.0 :
		cvf1wr = 5.0
		
	if cvimode : cvimode = 2
	else: cvimode = 0
		
	#valvepositions = [0]*4
	fxflows = (2*valvepositions[0])**3+(2*valvepositions[1])**2+(2*valvepositions[2])**1+valvepositions[3]
	usernumchanges = 0
	
	#output = [dsmtime,cvfxwr[0],cvfxwr[1],cvfxwr[2],cvfxwr[3],cvf1wr,
	#	valvepositions[0],valvepositions[1],valvepositions[2],valvepositions[3],
	#	cvimode,fxflows,usernumchanges,cvrad,cvcfact,cvrh,cvdp,cvrhoo_tdl]
	
	if( input[34] != -99.99 ) : input[34] = calibrated[10]/(calibrated[14]+273.15) * 0.000217 * input[34]
	
	cvcfact_tdl = cfact_tdl
	#input[1] is equivalent to cvtas
	#input[0] is equivalent to cnt1?
	
	output = np.r_[input[0], 0, 0, 0, input[3:19], calibrated[10:16], zerocorrectedflows[:], 
		cvl, cvrhoo_tdl, cvrho_tdl, cvrad, cvcfact_tdl,  
		cvf3, input[1], cvcnc1, cvcnc01, cvcfact,  cvftc, cvrh, cvdp, 
		cvfxwr[0:4], cvf1wr, input[2], tdl_data[:], opcc, opcco, opc_data[0:2], 
		opcc_Pcor, opcco_Pcor, opc_press_mb, input[34:37]]
		
	#tdl_data[:] represents H2O_TDL -> TDLtrans
	#H2O_PIC_cvrtd, 180, HDO]	
	
	#extra = [cvf3, cvcnc1, cvcnc01, cvrho_tdl, cvrhoo_tdl, opcc, opcco]
		
	
	#Desired Output is 
	#[60872.5,0,0,0,0,0,0,0,0,0,0,0,0,10,1,11.809,7.395,7.555]
	
	#taskkill /F /im python.exe
	#output = calcoeffs
	#return output, extra, calibrated, zerocorrectedflows
	return output, calibrated
