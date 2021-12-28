使用说明：
1.在全局变量处设置需要回测的时间区间，以及指定数据调仓频率，即可输出结果。
if __name__ == '__main__':
    # 指定回测区间：
    startdate = '2013-12-31'
    enddate = '2021-1-29'
    
    #用户自己指定回测的调仓频率：'Q'代表季度，'M'代表月度，'Y'代表年度
    period = 'M'
    main()
strategy_cycle_change(startdate,enddate,period)
