
ALPHA_MULTILAYER

start_Model Version
	4	6	
end_Model Version

start_Model Parms
	3	0	
	0.0	F	-5.0	5.0	F	'Angle Offset'	F	F	0.0	0.0	100000.0	F	100.0	
	T	
	116.44171787505859	T	10.0	500.0	F	'Roughness'	F	F	0.0	0.0	100000.0	F	100.0	
	F	
	100	
	''	
	NaN	
	NaN	
	-1	
	
	''	
	NaN	
	NaN	
	-1	
	
	''	
	NaN	
	NaN	
	-1	
	
	F	
	5.0	F	0.0	20.0	F	'# Back Reflections'	F	F	0.0	0.0	100000.0	F	100.0	
	100.0	F	0.0	100.0	F	'% 1st Reflection'	F	F	0.0	0.0	100000.0	F	100.0	
	
	T	
	2000.0	18000.0	
	F	
	'N,C,S'	
	T	
	F	
	20	
	0.0	F	0.0	50.0	F	'Bandwidth (eV)'	F	F	0.0	0.0	100000.0	F	100.0	
	9	
	F	
	T	
	F	
	F	
	5000.0	9000.0	
	F	
	5	
	F	
	F	
	'Ideal'	
	0.0	F	0.0	100.0	F	'% Thickness Non-uniformity'	F	F	0.0	0.0	100000.0	F	100.0	
	0.0	F	0.0	30.0	F	'Bandwidth (nm)'	F	F	0.0	0.0	100000.0	F	100.0	
	F	
	F	
	'All'	
	100.0	
	25	
	F	
	F	
	10.0	
	F	
	5	
	
	start_GlobalFit
		0	
		
	end_GlobalFit
	
	start_Ambient
		F	
		'(Not Specified)'	
		F	
		'(Not Specified)'	
		
	end_Ambient
	
	start_ScatteringFactor
		F	
		'(Not Specified)'	
		
	end_ScatteringFactor
	F	
	F	
	100.0	
	100.0	
	0.0	F	-5.0	5.0	F	'Wvl. Shift (nm)'	F	F	0.0	0.0	100000.0	F	100.0	
	1.0E-4	
	
	start_Simulation
		250.0	1000.0	5.0	45.0	75.0	10.0	100.0	F	0.5	
		F	
		1	
		0.0	F	0.0	10.0	F	'Angular Spread'	F	F	0.0	0.0	100000.0	F	100.0	
		'None'	
		0.0	F	-20.0	20.0	F	'#1'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-20.0	20.0	F	'#2'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-20.0	20.0	F	'#3'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-20.0	20.0	F	'#4'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-180.0	180.0	F	'Source Rot.'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-180.0	180.0	F	'Receiver Rot.'	F	F	0.0	0.0	100000.0	F	100.0	
		F	0	
	end_Simulation
	
	start_MultiSamp
		0	0	
		
		start_DS Weighting
			
		end_DS Weighting
		
	end_MultiSamp
	
	start_ParmCoupling
		0	
		
		start_ParmCouplingFitParms
			0	
		end_ParmCouplingFitParms
		
	end_ParmCoupling
	100.0	
	'Standard Ellipsometric'	
	0	
	50	
	F	
	'(none)'	
	5	
	0.0	F	0.0	1000.0	F	'Smear Width'	F	F	0.0	0.0	100000.0	F	100.0	
	F	
	0	
	F	
	
	start_BW Conv
		'Gaussian'	
		0.0	F	0.0	1.0	F	'Exp. Relative Amp.'	F	F	0.0	0.0	100000.0	F	100.0	
		1.0	F	0.0	50.0	F	'Exp. Relative Width'	F	F	0.0	0.0	100000.0	F	100.0	
		F	
		0.0	F	0.0	30.0	F	'Bandwidth (nm) IR'	F	F	0.0	0.0	100000.0	F	100.0	
		1000.0	
		
	end_BW Conv
	
	start_Patterning
		F	
		0	
		0.0	F	0.0	100.0	F	'% Patterned'	F	F	0.0	0.0	100000.0	F	100.0	
		
	end_Patterning
	
	start_Color Calc
		F	
		0	0	0	0	
		0	1	2	'0'	
	end_Color Calc
	'(none)'	
	5	
	0.0	F	0.0	1000.0	F	'Smear Width #2'	F	F	0.0	0.0	100000.0	F	100.0	
	'(none)'	
	5	
	0.0	F	0.0	1000.0	F	'Smear Width #3'	F	F	0.0	0.0	100000.0	F	100.0	
	
	start_MultiModel
		0	2	
		
		50.0	F	0.0	100.0	F	'mWt1'	F	F	0.0	0.0	100000.0	F	100.0	
		50.0	F	0.0	100.0	F	'mWt2'	F	F	0.0	0.0	100000.0	F	100.0	
		
	end_MultiModel
	F	
	0.0	F	-20.0	20.0	F	'PsiOffset'	F	F	0.0	0.0	100000.0	F	100.0	
	0.0	F	-20.0	20.0	F	'PsiOff #1'	F	F	0.0	0.0	100000.0	F	100.0	
	0.0	F	-20.0	20.0	F	'PsiOff #2'	F	F	0.0	0.0	100000.0	F	100.0	
	0.0	F	-20.0	20.0	F	'PsiOff #3'	F	F	0.0	0.0	100000.0	F	100.0	
	0.0	F	-20.0	20.0	F	'PsiOff #4'	F	F	0.0	0.0	100000.0	F	100.0	
	
	start_LAB MSE
		F	
		
	end_LAB MSE
	
	start_Multiple Angle Offsets
		3	
		50.0	0.1118869557883598	F	-5.0	5.0	F	'50.0° Angle Offset'	F	F	0.0	0.0	100000.0	F	100.0	
		60.0	0.1118869557883598	F	-5.0	5.0	F	'60.0° Angle Offset'	F	F	0.0	0.0	100000.0	F	100.0	
		70.0	0.1118869557883598	F	-5.0	5.0	F	'70.0° Angle Offset'	F	F	0.0	0.0	100000.0	F	100.0	
		F	
		
	end_Multiple Angle Offsets
	
	start_Multiple Reflection Angles
		F	
		3	
		50.0	100.0	F	0.0	100.0	F	'% 1st Reflection at 50.0°'	F	F	0.0	0.0	100000.0	F	100.0	
		60.0	100.0	F	0.0	100.0	F	'% 1st Reflection at 60.0°'	F	F	0.0	0.0	100000.0	F	100.0	
		70.0	100.0	F	0.0	100.0	F	'% 1st Reflection at 70.0°'	F	F	0.0	0.0	100000.0	F	100.0	
		
	end_Multiple Reflection Angles
	
	start_Multiple Back Reflections Angles
		F	
		3	
		50.0	5.0	F	0.0	20.0	F	'# Back Reflections at 50.0°'	F	F	0.0	0.0	100000.0	F	100.0	
		60.0	5.0	F	0.0	20.0	F	'# Back Reflections at 60.0°'	F	F	0.0	0.0	100000.0	F	100.0	
		70.0	5.0	F	0.0	20.0	F	'# Back Reflections at 70.0°'	F	F	0.0	0.0	100000.0	F	100.0	
		
	end_Multiple Back Reflections Angles
	
