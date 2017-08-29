# Problem_solved

## Contents

-  中文乱码处理

    添加zhfont = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/chinese/ukai.ttc')
    这个得自己下载放置一个目录下。然后，plt.title等的参数中指定fontproperties的值即可

-  给matplotlib.pyplot和seaborn形成的图形中添加注释

    ax = sns.countplot(general_info_df.PRESSURE, color=color[1])
    plt.title(u'', fontproperties=zhfont, fontsize=20)
    for i, p in enumerate(ax.patches):
        ratio = p.get_height()
        ano_str = '{}'.format(int(ratio))
        ax.annotate(ano_str, (p.get_x()+0.1, p.get_height()+80), fontproperties=zhfont, fontsize=20)

    plt.xticks((0,), (u'',), fontproperties=zhfont)
    plt.xlabel('')
    plt.ylabel(u'', fontproperties=zhfont, fontsize=18)

-