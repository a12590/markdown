# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize =(8,6),dpi = 80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(111)

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,4,9,endpoint = True))

#给一些特殊点做标记
annotate



