# jupyter_timing_killer
根据设定的运行时间，清理jupyter notebook进程。 避免过多的note打开一直占用系统资源

# 测试环境： 
psutil  5.4.3 (在5.0.x版本后出现了psutil.process_iter函数的参数变化，会报错，建议升级版本或者修改代码 )
python3.6    

# 结合定时脚本，定期检查执行时间过长的进程，kill掉
0 */1 * * * python3 /root/jupyter_timing_killer.py

# notice:
notebook进程是由jupyter-notebook 母进程所派生。 所以结束任何一个notebook进程之后，会再次被拉起一个新进程。 进程数是不会减少的。

但是，随着一次kill，notebook上次运行的堆栈和对象信息，会被清零。 比如spark脚本读入的DF，创建的application，都会得到释放。
