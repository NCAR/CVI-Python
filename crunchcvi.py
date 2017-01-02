#File: crunchcvi.py

import time
import math
import numpy as np

def cvioutput( input, cvfxlimits, cfexcess, cvfxoptions, nullsignals, flowonoff, cvimode, C0, C1, C2, more, tdl_cals, opc_cal):
	'''
	#INPUT array is of the form
	#	time, cvtas, counts, cvf1, cvfx0, cvfx1, cvfx2, cvfx3, cvfx4, 
	#	cvfx5, cvfx6, cvfx7, cvfx8, cvpcn, cvtt, cvtp, cvts, cvtcn, cvtai, 
	#	H2OR, ptdlR, ttdlR, TDLsignal, TDLlaser, TDLline, TDLzero, TTDLencl, 
	#	TTDLtec, TDLtrans, opc_cnts, opc_flow_raw, opc_pres_raw, ext1, ext2, 
	#	H2O-PIC, 18O, HDO
	
	
	#"data" and "calibrated" arrays are of the form:
	#	cvf1, cvfx0, cvfx1, cvfx2, cvfx3, cvfx4, 
	#	cvfx5, cvfx6, cvfx7, cvfx8, cvpcn, cvtt, 
	#	cvtp, cvts, cvtcn, cvtai

	
	#calcoeffs array is of the form (23 elements), parenthesis denote separate naming
	#	C0cvf1, C1cvf1, C2cvf1, C0cvfx0, C1cvfx0, C2cvfx0, 
	#	C0cvfx1, C1cvfx1, C2cvfx1, C0cvfx2, C1cvfx2, C2cvfx2, 
	#	C0cvfx3, C1cvfx3, C2cvfx3, C0cvfx4, C1cvfx4, C2cvfx4, 
	#	RHOD (rhod), CVTBL (cvtbl), CVTBR (cvtbr), CVOFF1 (cvoff1), CVOFF2 (LTip)	
	
	#tdl_data is as follows
	#	H2OR, ptdlR, ttdlR, TDLsignal, TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec, TDLtrans
	
	#opc_data is as follows:
	#	opc_cnts, opc_flow_raw, opc_pres_raw, ext1
	
	#zerocorrectedflows are the pressure and temperature corrected flows of the form.
	#	cvfx0c, cvfx1c, cvfx2c, cvfx3c, cvfx4c, 
	#	cvfx5c, cvfx6c, cvfx7c, cvfx8c, cvf1Z
	'''

	#Input values 3 -> 18 is composed of the "data" values above
	data = input[3:19] ; tdl_data = input[19:29] ; opc_data = input[29:33]
	
	#opc_cal input from files
	#NEEDS TO BE ADDED TO CALIBRATION SPACE, #opc_cal = [10.55600, 22.22200]
	
	opc_press = opc_cal[0] + opc_cal[1]*opc_data[2] #opc_data[2] corresponds to opc_pres_raw	
	
	#REMOVED MANUAL CALS, REPLACED WITH FUNCTION INPUT
	#C0 = [0.472500,0.084000,0.013000,0.499000,0.097000,0.000000,0.000000,-1.374000,0.000000,0.000000,-5.816600,-245.864050,-245.864050,-245.864050,-245.864050,-245.864050]
	#C1 = [2.866000,1.032000,0.396600,1.021000,1.958000,0.020000,3.000000,1.419940,1.000000,1.000000,342.050000,2358.886300,2358.886300,2358.886300,2358.886300,2358.886300]	
	#C2 = [0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.0353620,997.5559000,997.5559000,997.5559000,997.5559000,997.5559000]
	#more = [1.0000,9.8400,0.3175,0.0000,0.4000]
	
	#Default Null Signals Originall Used in LabView (NEEDS TO BE CHANGED), #These Null signals allowed instruments to be ignored
	#NullSignal = [0]*16, #NullSignal[7] = 1, #NullSignal[8] = 1, #NullSignal[9] = 1
	
	#Array to hold calibration coefficients for flows from inputs
	calcoeffs = [0]*23
	for i in range(0,6):
		calcoeffs[i*3] = C0[i]; calcoeffs[(i*3)+1] = C1[i]; calcoeffs[(i*3)+2] = C2[i]
		#clusters of three are, #c0cvf1...c2cvf1, #c0cvfx0..c2cvfx0, #.............., #c0cvfx4..c2cvfx4
		
	#Append "more" calibration coefficients to array
	for i in range(18,23):
		calcoeffs[i] = more[i-18]
		
	#Perform default calibration of flows, pressures, temps, etc., #based on calibtraion arrays
	calibrated = [0]*16	
	for i in range(0,16): calibrated[i] = C0[i] + C1[i]*data[i] + C2[i]*data[i]**2
		
	#USER INPUTS
	#	REQUIRES IMPLEMENTATION
	cvfxtemp = [20]*4 		#	#USER INPUT TEMPERATURE USED AS DEFAULT UNLESS OTHERWISE OVERWRITTEN	
	cvfxtempsource = [1]*4 	#1 denotes cnt1, 0 denotes user input
	cvfxsw = [0]*4 			#1 denotes connected, 0 denotes otherwise #is the instrument connected?
	cvfxmode = [1]*4 		#1 denotes from the DAQ, 0 is user input
	cvfxdatatype = [0]*4 	#0 denotes Mass, 1 denotes Volume
	cvfxalt = [1,3,3,3] 	#USER INPUT FLOATS FROM FRONT PANEL
							#	Denotes a default uncalibrated flow to use
							#	If necessary
							
							
	cvfxtemp = cvfxoptions[5][:]; cvfxtempsource = cvfxoptions[4][:]; cvfxsw = cvfxoptions[0][:]
	cvfxmode = cvfxoptions[1][:]; cvfxalt = cvfxoptions[2][:]; cvfxdatatype = cvfxoptions[3][:]	
	
	#Modifications to the flow based on if there are data,
	#	mass vs. volume input, etc.
	for i in range(0,4):
		if cvfxtempsource[i] == 1 : cvfxtemp[i] = calibrated[14]
		else: cvfxtemp[i] = cvfxtemp[i]
		if cvfxsw[i] == 0 : calibrated[i+6] = 0
		else:
			if cvfxmode[i] == 1 : calibrated[i+6] = C0[i+6] + C1[i+6]*data[i+6] + C2[i+6]*data[i+6]**2
			else: calibrated[i+6] = cvfxalt[i] #USER ENTERED FLOW
			if cvfxdatatype[i] == 1 : calibrated[i+6] = calibrated[i+6]*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[i]+273.15)) #calibrated[10] is cvpcn				

	#Calibration of opc_data parameters and cvfx4
	opc_flow = C0[5] + opc_data[1]*C1[5] #opc_data[1] corresponds to opc_flow_raw	
	calibrated[5] = opc_flow*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[1]+273.15)) #cvfxtemp[i] corresponds to cvfx6temp (user input)

	#'''TEMPORARY'''
	#For nulling a few of the signals
	for i in range(0,16):
		if nullsignals[i] == 1: calibrated[i] = 0
	
	#Needs to be removed?
	#H is the upper limit of airspeed, L is the lower limit
	shroud = 1; H = 300; L = 4; location = 1
	
	#Pull windspeed from dsm string
	wspd = input[1]
	
	#cvtascc appears to be the corrected total airspeed
	cvtascc = 0
	
	#If the wspd adjusted for the shroud is within the bounds of H and L
	#	then proceed with corrected total airspeed (TAS) calculation
	if shroud*location*wspd >= L and shroud*location*wspd <= H : cvtascc = shroud*location*wspd*100
		
	#Added to prevent dividing by zero
	#	NEEDS MODIFICATION TO JUST USE DEFAULT
	if cvtascc <= 0 : cvtascc = 0.0001
	
	#Zero Corrected Flows are the flows that have been corrected for
	#	Temp and Pres AND have been filtered for values less than 0.
	zerocorrectedflows = [0]*10
	
	#Initialization of flow summing parameters
	summedzerocorrectedflow = 0; summedflow = 0
	
	#Iteration of flows to correct for pressure and temperature
	#	IF the pressure is reported correctly.
	#	ALSO performs the flow summations.
	for i in range(1,10):
		if calibrated[10] > 0 : zerocorrectedflows[i] = ( calibrated[i]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
		else : zerocorrectedflows[i] = ( calibrated[i]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
		if zerocorrectedflows[i] < 0 : zerocorrectedflows[i] = 0.0001
		summedflow = summedflow + calibrated[i]
		summedzerocorrectedflow = summedzerocorrectedflow + zerocorrectedflows[i]	
		
	#Shift in index to place cvf1c at the beginning
	#	DOES NOT REQUIRE PRESSURE AND TEMP CORRECTION
	zerocorrectedflows[0] = calibrated[0]#calibrated[i]
	if zerocorrectedflows[0] < 0 : zerocorrectedflows[0] = 0.0001

	#IF the pressure is greater than 0,
	#	THEN perform calculation of cvftc, otherwise use 0.0001 for pressure
	if calibrated[10] > 0 : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
	else : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
	
	#Calculation of the enhancement factor?
	cvcfact=(cvtascc*math.pi*(calcoeffs[20]**2))/(cvftc*1000.0/60) #calcoeffs[20] corresponds to cvtbr;
	if cvcfact<1 : cvcfact=1
		
	#cutsize (NOT SURE IF NECESSARY))
	cutsize = 0#5	
		
	#Miscellaneous calculations, #NEEDS DEFINITIONS
	rhoa=calibrated[10]/(2870.12*(calibrated[11]+273.15)) #calibrated[10 & 11] correspond to cvpcn and cvtt respectively
	gnu=(0.0049*calibrated[11]+1.718)*0.0001
	cvrNw=cutsize*10**(-4)
	reNw=(2*cvrNw*cvtascc*rhoa)/gnu
	
	#UNSURE OF PRIOR FUNCTION, LEFT TO ENSURE 
	#cvl=CVTBL*cvf3/cvf1Z;
	cvl = calcoeffs[19]*(zerocorrectedflows[0] - summedflow)/zerocorrectedflows[0]

	#Prevent calculation of greater cut size radii
	cutsizelooplimit = 10
	
	#Code for presumably calculating cut size radius
	for cvrad in range(1,cutsizelooplimit*10+1):
		cvri=(cvrad/10)*10**(-4); rei= 2 * cvtascc * cvri * rhoa/gnu
		if rei <= 0 : rei = 0.0001
		cvli=(cvri*14.6969*calcoeffs[18] * ((0.408248*rei**(1/3)) + math.atan(2.44949*rei**(-1/3)) - 0.5*math.pi)/(3*rhoa))-calcoeffs[22]
		if cvli >= cvl:
			break
	cvrad = cvrad/10
	cvft=summedflow-calcoeffs[21]
		
	#tdl_data[1] corresponds to press, #tdl_data[2] corresponds to temp, #calcoeffs[20] corresponds to cvtbr;
	cvcfact_tdl=(cvtascc*math.pi*(calcoeffs[20]**2))/((cvft*1000.0/60)*(1013.23/tdl_data[1])*((tdl_data[2]+273.15)/294.26))
	if cvcfact_tdl<1 : cvcfact_tdl=1;
	
	#tdl_cals = [[-0.20000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.33675999999999995,0.00000000000000000,0.00000000000000000,0.00000000000000000],[-0.03415301800000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00144543240000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
	#tdl_cals = [[0.00000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
	
	#calibration of tdl coefficients based on temperature and pressure
	tdl_poly_coeffs = [0]*4
	tdl_poly_coeffs[0]=tdl_cals[0][0]+tdl_cals[0][1]*tdl_data[1]+tdl_cals[0][2]*tdl_data[1]*tdl_data[1]+tdl_cals[0][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	tdl_poly_coeffs[1]=tdl_cals[1][0]+tdl_cals[1][1]*tdl_data[1]+tdl_cals[1][2]*tdl_data[1]*tdl_data[1]+tdl_cals[1][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	tdl_poly_coeffs[2]=tdl_cals[2][0]+tdl_cals[2][1]*tdl_data[1]+tdl_cals[2][2]*tdl_data[1]*tdl_data[1]+tdl_cals[2][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	tdl_poly_coeffs[3]=tdl_cals[3][0]+tdl_cals[3][1]*tdl_data[1]+tdl_cals[3][2]*tdl_data[1]*tdl_data[1]+tdl_cals[3][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]

	#cvrho_tdl=C0+C1*TDL_H2O+C2*TDL_H2O*TDL_H2O+C3*TDL_H2O*TDL_H2O*TDL_H2O;
	cvrho_tdl=tdl_poly_coeffs[0]+tdl_poly_coeffs[1]*tdl_data[0]+tdl_poly_coeffs[2]*tdl_data[0]*tdl_data[0]+tdl_poly_coeffs[3]*tdl_data[0]*tdl_data[0]*tdl_data[0]
	RHOO_TDL=cvrho_tdl/cvcfact_tdl	
	
	#FIRST CALCULATION (CVRH just goes to output file) , #CVRH is CVI relative humidity in the TDL line   */
	TTDLK=tdl_data[2]+273.15#;                                /*First, Correct temp in C to K */
    #SATVP is saturation vapor pressure (g/m3) from Goff-Gratch and RAF Bull. 9 */
	SATVP=10**(23.832241-5.02808*math.log10(TTDLK)-1.3816E-7*(10**(11.334-0.0303998*TTDLK))+0+8.1328E-2*(10**(3.49149-1302.8844/TTDLK))-2949.076/TTDLK)
	
	cvrh=100*cvrho_tdl*TTDLK/(SATVP*216.68)
		
	if cvrho_tdl<=  0.0 : Z= -10
	else : Z = math.log(((tdl_data[2]+273.15))*cvrho_tdl/1322.3)

	cvdp = 273.0*Z/(22.51-Z) #/*CVDP is CVI Dew Point, Z is intermediate variable*/
	
	#Indicator in LabView
	cvrhoo_tdl=cvrho_tdl/cvcfact_tdl
	if cvrhoo_tdl>50  : cvrhoo_tdl=99
	if cvrhoo_tdl<-50 : cvrhoo_tdl=-99
	
	opc_press_mb = (opc_press*10)
	opcc = (opc_data[0]*60)/(opc_data[1]*1000); opcc_Pcor = opcc*calibrated[10]/opc_press
	opcco = opcc/cvcfact; opcco_Pcor = opcco*calibrated[10]/opc_press

	cvf3 = calibrated[0] - summedflow #Indicator in Labview Plot

	cvcnc1 = (input[2]/(zerocorrectedflows[2]*1000/60))
	cvcnc1 = cvcnc1*math.exp(cvcnc1*zerocorrectedflows[2]*4.167*10**(-6))
	
	cvcnc01 = cvcnc1/cvcfact
	
	#USER INPUTS
	cvfxwr = [0.00]*4
		
	#If lower <= flow <= Upper, flow set point from before, #	Otherwise, recalculate
	if flowonoff:
		if (zerocorrectedflows[1] <= (cvfxlimits[0] + 0.05)) and (zerocorrectedflows[1] >= (cvfxlimits[0] - 0.05)) :
			cvfxwr[0] = 0.0
		else:
			cvfxnw = cvfxlimits[0]*(calibrated[10]/1013.25)*(294.26/(calibrated[14]+273.15))
			cvfxwr[0] = (cvfxnw-calcoeffs[3])/calcoeffs[4] #will be 6 and 7 on next iteration.
		#Starting at cvfx2 to cvfx4 (index 2 to 3 on calibrated)
		for i in range(1,4) : # int i = 1 ; i < 4; i++ ) {
			if (zerocorrectedflows[i+2] <= cvfxlimits[i] + 0.05) and (zerocorrectedflows[i+2] >= cvfxlimits[i] - 0.05) :
				cvfxwr[i] = 0.0; #REPLACE WITH OLDER VALUE
			else :
				cvfxnw = cvfxlimits[i] * (calibrated[10]/1013.25)*(294.26/(calibrated[14] + 273.15))
				#cvfx0wr = ( cvfxnw – c0cvfx0) / c1cvfx0;
				cvfxwr[i] = ( cvfxnw - calcoeffs[(i+2)*3] ) / calcoeffs[(i+2)*3+1] #will be 9 (12) and 10 (13) on next iteration.			
	
	if flowonoff and not cvimode :
		cfexcess_cor=cfexcess*(calibrated[10]/1013.25)*294.26/(calibrated[14]+273.15)
		cfsummed=cfexcess_cor + summedflow + calcoeffs[21] - calibrated[5]  #cvoff1 is equivalent to calcoeffs[21]
		cvf1wr=( cfsummed - calcoeffs[0])/calcoeffs[1]
		'''
		if not setvalue :
			cfexcess_cor=cfexcess*(calibrated[10]/1013.25)*294.26/(calibrated[14]+273.15)
			cfsummed=cfexcess_cor + summedflow + calcoeffs[21] - calibrated[5]  #cvoff1 is equivalent to calcoeffs[21]
			cvf1wr=( cfsummed - calcoeffs[0])/calcoeffs[1]
		else:
			if reNw > 0 : 
				cvsNw=cvrNw*14.6969*calcoeffs[18]*((0.408248*reNw**(1/3))+math.atan(2.44949*reNw**(-1/3))-0.5*math.pi)/(3*rhoa)
			else: 
				cvsNw = 100
			cvlw=cvsNw-calcoeffs[22]
			cons=calcoeffs[19]/cvlw
			cvf1cw=-cvftc*cons/(1-cons)
			cvf1w=cvf1cw*(calibrated[10]/1013.25)*(294.26/(calibrated[11]+273.15))
			cvf1wr=(cvf1w - calcoeffs[0])/calcoeffs[1]  # //setvalueversion
		'''
	else: cvf1wr = 0.0

	if cvf1wr >= 5.0 : cvf1wr = 5.0
			
	#OLD OUTPUT
	#output = [dsmtime,cvfxwr[0],cvfxwr[1],cvfxwr[2],cvfxwr[3],cvf1wr,valvepositions[0],valvepositions[1],valvepositions[2],valvepositions[3],cvimode,fxflows,usernumchanges,cvrad,cvcfact,cvrh,cvdp,cvrhoo_tdl]
	
	if( input[34] != -99.99 ) : input[34] = calibrated[10]/(calibrated[14]+273.15) * 0.000217 * input[34]
	
	output = np.r_[input[0], 0, 0, 0, input[3:19], calibrated[10:16], zerocorrectedflows[:], #ENDS AT INDEX 35, next line is 36
		cvl, cvrhoo_tdl, cvrho_tdl, cvrad, cvcfact_tdl,  #ENDS AT 40, next line 41
		cvf3, input[1], cvcnc1, cvcnc01, cvcfact,  cvftc, cvrh, cvdp, #ENDS at 48, next line 49
		cvfxwr[0:4], cvf1wr, input[2], tdl_data[:], opcc, opcco, opc_data[0:2], 
		opcc_Pcor, opcco_Pcor, opc_press_mb, input[34:37]]
		
	#Command used to force kill python
	#	taskkill /F /im python.exe

	return output, calibrated
