'''Module with functions for plotting'''
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def apply_labels(patches, axis, position="center"):
    '''Apply labels to a plot'''
    for patch in patches:
        height = patch.get_height()
        if position=="center":
            ypos = patch.get_y() + height / 2.
            va = "center"
        elif position=="top":
            ypos = patch.get_y() + 1.05*height
            va = "bottom"
        axis.text(patch.get_x() + patch.get_width()/2., ypos,
                    '%5.2f%%' % height,
                    ha='center', va=va)

def percentage_graph(data, axes):
    '''Make stacked bar graph of percentages'''
    years = list(data.index)
    pcts_a = axes.bar(range(len(data.A)), data.A,
                        align='center', color='green', label="A")
    pcts_b = axes.bar(range(len(data.B)), data.B,
                        align='center', color='yellow', bottom=data.A, label="B")
    pcts_c = axes.bar(range(len(data.C)), data.C,
                        align='center', color="red", bottom=data.A + data.B, label="C")


    apply_labels(pcts_a, axes)
    apply_labels(pcts_b, axes)
    apply_labels(pcts_c, axes, position="top")

    axes.set_ylim([0, 100])
    pctfmt = '%.0f%%'
    axes.yaxis.set_major_formatter(mtick.FormatStrFormatter(pctfmt))

    axes.set_xticks(range(len(data)))
    axes.set_xticklabels(years)

    axes.set_title("Pecentage of Restaurants Earning Each Grade", y=1.1)
    axes.legend(loc='upper left', bbox_to_anchor=(1, 1))

def bar_graph(data, axes):
    '''Make bar graph of counts'''

    data.plot(kind='bar', ax=axes)
    axes.set_title("Number of Restaurants Earning Each Grade", y=1)