end_Model Parms

start_Derived Parms
	F	
	
end_Derived Parms

start_Derived Parms 2
	'Total Thickness'	1	6328.0	0.0	0.0	F	F	
	
end_Derived Parms 2

start_Previous Results
	F	
	''	
	F	
	'-'	
	F	
	
end_Previous Results

start_Selected Options
	
	start_Options_Model Options
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		
	end_Options_Model Options
	
	start_Options_Fit Options
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		
	end_Options_Fit Options
	
	start_Options_Other Options
		F	
		F	
		F	
		F	
		
	end_Options_Other Options
	
end_Selected Options

start_Prefit Stage Options
	F	
	
	start_Prefit Fit Parms
		0	
	end_Prefit Fit Parms
	
	start_Prefit Global Parms
		F	
		3700.0	50000.0	
		5	
		100	
		F	
		'All'	
		F	
		'N,C,S'	
		0	
		50	
		
	end_Prefit Global Parms
	
end_Prefit Stage Options

start_First Point Only Options
	T	F	
	0	
	0	
	
end_First Point Only Options

start_MM_Weighting
	'Absolute MSE'	
	
end_MM_Weighting

start_Model Nonidealities
	F	F	F	
	'nm'	
	
end_Model Nonidealities

start_Model Structure
	
	start_Layer0
		5000000.0	F	-0.0	1.0E8	F	'Substrate Thickness'	F	F	0.0	0.0	100000.0	F	100.0	
		'Layer'	'silicon wafer'	'ANGSTROMS'	''	'silicon wafer'	
		start_File Info
			'Si substrate, Herzinger et.al., JAP v83p3323y1998, (multi-wavelength, multi-sample analysis)'	
			1	
			
		end_File Info
		
		start_Mat Table
			697	
			
			start_Wvl Array
				'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'	
			end_Wvl Array
			
			start_e1 Array
				'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'	
			end_e1 Array
			
			start_e2 Array
				'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'	
			end_e2 Array
			
		end_Mat Table
		
		start_silicon wafer Fit Parms
			
		end_silicon wafer Fit Parms
		
		start_SL Parms
			0	1	
			
		end_SL Parms
		
	end_Layer0
	
	start_Layer1
		15.299999237060547	F	-10.0	50.0	T	'Native Oxide'	F	T	0.0	0.0	100000.0	F	100.0	
		'Layer'	'nativ oxide of silicon wafer'	'ANGSTROMS'	''	'nativ oxide of silicon wafer'	
		start_File Info
			'Native Si oxide, Herzinger et.al., JAP v83p3323y1998, (multi-wavelength, multi-sample analysis)'	
			1	
			
		end_File Info
		
		start_Mat Table
			697	
			
			start_Wvl Array
				'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'	
			end_Wvl Array
			
			start_e1 Array
				'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'	
			end_e1 Array
			
			start_e2 Array
				'H4sIAAAAAAAAAO3BAQ0AAADCoPdPbQ8HFAAAfBln4SHy5AoAAA=='	
			end_e2 Array
			
		end_Mat Table
		
		start_nativ oxide of silicon wafer Fit Parms
			
		end_nativ oxide of silicon wafer Fit Parms
		
		start_SL Parms
			0	1	
			
		end_SL Parms
		
	end_Layer1
	
	start_Layer2
		4952.139808764211	T	300.0	100000.0	F	'Thickness # 2'	F	F	0.0	0.0	100000.0	F	100.0	
		'Layer'	'B-Spline'	'BSPLINE'	''	'B-Spline'	
		start_B-Spline Fit Parms
			28	0.7337278106508875	5.904761904761905	T	
			T	
			1.5	
			0.0	
			0.3	
			T	
			F	
			0.0	F	0.0	1000.0	F	'UV Pole Amp (+0.1)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.1	F	0.0	1000.0	F	'UV1 Pole E+'	F	F	0.0	0.0	100000.0	F	100.0	
			1.782441805402816	T	-10.0	100.0	F	'E Inf'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0011037351736161	T	0.0	1000.0	F	'IR Amp'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	0.0	100.0	F	'IR Br'	F	F	0.0	0.0	100000.0	F	100.0	
			T	
			T	
			F	
			'spline'	
			F	
			F	
			T	
			1.2	
			100000.0	5000.0	
			T	
			'Gen-Osc'	'GENOSC'	''	'Gen-Osc'	
			start_GenOsc File Version
				1	
			end_GenOsc File Version
			
			start_Gen-Osc Misc Parms
				1	T	
				F	
			end_Gen-Osc Misc Parms
			
			start_Gen-Osc Fit Parms
				0	0.8521217364275933	T	0.0	30.0	F	'Einf'	F	F	0.0	0.0	100000.0	F	100.0	
				
			end_Gen-Osc Fit Parms
			
			start_Gen-Osc Grade Parms
				
			end_Gen-Osc Grade Parms
			
			start_Gen-Osc Energy Units
				F	''	
				
			end_Gen-Osc Energy Units
			
			start_Gen-Osc Permanent Poles
				311.68498823942036	T	-1000.0	1000.0	F	'UV Pole Amp.'	F	F	0.0	0.0	100000.0	F	100.0	
				8.751812606452392	T	1.0E-8	15.0	F	'UV Pole En.'	F	F	0.0	0.0	100000.0	F	100.0	
				0.0	T	0.0	2.0	F	'IR Pole Amp.'	F	F	0.0	0.0	100000.0	F	100.0	
				F	
				2.0	F	0.1	10.0	F	'Urbach Transition Energy'	F	F	0.0	0.0	100000.0	F	100.0	
				1.0	F	0.1	2.0	F	'Urbach Tail Slope'	F	F	0.0	0.0	100000.0	F	100.0	
				
				start_Pole Grade Parameters
					F	
					0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 3'	F	F	0.0	0.0	100000.0	F	100.0	
					F	
					0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 3'	F	F	0.0	0.0	100000.0	F	100.0	
					F	
					0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 3'	F	F	0.0	0.0	100000.0	F	100.0	
					F	
					0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
					0.0	F	-1000.0	1000.0	F	'Grade 3'	F	F	0.0	0.0	100000.0	F	100.0	
					
				end_Pole Grade Parameters
				
			end_Gen-Osc Permanent Poles
			
			start_Gen-Osc Reference Layer
				
			end_Gen-Osc Reference Layer
			
			start_Gen-OscEnabled Oscillators
				
			end_Gen-OscEnabled Oscillators
			
			start_SL Parms
				0	1	
				
			end_SL Parms
			
			0	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 0 {TieOff(1)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			1	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 1 {TieOff(2)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			2	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 2 {TieOff(3)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			3	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 3 {TieOff(4)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			4	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 4 (min-E)'	F	F	0.0	0.0	100000.0	F	100.0	
			5	0.5	F	1.0E-4	10.0	F	'Tie Off n+1 (max+E)'	F	F	0.0	0.0	100000.0	F	100.0	
			6	0.5	F	1.0E-4	10.0	F	'Tie Off n+2 {TieOff(n+1)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			7	1.0	F	1.0E-4	10.0	F	'Tie Off n+3 {TieOff(n+2)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			8	2.0	F	1.0E-4	10.0	F	'Tie Off n+4 {TieOff(n+3)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			9	4.0	F	1.0E-4	10.0	F	'Tie Off n+5 {TieOff(n+4)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			2100.0	16900.0	
			T	
			
		end_B-Spline Fit Parms
		
		start_B-Spline Nodes
			-0.26627220425027365	-0.06627220127004141	0.13372780171019083	0.33372780469042307	0.5337278076706553	0.7337278106508875	1.037906286775065	1.3420847628992425	1.64626323902342	1.9504417151475975	2.2546201912717754	2.558798667395952	2.86297714352013	3.1671556196443076	3.4713340957684844	3.775512571892663	4.07969104801684	4.3838695241410175	4.688048000265195	4.992226476389373	5.29640495251355	5.600583428637727	5.904761904761905	6.404761904761905	6.904761904761905	7.904761904761905	9.904761904761905	13.904761904761905	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	
			-0.08473450257168641	F	-1000.0	1000.0	T	'spline_e2(0.134)'	T	F	0.0	0.0	100000.0	F	100.0	
			-0.16946900514337282	F	-1000.0	1000.0	T	'spline_e2(0.334)'	T	F	0.0	0.0	100000.0	F	100.0	
			-0.2567712199142012	T	-1000.0	1000.0	T	'spline_e2(0.534)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.0	T	0.0	1000.0	T	'spline_e2(0.734)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.02820704393019266	T	0.0	1000.0	T	'spline_e2(1.038)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.07053208896870074	T	0.0	1000.0	T	'spline_e2(1.342)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.021580701103248567	T	0.0	1000.0	T	'spline_e2(1.646)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.0	T	0.0	1000.0	T	'spline_e2(1.950)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.0	T	0.0	1000.0	T	'spline_e2(2.255)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.0	T	0.0	1000.0	T	'spline_e2(2.559)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.004164647053593681	T	0.0	1000.0	T	'spline_e2(2.863)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.031899408916096175	T	0.0	1000.0	T	'spline_e2(3.167)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.003601902970145323	T	0.0	1000.0	T	'spline_e2(3.471)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.5126637057754717	T	0.0	1000.0	T	'spline_e2(3.776)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.4313507031087735	T	0.0	1000.0	T	'spline_e2(4.080)'	T	F	0.0	0.0	100000.0	F	100.0	
			5.491010943178723	T	0.0	1000.0	T	'spline_e2(4.384)'	T	F	0.0	0.0	100000.0	F	100.0	
			5.893373197380749	T	0.0	1000.0	T	'spline_e2(4.688)'	T	F	0.0	0.0	100000.0	F	100.0	
			6.873721417165991	T	0.0	1000.0	T	'spline_e2(4.992)'	T	F	0.0	0.0	100000.0	F	100.0	
			5.491042066129224	T	0.0	1000.0	T	'spline_e2(5.296)'	T	F	0.0	0.0	100000.0	F	100.0	
			4.114555078738343	T	0.0	1000.0	T	'spline_e2(5.601)'	T	F	0.0	0.0	100000.0	F	100.0	
			6.249111102976279	T	0.0	1000.0	T	'spline_e2(5.905)'	T	F	0.0	0.0	100000.0	F	100.0	
			7.5535929242149304	T	0.0	1000.0	T	'spline_e2(6.405)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.4742289546043858	T	-1000.0	1000.0	T	'spline_e2(6.905)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e2(7.905)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			
			0.0	F	-1000.0	1000.0	T	'spline_e1(-0.125)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(0.175)'	F	F	0.0	0.0	100000.0	F	100.0	
			4.968595583875127	T	-1000.0	1000.0	T	'spline_e1(0.475)'	F	F	0.0	0.0	100000.0	F	100.0	
			4.940338833063255	T	-1000.0	1000.0	T	'spline_e1(0.775)'	T	F	0.0	0.0	100000.0	F	100.0	
			4.909054573235824	T	-1000.0	1000.0	T	'spline_e1(1.107)'	T	F	0.0	0.0	100000.0	F	100.0	
			4.928405668880008	T	-1000.0	1000.0	T	'spline_e1(1.439)'	T	F	0.0	0.0	100000.0	F	100.0	
			4.947713223941249	T	-1000.0	1000.0	T	'spline_e1(1.771)'	T	F	0.0	0.0	100000.0	F	100.0	
			4.965152305932048	T	-1000.0	1000.0	T	'spline_e1(2.071)'	T	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(2.371)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(2.671)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(2.967)'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			
			
		end_B-Spline Nodes
		
		start_Node Positioning Ranges
			0	
		end_Node Positioning Ranges
		
		start_SL Parms
			0	1	
			
		end_SL Parms
		
	end_Layer2
	
end_Model Structure
