from hdfs.client import Client
import  pyhdfs
import json
import datetime
import sys
import os
import pandas as pd
import numpy as np
import time
import difflib
def analyse_data(syspath):
    a=0
    b=0
    thesame=0
    label_array=['time', 'FLOW_2_4_5', 'FLOW_2_2_5', 'FLOW_2_1_5', 'FLOW_2_0_5', 'FLOW_1_4_5', 'FLOW_1_3_5', 'FLOW_1_2_5', 'FLOW_1_1_5', 'FLOW_1_0_5', 'FLOW_0_4_5', 'FLOW_0_3_5', 'FLOW_0_2_5', 'FLOW_0_1_5', 'FLOW_0_0_5', 'PID_MAX_2_5', 'PID_MIN_2_5', 'PID_KP_2_5', 'PID_MAX_1_5', 'PID_MIN_1_5', 'PID_KP_1_5', 'PID_MAX_0_5', 'PID_MIN_0_5', 'PID_KP_0_5', 'PRE_JJQZG_IN', 'PRE_ELSZG_IN', 'SBS_ZG_YL', 'YYZ_JS_YL', 'TEM_JJQZG_IN', 'TE_ELS_ZG', 'SBS_JS_WD', 'YYZ_JS_WD', 'YYJ_XST_1', 'YYJ_XXT_1', 'YYJ_XQT_1', 'YYJ_XST_SET_1', 'YYJ_XXT_SET_1', 'YYJ_XQT_SET_1', 'YYJ_XST_2', 'YYJ_XXT_2', 'YYJ_XQT_2', 'YYJ_XST_SET_2', 'YYJ_XXT_SET_2', 'YYJ_XQT_SET_2', 'YYJ_XST_3', 'YYJ_XXT_3', 'YYJ_XQT_3', 'YYJ_XST_SET_3', 'SPEED_MIN_0_2', 'YYJ_XQT_SET_3', 'YYJ_XST_4', 'YYJ_XXT_4', 'YYJ_XQT_4', 'YYJ_XST_SET_4', 'YYJ_XXT_SET_4', 'YYJ_XQT_SET_4', 'YYJ_XST_5', 'YYJ_XXT_5', 'YYJ_XQT_5', 'YYJ_XST_SET_5', 'YYJ_XXT_SET_5', 'YYJ_XQT_SET_5', 'KD_2_4_5', 'KD_2_3_5', 'KD_2_2_5', 'KD_2_1_5', 'KD_2_0_5', 'KD_1_4_5', 'KD_1_3_5', 'KD_1_2_5', 'KD_1_1_5', 'KD_1_0_5', 'KD_0_4_5', 'KD_0_3_5', 'KD_0_2_5', 'KD_0_1_5', 'KD_0_0_5', 'FPBC_B_5', 'FPBC_A_5', 'ELS_KD_MAX_5', 'V_SP_2_5', 'V_SP_1_5', 'V_SP_0_5', 'ELS_FP_BL_2_5', 'ELS_FP_BL_1_5', 'ELS_FP_BL_0_5', 'ELS_BSL_5', 'YYZ_TDG_ZT_5', 'YYZ_LJG_ZT_5', 'KD_TJF_2_5', 'KD_TJF_1_5', 'KD_TJF_0_5', 'PEM_JJQ_IN_1', 'TEM_JJQ_OUT_1', 'PRE_ELS_0_1', 'PRE_ELS_1_1', 'PRE_ELS_2_1', 'SPEED_LZJ_1', 'FLOW_ELS_0_1', 'FLOW_ELS_1_1', 'FLOW_ELS_2_1', 'FLOW_JJQ_1', 'KD_TJF_0_1', 'KD_TJF_1_1', 'KD_TJF_2_1', 'YYZ_LJG_ZT_1', 'YYZ_TDG_ZT_1', 'ELS_BSL_1', 'ELS_FP_BL_0_1', 'ELS_FP_BL_1_1', 'ELS_FP_BL_2_1', 'V_SP_0_1', 'V_SP_1_1', 'V_SP_2_1', 'ELS_KD_MAX_1', 'FPBC_A_1', 'FPBC_B_1', 'KD_0_0_1', 'KD_0_1_1', 'KD_0_2_1', 'KD_0_3_1', 'KD_0_4_1', 'KD_1_0_1', 'KD_1_1_1', 'KD_1_2_1', 'KD_1_3_1', 'KD_1_4_1', 'KD_2_0_1', 'KD_2_1_1', 'KD_2_2_1', 'KD_2_3_1', 'KD_2_4_1', 'PID_KP_0_1', 'PID_MIN_0_1', 'PID_MAX_0_1', 'PID_KP_1_1', 'PID_MIN_1_1', 'PID_MAX_1_1', 'PID_KP_2_1', 'PID_MIN_2_1', 'PID_MAX_2_1', 'FLOW_0_0_1', 'FLOW_0_1_1', 'FLOW_0_2_1', 'FLOW_0_3_1', 'FLOW_0_4_1', 'FLOW_1_0_1', 'FLOW_1_1_1', 'FLOW_1_2_1', 'FLOW_1_3_1', 'FLOW_1_4_1', 'FLOW_2_0_1', 'FLOW_2_1_1', 'FLOW_2_2_1', 'FLOW_2_3_1', 'FLOW_2_4_1', 'FLOW_JJQ_5', 'FLOW_ELS_2_5', 'FLOW_ELS_1_5', 'FLOW_ELS_0_5', 'SPEED_LZJ_5', 'PRE_ELS_2_5', 'PRE_ELS_1_5', 'PRE_ELS_0_5', 'TEM_JJQ_OUT_5', 'PEM_JJQ_IN_5', 'FLOW_2_4_4', 'FLOW_2_3_4', 'FLOW_2_2_4', 'FLOW_2_1_4', 'FLOW_2_0_4', 'FLOW_1_4_4', 'FLOW_1_3_4', 'FLOW_1_2_4', 'FLOW_1_1_4', 'FLOW_1_0_4', 'FLOW_0_4_4', 'FLOW_0_3_4', 'FLOW_0_2_4', 'FLOW_0_1_4', 'FLOW_0_0_4', 'PID_MAX_2_4', 'PID_MIN_2_4', 'PID_KP_2_4', 'PID_MAX_1_4', 'PID_MIN_1_4', 'PEM_JJQ_IN_2', 'TEM_JJQ_OUT_2', 'PRE_ELS_0_2', 'PRE_ELS_1_2', 'PRE_ELS_2_2', 'SPEED_LZJ_2', 'FLOW_ELS_0_2', 'FLOW_ELS_1_2', 'FLOW_ELS_2_2', 'FLOW_JJQ_2', 'KD_TJF_0_2', 'KD_TJF_1_2', 'KD_TJF_2_2', 'YYZ_LJG_ZT_2', 'YYZ_TDG_ZT_2', 'ELS_BSL_2', 'ELS_FP_BL_0_2', 'ELS_FP_BL_1_2', 'ELS_FP_BL_2_2', 'V_SP_0_2', 'V_SP_1_2', 'V_SP_2_2', 'ELS_KD_MAX_2', 'FPBC_A_2', 'FPBC_B_2', 'KD_0_0_2', 'KD_0_1_2', 'KD_0_2_2', 'KD_0_3_2', 'KD_0_4_2', 'KD_1_0_2', 'KD_1_1_2', 'KD_1_2_2', 'KD_1_3_2', 'KD_1_4_2', 'KD_2_0_2', 'KD_2_1_2', 'KD_2_2_2', 'KD_2_3_2', 'KD_2_4_2', 'PID_KP_0_2', 'PID_MIN_0_2', 'PID_MAX_0_2', 'PID_KP_1_2', 'PID_MIN_1_2', 'PID_MAX_1_2', 'PID_KP_2_2', 'PID_MIN_2_2', 'PID_MAX_2_2', 'FLOW_0_0_2', 'FLOW_0_1_2', 'FLOW_0_2_2', 'FLOW_0_3_2', 'FLOW_0_4_2', 'FLOW_1_0_2', 'FLOW_1_1_2', 'FLOW_1_2_2', 'FLOW_1_3_2', 'FLOW_1_4_2', 'FLOW_2_0_2', 'FLOW_2_1_2', 'FLOW_2_2_2', 'FLOW_2_3_2', 'FLOW_2_4_2', 'PID_KP_1_4', 'PID_MAX_0_4', 'PID_MIN_0_4', 'PID_KP_0_4', 'KD_2_4_4', 'KD_2_3_4', 'KD_2_2_4', 'KD_2_1_4', 'KD_2_0_4', 'KD_1_4_4', 'KD_1_3_4', 'KD_1_2_4', 'KD_1_1_4', 'KD_1_0_4', 'KD_0_4_4', 'KD_0_3_4', 'FLOW_2_3_5', 'KD_0_2_4', 'KD_0_1_4', 'KD_0_0_4', 'FPBC_B_4', 'FPBC_A_4', 'ELS_KD_MAX_4', 'V_SP_2_4', 'V_SP_1_4', 'V_SP_0_4', 'ELS_FP_BL_2_4', 'ELS_FP_BL_1_4', 'ELS_FP_BL_0_4', 'ELS_BSL_4', 'PEM_JJQ_IN_3', 'TEM_JJQ_OUT_3', 'PRE_ELS_0_3', 'PRE_ELS_1_3', 'PRE_ELS_2_3', 'SPEED_LZJ_3', 'FLOW_ELS_0_3', 'FLOW_ELS_1_3', 'FLOW_ELS_2_3', 'FLOW_JJQ_3', 'KD_TJF_0_3', 'KD_TJF_1_3', 'KD_TJF_2_3', 'YYZ_LJG_ZT_3', 'YYZ_TDG_ZT_3', 'ELS_BSL_3', 'ELS_FP_BL_0_3', 'ELS_FP_BL_1_3', 'ELS_FP_BL_2_3', 'V_SP_0_3', 'V_SP_1_3', 'V_SP_2_3', 'ELS_KD_MAX_3', 'FPBC_A_3', 'FPBC_B_3', 'KD_0_0_3', 'KD_0_1_3', 'KD_0_2_3', 'KD_0_3_3', 'KD_0_4_3', 'KD_1_0_3', 'KD_1_1_3', 'KD_1_2_3', 'KD_1_3_3', 'KD_1_4_3', 'KD_2_0_3', 'KD_2_1_3', 'KD_2_2_3', 'KD_2_3_3', 'KD_2_4_3', 'PID_KP_0_3', 'PID_MIN_0_3', 'PID_MAX_0_3', 'PID_KP_1_3', 'PID_MIN_1_3', 'PID_MAX_1_3', 'PID_KP_2_3', 'PID_MIN_2_3', 'PID_MAX_2_3', 'FLOW_0_0_3', 'FLOW_0_1_3', 'FLOW_0_2_3', 'FLOW_0_3_3', 'FLOW_0_4_3', 'FLOW_1_0_3', 'FLOW_1_1_3', 'FLOW_1_2_3', 'FLOW_1_3_3', 'FLOW_1_4_3', 'FLOW_2_0_3', 'FLOW_2_1_3', 'FLOW_2_2_3', 'FLOW_2_3_3', 'FLOW_2_4_3', 'YYZ_TDG_ZT_4', 'YYZ_LJG_ZT_4', 'KD_TJF_2_4', 'KD_TJF_1_4', 'KD_TJF_0_4', 'FLOW_JJQ_4', 'FLOW_ELS_2_4', 'FLOW_ELS_1_4', 'FLOW_ELS_0_4', 'SPEED_LZJ_4', 'PRE_ELS_2_4', 'PRE_ELS_1_4', 'PRE_ELS_0_4', 'TEM_JJQ_OUT_4', 'PEM_JJQ_IN_4', 'HQJ_YR_TIM_5', 'HQJ_YR_TIM_4', 'HQJ_YR_TIM_3', 'HQJ_YR_TIM_2', 'HQJ_YR_TIM_1', 'ZD_HSP_5', 'ZD_LSP_5', 'ZD_HSP_4', 'ZD_LSP_4', 'ZD_HSP_3', 'ZD_LSP_3', 'ZD_HSP_2', 'ZD_LSP_2', 'ZD_HSP_1', 'ZD_LSP_1', 'SBS_JS_YL', 'JJQ_JS_YL_6', 'JJQ_CS_WD_6', 'ELS_YL_0_6', 'ELS_YL_1_6', 'ELS_YL_2_6', 'SPEED_6', 'ELS_FLOW_0_6', 'ELS_FLOW_1_6', 'ELS_FLOW_2_6', 'JJQ_CS_FLOW_6', 'TJF_KD_0_6', 'TJF_KD_1_6', 'TJF_KD_2_6', 'YYZ_LJG_ZT_6', 'YYZ_TDG_ZT_6', 'ELS_BSL_6', 'ELS_BSL_0_6', 'ELS_BSL_1_6', 'ELS_BSL_2_6', 'V_SP_0', 'V_SP_1', 'V_SP_2', 'ELS_KD_MAX', 'FP_BC_A', 'FP_BC_B', 'KD_0_0', 'KD_0_1', 'KD_0_2', 'KD_0_3', 'KD_0_4', 'KD_1_0', 'KD_1_1', 'KD_1_2', 'KD_1_3', 'KD_1_4', 'KD_2_0', 'KD_2_1', 'KD_2_2', 'KD_2_3', 'KD_2_4', 'KP0', 'ELS_0_MIN', 'ELS_0_MAX', 'KP1', 'ELS_1_MIN', 'ELS_1_MAX', 'KP2', 'ELS_2_MIN', 'ELS_2_MAX', 'FLOW_0_0', 'FLOW_0_1', 'FLOW_0_2', 'FLOW_0_3', 'FLOW_0_4', 'FLOW_1_0', 'FLOW_1_1', 'FLOW_1_2', 'FLOW_1_3', 'FLOW_1_4', 'FLOW_2_0', 'FLOW_2_1', 'FLOW_2_2', 'FLOW_2_3', 'FLOW_2_4', 'SPEED_MIN_0', 'SPEED_MIN_1', 'SPEED_MIN_2', 'SPEED_MIN_0_5', 'SPEED_MIN_1_5', 'SPEED_MIN_2_5', 'SPEED_MIN_0_4', 'SPEED_MIN_1_4', 'SPEED_MIN_2_4', 'SPEED_MIN_1_3', 'SPEED_MIN_0_3', 'SPEED_MIN_2_3', 'SPEED_MIN_1_2', 'SPEED_MIN_2_2', 'YYJ_XXT_SET_3', 'SPEED_MIN_0_1', 'SPEED_MIN_1_1', 'SPEED_MIN_2_1', 'FAULT_LJJ_4', 'FAULT_CF_4', 'FAULT_SSGD_1_4', 'FAULT_SSGD_2_4', 'READY_SYD_4', 'READY_JZ_4', 'LJG_AUTO_4', 'TDG_AUTO_4', 'CF_RUN_4', 'FLOW_0_ALM_4', 'FLOW_1_ALM_4', 'FLOW_2_ALM_4', 'FAULT_SSGD_3_4', 'WATER_AUTO_START_4', 'PID_USE_4', 'FAULT_LJ_L_4', 'FAULT_LJ_H_4', 'FAULT_ZD_4', 'JZF_CLOSE_4', 'JZF_OPEN_4', 'ZT_FM_4', 'YDG_XC_L_4', 'YDG_XC_Z_4', 'YDG_XC_H_4', 'YDG_YK_JD_4', 'SHOW_KJ_4', 'LJJ_FANG_4', 'LJJ_ZHEN_4', 'CF_FANG_4', 'CF_ZHENG_4', 'PID_USE_3', 'WATER_AUTO_START_3', 'FAULT_SSGD_3_3', 'FLOW_2_ALM_3', 'FLOW_1_ALM_3', 'FLOW_0_ALM_3', 'CF_RUN_3', 'TDG_AUTO_3', 'LJG_AUTO_3', 'READY_JZ_3', 'READY_SYD_3', 'FAULT_SSGD_2_3', 'FAULT_SSGD_1_3', 'FAULT_LJJ_3', 'FAULT_LJ_L_3', 'FAULT_LJ_H_3', 'FAULT_ZD_3', 'JZF_CLOSE_3', 'JZF_OPEN_3', 'ZT_FM_3', 'YDG_XC_L_3', 'YDG_XC_Z_3', 'YDG_XC_H_3', 'YDG_YK_JD_3', 'SHOW_KJ_3', 'LJJ_FANG_3', 'LJJ_ZHEN_3', 'CF_FANG_3', 'CF_ZHENG_3', 'PID_USE_2', 'WATER_AUTO_START_2', 'FAULT_SSGD_3_2', 'FLOW_2_ALM_2', 'FLOW_1_ALM_2', 'FLOW_0_ALM_2', 'CF_RUN_2', 'TDG_AUTO_2', 'LJG_AUTO_2', 'READY_JZ_2', 'READY_SYD_2', 'FAULT_SSGD_2_2', 'FAULT_SSGD_1_2', 'FAULT_CF_2', 'FAULT_LJJ_2', 'FAULT_LJ_L_2', 'FAULT_LJ_H_2', 'FAULT_ZD_2', 'JZF_CLOSE_2', 'JZF_OPEN_2', 'CF_ZHENG_5', 'CF_FANG_5', 'LJJ_ZHEN_5', 'LJJ_FANG_5', 'SHOW_KJ_5', 'YDG_YK_JD_5', 'YDG_XC_H_5', 'YDG_XC_Z_5', 'YDG_XC_L_5', 'ZT_FM_5', 'JZF_OPEN_5', 'JZF_CLOSE_5', 'FAULT_ZD_5', 'FAULT_LJ_H_5', 'FAULT_LJ_L_5', 'FAULT_LJJ_5', 'FAULT_CF_5', 'FAULT_SSGD_1_5', 'FAULT_SSGD_2_5', 'READY_SYD_5', 'READY_JZ_5', 'LJG_AUTO_5', 'TDG_AUTO_5', 'CF_RUN_5', 'FLOW_0_ALM_5', 'FLOW_1_ALM_5', 'FLOW_2_ALM_5', 'FAULT_SSGD_3_5', 'WATER_AUTO_START_5', 'PID_USE_5', 'ZT_FM_2', 'YDG_XC_L_2', 'YDG_XC_Z_2', 'YDG_XC_H_2', 'YDG_YK_JD_2', 'SHOW_KJ_2', 'LJJ_FANG_2', 'LJJ_ZHEN_2', 'CF_FANG_2', 'CF_ZHENG_2', 'PID_USE_1', 'WATER_AUTO_START_1', 'FAULT_SSGD_3_1', 'FLOW_2_ALM_1', 'FLOW_1_ALM_1', 'FLOW_0_ALM_1', 'CF_RUN_1', 'TDG_AUTO_1', 'LJG_AUTO_1', 'READY_JZ_1', 'READY_SYD_1', 'FAULT_SSGD_2_1', 'FAULT_SSGD_1_1', 'FAULT_CF_1', 'FAULT_LJ_BP_1', 'FAULT_LJ_L_1', 'FAULT_LJ_H_1', 'FAULT_ZD_1', 'JZF_CLOSE_1', 'JZF_OPEN_1', 'ZT_FM_1', 'YDG_XC_L_1', 'YDG_XC_Z_1', 'YDG_XC_H_1', 'YDG_YK_JD_1', 'SHOW_KJ_1', 'LJJ_FANG_1', 'LJJ_ZHEN_1', 'CF_FANG_1', 'CF_ZHENG_1', 'YYB_RUN2', 'YYB_RUN1', 'YYZ_GY', 'YYZ_DY', 'ELFJ_RUN', 'XYF_GDW', 'XYF_KDW', 'ELS_XYF_AUTO', 'JJQ_JSYL_LOW', 'FAULT_YYB_2', 'FAULT_YYB_1', 'FAULT_ELS_FJ', 'FAULT_YGJ_1', 'FAULT_YGJ_2', 'FAULT_CPGD_2', 'FAULT_CPGD_1', 'FAULT_ZBC_2_2', 'FAULT_ZBC_2_1', 'FAULT_ZBC_1_2', 'FAULT_ZBC_1_1', 'FAULT_GBC', 'YYB_XYF_1', 'FAULT_CF_3', 'YYB_XYF_2', 'FAULT_ZBC_BP1', 'FAULT_ZBC_BP2', 'FAULT_ELS_FJ1', 'RUN_ELS_FJ1', 'FAULT_GBHZT', 'FAULT_ELS_FJ2', 'RUN_ELS_FJ2', 'FAULT_YYB_3', 'RUN_YYB_1', 'RUN_YYB_2', 'RUN_YYB_3', 'YYZ_YL_LOW', 'YYZ_YL_HIG', 'FAULT_CPGD_3', 'FAULT_CPGD_4', 'FAULT_TD_BP1', 'FAULT_SSGD_4_1', 'FAULT_TD_BP2', 'FAULT_SSGD_4_2', 'FAULT_TD_BP3', 'FAULT_SSGD_4_3', 'FAULT_TD_BP4', 'FAULT_SSGD_4_4', 'FAULT_TD_BP5', 'FAULT_SSGD_4_5', 'ADJUST_WATER_START', 'PID_USE_6', 'READY', 'RUNNING', 'Q_RESET', 'FAULT_INV', 'FWD_INV', 'REV_INV', 'RST_FAULT_INV', 'USE_INV', 'KJ_6', 'YDG_XC_S_6', 'YDG_XC_Z_6', 'YDG_XC_L_6', 'ELS_FM_ZD_6', 'ELS_JZF_KDW_6', 'ELS_JZF_GDW_6', 'YDG_ZSD_6', 'JZ_ZB_ZSD_6', 'LJG_AUTO_6', 'TDG_AUTO_6', 'PROJECT_ID']
    len_array=[]
    columns = [] #标签值
    ab = None
    dicttype = {}
    label_index=[]
    speed_lzj_5=[]
    next_speed_lzj_5 = []
    a_product=None
    b_product=None
    with client.read(hdfs_path=syspath, encoding='utf-8', delimiter='\n') as reader:
        for line in reader:
            if len(line.split(',')) not in len_array:
                len_array.append(len(line.split(',')))
            if a == 0:
               thesame = len(line.split(','))
               columns=line.split(',')
               ss = difflib.get_close_matches('SPEED_LZJ_',columns,9,cutoff=0.7)
               for s in range(len(ss)):

                   label_index.append(columns.index(ss[s]))

               print(label_index)
               # ab = np.concatenate((ab, line.split(',')))
               # ab=np.append(line.split(','))
               a = a+1
               continue
            elif len(line.split(',')) == thesame:
               speed_lzj_5.append(line.split(',')[label_index[0]])
               a = a+1

               # ab=np.concatenate((ab,line.split(',')),axis=0)
            elif len(line.split(',')) > thesame:
               b = b+1

               temp_array=[round(float(line.split(',')[label_index[0]]),2),round(float(line.split(',')[label_index[1]]),2),round(float(line.split(',')[label_index[2]]),2),round(float(line.split(',')[label_index[3]]),2),round(float(line.split(',')[label_index[4]]),2)]

               Unixtime = time.mktime(time.strptime(line.split(',')[0], '%Y-%m-%d %H:%M:%S.%f'))
               # print(Unixtime, round(float(line.split(',')[label_index[0]]),2))
               dicttype[str(Unixtime)]=temp_array
               # next_speed_lzj_5.append(line.split(',')[label_index[0]])
    print('a_product生产数据{0},b_product生产数据{1}'.format(a,b))
    print('总共有几个厂家{0}'.format(len_array))
    print(speed_lzj_5)
    # spe=np.array([e for e in next_speed_lzj_5 if e != 0]).astype(float)
    # print(spe.max())
    # print(spe.mean())
    # print(spe.min())
    # print(spe.sum())
    # print(next_speed_lzj_5)
    print(dicttype)
    df = pd.DataFrame(dicttype)
    df = pd.DataFrame(df.values.T,index=df.columns,columns=['SPEED5','SPEED4','SPEED3','SPEED2','SPEED1'])
    print('SPEED5={0} SPEED4={1} SPEED3={2} SPEED2={3} SPEED1={4}'.format(float('%.2f' % df['SPEED5'].mean()),df['SPEED4'].mean(),df['SPEED3'].mean(),df['SPEED2'].mean(),df['SPEED1'].mean()))
    print(df.loc['1574956789.0','SPEED5'])



def fiter_data():
    pass


if __name__ == '__main__':
    client = Client('http://master:50070')
    analyse_data('/data/2019-11-28/0')

