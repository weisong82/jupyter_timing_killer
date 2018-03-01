# jupyter_timing_killer
根据设定的运行时间，清理jupyter notebook进程。 避免过多的note打开一直占用系统资源

# 测试环境： 
psutil  5.4.3 (在5.0.x版本后出现了psutil.process_iter函数的参数变化，会报错，建议升级版本或者修改代码 )
python3.6    

# 结合定时脚本，定期检查执行时间过长的进程，kill掉
0 */1 * * * python3 /root/jupyter_timing_killer.py
