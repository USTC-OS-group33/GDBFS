# MATLAB 文件说明文档
由于我们使用 MATLAB 进行算法的调试与测试，因此我们也将 MATLAB 代码上传。
下面是这部分代码的使用说明：
* 将全部文件下载到一个文件夹后，打开`learning.m`脚本，如有需要，可在开头更改参数。如学习率，最大节点集等等。
* 运行`learning.m`脚本，会提示输入序号。此时按顺序输入以整数表示对节点序列。输完后直接`control+c`退出脚本运行，得到三种不同算法的每一步的预测效果值。（这里的具体意义请参见`./Report&ppt/详细设计报告.pdf`）
* 调用函数计算预测效果参数值 $ \sigma $ 并绘制效果折线图：
```
[y_mm, y_vmm, y_voting]=generate_curve(eff_MM,eff_VMM,eff_vote)
plot(y_mm)
hold on
plot(y_vmm)
plot(y_voting)
```