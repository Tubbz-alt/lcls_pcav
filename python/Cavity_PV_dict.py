def Cavity_PV_Init(IOC, SIOC, BLD_IOC, Set):
    if Set == 1:
        Set_dic = dict([
            ('Phi_Shift_ps' , '748'),
            ('Phi_Shift_476', '750'),
            ('Atten1'       , ':BTAM1:Attenuator'),
            ('Atten2'       , ':BTAM2:Attenuator'),
            ('Amp1'         , ':BTAM1:RF:Switch'),
            ('Amp2'         , ':BTAM2:RF:Switch'),
            ('Status1'      , ':DigIn0:Port0:In0'),
            ('Status2'      , ':DigIn0:Port0:In1'),
            ('Cav_Gain1'    , '758'),
            ('Cav_Gain2'    , '770'),
            ('Bld_phi_rotat', ':BAT:PhaseRotation1'),
            ('Bld_Q_scale'  , ':BAT:ChargeScale1'),
            ('Bld_Cav_f'    , ':BAT:CavityFreq1'),
            ('Bld_Prec_t'   , ':BAT:PrecStart1'),
            ('MaxCount1'    , '757'),
            ('MaxCount2'    , '769'),
            ('Time1'        , '755'),
            ('Time2'        , '767'),
            ('Scale1'       , '752'),
            ('Scale2'       , '764'),
            ('Charge1'      , '754'),
            ('Charge2'      , '766'),
            ('Freq1'        , '756'),
            ('Freq2'        , '768'),
            ('Offset1'      , '753'),
            ('Offset2'      , '765'),
            ('fbck_gain1'   , '761'),
            ('fbck_gain2'   , '773'),
            ('Time_std1'    , '759'),
            ('Time_std2'    , '771'),
            ('Time_diff1'   , '760'),
            ('Time_diff2'   , '772'),
            ('Q1'           , '763'),
            ('Q2'           , '775'),
            ('Start_time1'  , '762'),
            ('Start_time2'  , '774'),
            ('Amp_gain1'    , 1),
            ('Amp_gain2'    , 2),
            ('bckg1'        , -21),
            ('bckg2'        , -157),
            ('Window_Crude_Time' , [2e-6, 8e-6]),
            ('Window_Fit_Time'   , [3.05e-6, 5e-6]),
            ('Window_Exact_Time' , [2.9259e-6, 2.9259e-6]),
            ('Attn_start'   , 9),
            ('Attn_end'     , 15),
            ('Attn_val'     , 12),
            ('Attn_Phi_Shift1', [0]*15),
            ('Attn_Phi_Shift2', [0]*15),
            ('Attn_Gain1'   , [0]*15),
            ('Attn_Gain2'   , [0]*15)
        ])
    else:
        Set_dic = dict([
            ('Phi_Shift_ps' , '718'),
            ('Phi_Shift_476', '717'),
            ('Atten1'       , ':BTAM3:Attenuator'),
            ('Atten2'       , ':BTAM4:Attenuator'),
            ('Amp1'         , ':BTAM3:RF:Switch'),
            ('Amp2'         , ':BTAM4:RF:Switch'),
            ('Status1'      , ':DigIn0:Port0:In2'),
            ('Status2'      , ':DigIn0:Port0:In3'),
            ('Cav_Gain1'    , '783'),
            ('Cav_Gain2'    , '795'),
            ('Bld_phi_rotat', ':BAT:PhaseRotation2'),
            ('Bld_Q_scale'  , ':BAT:ChargeScale2'),
            ('Bld_Cav_f'    , ':BAT:CavityFreq2'),
            ('Bld_Prec_t'   , ':BAT:PrecStart2'),
            ('MaxCount1'    , '782'),
            ('MaxCount2'    , '794'),
            ('Time1'        , '780'),
            ('Time2'        , '792'),
            ('Scale1'       , '777'),
            ('Scale2'       , '789'),
            ('Charge1'      , '779'),
            ('Charge2'      , '791'),
            ('Freq1'        , '781'),
            ('Freq2'        , '793'),
            ('Offset1'      , '778'),
            ('Offset2'      , '790'),
            ('fbck_gain1'   , '786'),
            ('fbck_gain2'   , '798'),
            ('Time_std1'    , '784'),
            ('Time_std2'    , '796'),
            ('Time_diff1'   , '785'),
            ('Time_diff2'   , '797'),
            ('Q1'           , '788'),
            ('Q2'           , '800'),
            ('Start_time1'  , '787'),
            ('Start_time2'  , '799'),
            ('Amp_gain1'    , 1),
            ('Amp_gain2'    , 2),
            ('bckg1'        , 38),
            ('bckg2'        , -3),
            ('Window_Crude_Time' , [2e-6, 8e-6]),
            ('Window_Fit_Time'   , [3.05e-6, 5e-6]),
            ('Window_Exact_Time' , [2.9259e-6, 2.9259e-6]),
            ('Attn_start'   , 9),
            ('Attn_end'     , 15),
            ('Attn_val'     , 12),
            ('Attn_Phi_Shift1', [0]*15),
            ('Attn_Phi_Shift2', [0]*15),
            ('Attn_Gain1'   , [0]*15),
            ('Attn_Gain2'   , [0]*15)
        ])
    
    # print Set_dic['Phi_Shift_476']
    PVs = dict([
        ('Ele_PV_Heater'           ,IOC+':Cavity'+str(Set)+':HeaterOn'),
        ('Ele_PV_Temper'           ,'UND:R01:BHC:05:KL3314:SLOT2:TEMP'+str(Set+4)),
        ('Ele_PV_Phi_Ctrl'         ,'LAS:UND:MMS:0'+str(3-Set)),
        ('Ele_PV_Phi_Shift_ps'     , SIOC+Set_dic['Phi_Shift_ps']),
        ('Ele_PV_Phi_Shift_476_Deg', SIOC+Set_dic['Phi_Shift_476']),
        ('Ele_PV_Atten1'           , IOC+Set_dic['Atten1']),
        ('Ele_PV_Atten2'           , IOC+Set_dic['Atten2']),
        ('Ele_PV_Amp1'             , IOC+Set_dic['Amp1']),
        ('Ele_PV_Amp2'             , IOC+Set_dic['Amp2']),
        ('Ele_PV_Status1'          , IOC+Set_dic['Status1']),
        ('Ele_PV_Status2'          , IOC+Set_dic['Status2']),
        ('Ele_PV_Cav_Gain1'        , SIOC+Set_dic['Cav_Gain1']),
        ('Ele_PV_Cav_Gain2'        , SIOC+Set_dic['Cav_Gain2']),
        ('Cav_PV_bld_phase_rotation' , BLD_IOC+Set_dic['Bld_phi_rotat']),
        ('Cav_PV_bld_charge_scale'   , BLD_IOC+Set_dic['Bld_Q_scale']),
        ('Cav_PV_bld_cav_freq'     , BLD_IOC+Set_dic['Bld_Cav_f']),
        ('Cav_PV_bld_prec_start'   , BLD_IOC+Set_dic['Bld_Prec_t']),
        ('Cav_PV_MaxCounts1'       , SIOC+Set_dic['MaxCount1']),
        ('Cav_PV_MaxCounts2'       , SIOC+Set_dic['MaxCount2']),
        ('Cav_PV_Time1'            , SIOC+Set_dic['Time1']),
        ('Cav_PV_Time2'            , SIOC+Set_dic['Time2']),
        ('Cav_PV_Scale1'           , SIOC+Set_dic['Scale1']),
        ('Cav_PV_Scale2'           , SIOC+Set_dic['Scale2']),
        ('Cav_PV_Charge1'          , SIOC+Set_dic['Charge1']),
        ('Cav_PV_Charge2'          , SIOC+Set_dic['Charge2']),
        ('Cav_PV_Freq1'            , SIOC+Set_dic['Freq1']),
        ('Cav_PV_Freq2'            , SIOC+Set_dic['Freq2']),
        ('Cav_PV_Offset1'          , SIOC+Set_dic['Offset1']),
        ('Cav_PV_Offset2'          , SIOC+Set_dic['Offset2']),
        ('Calc_PV_Fbck_Gain1'      , SIOC+Set_dic['fbck_gain1']),
        ('Calc_PV_Fbck_Gain2'      , SIOC+Set_dic['fbck_gain2']),
        ('Calc_PV_Time_Std1'       , SIOC+Set_dic['Time_std1']),
        ('Calc_PV_Time_Std2'       , SIOC+Set_dic['Time_std2']),
        ('Calc_PV_Time_Diff1'      , SIOC+Set_dic['Time_diff1']),
        ('Calc_PV_Time_Diff2'      , SIOC+Set_dic['Time_diff2']),
        ('Cav_PV_Q1'               , SIOC+Set_dic['Q1']),
        ('Cav_PV_Q2'               , SIOC+Set_dic['Q2']),
        ('Calc_PV_StartTime1'      , SIOC+Set_dic['Start_time1']),
        ('Calc_PV_StartTime2'      , SIOC+Set_dic['Start_time2']),
        ('Ele_Amp_gain1'           , Set_dic['Amp_gain1']),
        ('Ele_Amp_gain2'           , Set_dic['Amp_gain2']),
        ('Ele_bckg1'               , Set_dic['bckg1']),
        ('Ele_bckg2'               , Set_dic['bckg2']),
        ('Calc_Window_Crude_Time'  , Set_dic['Window_Crude_Time']),
        ('Calc_Window_Fit_Time'    , Set_dic['Window_Fit_Time']),
        ('Calc_Window_Exact_Time'  , Set_dic['Window_Exact_Time']),
        ('Ele_Attn_start'          , Set_dic['Attn_start']),
        ('Ele_Attn_end'            , Set_dic['Attn_end']),
        ('Ele_Attn_val'            , Set_dic['Attn_val']),
        ('Ele_Attn_Phi_Shift1'     , Set_dic['Attn_Phi_Shift1']),
        ('Ele_Attn_Phi_Shift2'     , Set_dic['Attn_Phi_Shift2']),
        ('Ele_Attn_Gain1'          , Set_dic['Attn_Gain1']),
        ('Ele_Attn_Gain2'          , Set_dic['Attn_Gain2'])
    ])
    return PVs