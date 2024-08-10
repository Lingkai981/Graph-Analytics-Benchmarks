import matplotlib.pyplot as plt
import numpy as np

fontsize = 40
def pr_vertical_scalability():
    # thread = 1 2 4 8 16 32
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+", "Ligra"]
    time_pr_standard_8 = {
        "GraphX": [       72, 51, 39, 19],
        "PowerGraph": [113, 75, 46, 38, 29, 22],
        "Flash": [97, 62, 33, 20, 13.7, 11.8],
        "Grape": [20.2, 9.7, 4.8, 2.4, 1.3, 0.8],
        "Pregel+": [195, 103, 55, 31, 19, 13],
        "Ligra": [14.9, 13.3, 11.4, 10.3, 9.65, 9.18]
    }
    time_pr_density_8 = {
        "GraphX": [       50, 37, 26, 13],
        "PowerGraph": [117.2, 76.2, 49.8, 31.4, 22.9, 15],
        "Flash": [43.02, 30.72, 16.28, 14.22, 11.55, 9.47],
        "Grape": [13.4, 7.0, 3.4, 1.9, 1.0, 0.5],
        "Pregel+": [192, 97, 51, 26, 15, 9],
        "Ligra": [12, 10.6, 8.65, 7.52, 6.95, 6.51]
    }
    time_pr_diameter_8 = {
        "GraphX": [       71, 53, 37, 20],
        "PowerGraph": [49, 40, 34.6, 32.7, 26.2, 22.2],
        "Flash": [96, 60, 32, 19, 13, 11],
        "Grape": [20.8, 9.8, 4.9, 2.4, 1.3, 0.8],
        "Pregel+": [253, 136, 58, 31, 18, 12],
        "Ligra": [15.2, 13.4, 12, 10.4, 9.86, 9.62]
    }
    marker = ['o', 'd', '^', 'p', 's', 'x']
    ms = [14, 14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-', '-']

    ymin = 0.2
    ymax = 800

    fig = plt.figure(figsize=(18, 5.5))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_pr_standard_8[system]), 6), time_pr_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_pr_standard_8[system]), 6), time_pr_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)
    plt.xlabel("#threads", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_pr_standard_8[system]), 6), time_pr_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)

    # plt.legend(loc='right', bbox_to_anchor=(1.8, 0.3))
    # plt.legend(loc='upper right', ncol=6, bbox_to_anchor=(1.0, 0.5))
    # fig.legend(loc='center', ncol=6, columnspacing=1, handletextpad=0.4, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("pr_vertical_scalability.pdf", bbox_inches='tight')
    plt.show()


def sssp_vertical_scalability():
    # threads = 1 2 4 8 16 32
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+", "Ligra"]
    time_sssp_standard_8 = {
        "GraphX": [   550, 398, 238, 149, 79],
        "PowerGraph": [30, 20, 12, 8, 7, 6],
        "Flash": [62, 41, 20, 14, 9, 6],
        "Grape": [17.3, 10.2, 5.3, 2.5, 1.2, 0.7],
        "Pregel+": [26.9, 16.9, 10.3, 5.8, 4.4, 3.0],
        "Ligra": [2.02, 1.38, 1.19, 1.05, 1.02, 1.02]

    }
    time_sssp_density_8 = {
        "GraphX": [    310, 169, 108, 76, 40],
        "PowerGraph": [23, 13, 8, 5, 4, 4],
        "Flash": [26, 13, 6.7, 3.9, 3.3, 3.1],
        "Grape": [8.4, 5.6, 2.9, 1.3, 0.7, 0.4],
        "Pregel+": [25.6, 13.8, 7.9, 4.6, 2.6, 2.2],
        "Ligra": [1.81, 1.67, 1.36, 1.19, 1.1, 0.75]
    }
    time_sssp_diameter_8 = {
        "GraphX": [    4800, 3493, 2219, 1307, 717],
        "PowerGraph": [25, 28.7, 28.5, 28, 29.1, 30.5],
        "Flash": [907, 611, 286, 223, 138, 88],
        "Grape": [24.6, 16.5, 8.4, 4.6, 2.5, 1.8],
        "Pregel+": [38, 19, 12, 9, 3, 4],
        "Ligra": [2.13, 1.42, 1.4, 1.39, 1.26, 1.16]
    }
    marker = ['o', 'd', '^', 'p', 's', 'x']
    ms = [14, 14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-', '-']

    fig = plt.figure(figsize=(18, 5.5))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_sssp_standard_8[system]), 6), time_sssp_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([0.15, 10000])
    plt.title("S8-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_sssp_density_8[system]), 6), time_sssp_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([0.15, 10000])
    plt.title("S8-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)
    plt.xlabel("#threads", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_sssp_diameter_8[system]), 6), time_sssp_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([0.15, 10000])
    plt.title("S8-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, handletextpad=0.4, bbox_to_anchor=(0.5, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("sssp_vertical_scalability.pdf")
    plt.show()


def tc_vertical_scalability():
    # threads = 1 2 4 8 16 32
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+", "Ligra"]
    time_tc_standard_8 = {
        "GraphX": [   ],
        "PowerGraph": [145.3, 82.4, 45.5, 27.4, 18.1, 13.6],
        "Flash": [163, 82, 44, 24, 14, 8],
        "Grape": [101, 53, 24, 10, 5, 2.7],
        "Pregel+": [201, 113, 56, 27, 14, 6],
        "Ligra": [24, 23.3, 23.6, 28.9, 27.7, 26.6]

    }
    time_tc_diameter_8 = {
        "GraphX": [],
        "PowerGraph": [136, 80, 45.1, 27.2, 17.4, 14.4],
        "Flash": [160, 82, 43, 22, 13, 8],
        "Grape": [88, 42, 21, 10, 5, 2],
        "Pregel+": [192, 116, 57, 28, 14, 6],
        "Ligra": [25.4, 25.3, 24.5, 24.2, 28.4, 28.5]
    }
    time_tc_density_8 = {
        "GraphX": [ ],
        "PowerGraph": [301, 168, 92, 51, 30, 28.6],
        "Flash": [313, 161, 82, 42, 22, 14],
        "Grape": [111, 56, 29, 14, 7, 4],
        "Pregel+": [300, 166, 80, 40, 19, 9],
        "Ligra": [59.2, 59.8, 63.5, 77.4, 73.3, 72.5]
    }

    marker = ['o', 'd', '^', 'p', 's', 'x']
    ms = [14, 14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-', '-']

    ymin = 1
    ymax = 500

    fig = plt.figure(figsize=(18, 5.5))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_tc_standard_8[system]), 6), time_tc_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_tc_density_8[system]), 6), time_tc_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)
    plt.xlabel("#threads", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(range(6 - len(time_tc_diameter_8[system]), 6), time_tc_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(6), ["1", "2", "4", "8", "16", "32"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, handletextpad=0.4, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("tc_vertical_scalability.pdf")
    plt.show()


def pr_horizontal_scalability():
    # machines = 1 2 4 8 16
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+"]
    time_pr_standard_8 = {
        "GraphX": [19, 17, 14, 12, 11],
        "PowerGraph": [22, 15, 14, 14, 42.2],
        "Flash": [11.5, 13.9, 14.7, 15.1, 18.9],
        "Grape": [0.79, 1.13, 0.95, 0.34, 0.50],
        "Pregel+": [12, 7.6, 3.3, 2.9, 2.9]
    }
    time_pr_density_8 = {
        "GraphX": [13, 10, 9, 9, 10],
        "PowerGraph": [15, 9.3, 12.4, 10.9, 34.1],
        "Flash": [9.5, 10.1, 11.2, 14.9, 19.3],
        "Grape": [0.53, 0.46, 0.39, 0.19, 0.19],
        "Pregel+": [9.6, 5.7, 2.9, 2.4, 3.9]
    }
    time_pr_diameter_8 = {
        "GraphX": [20, 19, 15, 13, 12],
        "PowerGraph": [22.2, 14.7, 15, 14.8, 40.5],
        "Flash": [11.8, 21.5, 21.8, 12.6, 14.3],
        "Grape": [0.85, 0.17, 0.10, 0.06, 0.05],
        "Pregel+": [13.4, 8.7, 5.7, 3.2, 6.8]
    }
    marker = ['o', 'd', '^', 'p', 's']
    ms = [14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-']

    ymin = 0.03
    ymax = 200

    fig = plt.figure(figsize=(18, 6))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_pr_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_pr_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)
    plt.xlabel("#machines", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_pr_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("pr_horizontal_scalability.pdf")
    plt.show()


def sssp_horizontal_scalability():
    # machines = 1 2 4 8 16
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+"]
    time_sssp_standard_8 = {
        "GraphX": [79, 59, 45, 42, 77],
        "PowerGraph": [6, 4.5, 4.4, 4.5, 18.2],
        "Flash": [6.63, 5.8, 5.81, 6.22, 11.8],
        "Grape": [0.73, 0.96, 0.77, 0.68, 0.54],
        "Pregel+": [4.87, 3.14, 2.57, 4.88, 13.7]

    }
    time_sssp_density_8 = {
        "GraphX": [40, 29, 28, 27, 44],
        "PowerGraph": [4, 3.6, 3.5, 3.5, 13.3],
        "Flash": [3.12, 2.8, 2.95, 4.22, 7.71],
        "Grape": [0.43, 0.38, 0.32, 0.23, 0.20],
        "Pregel+": [2.26, 1.46, 1.47, 4.28, 11.5]
    }
    time_sssp_diameter_8 = {
        "GraphX": [717, 530, 621, 1418, 4633],
        "PowerGraph": [30.5, 35.4, 46.4, 78.7, 307.3],
        "Flash": [88.7, 107.3, 88.6, 57.7, 111.8],
        "Grape": [1.85, 1.45, 1.05, 1.07, 0.96],
        "Pregel+": [4.45, 6.79, 11.39, 38.7, 100.7]
    }
    marker = ['o', 'd', '^', 'p', 's']
    ms = [14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-']

    fig = plt.figure(figsize=(18, 6))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_sssp_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([0.15, 10000])
    plt.title("S8-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_sssp_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([0.15, 10000])
    plt.title("S8-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)
    plt.xlabel("#machines", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_sssp_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([0.15, 10000])
    plt.title("S8-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("sssp_horizontal_scalability.pdf")
    plt.show()


def tc_horizontal_scalability():
    # machines = 1 2 4 8 16
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+"]
    time_tc_standard_8 = {
        "GraphX": [],
        "PowerGraph": [13.6, 9.3, 8.4, 6.7, 10.1],
        "Flash": [8.74, 7.15, 6.08, 4.73, 3.56],
        "Grape": [2.73, 2.06, 1.53, 1.40, 1.36],
        "Pregel+": [6.3, 3.1, 1.6, 1.01, 1.09]
    }
    time_tc_diameter_8 = {
        "GraphX": [],
        "PowerGraph": [14.4, 9.1, 7.8, 5.8, 9.3],
        "Flash": [8.85, 7.07, 6.27, 4.58, 3.65],
        "Grape": [2.97, 2.01, 1.62, 1.52, 1.45],
        "Pregel+": [6.51, 3.15, 1.69, 1.01, 1.12]
    }
    time_tc_density_8 = {
        "GraphX": [],
        "PowerGraph": [28.6, 15.9, 14.4, 8.6, 13.2],
        "Flash": [14.1, 10.5, 9.8, 8.3, 6.1],
        "Grape": [4.05, 2.39, 1.69, 1.35, 1.24],
        "Pregel+": [9.28, 4.72, 2.48, 1.45, 1.41]
    }
    marker = ['o', 'd', '^', 'p', 's']
    ms = [14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-']

    ymin = 0.5
    ymax = 50

    fig = plt.figure(figsize=(18, 6))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_tc_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_tc_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)
    plt.xlabel("#machines", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_tc_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S8-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("tc_horizontal_scalability.pdf")
    plt.show()


def pr_horizontal_scalability_9():
    # machines = 1 2 4 8 16
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+"]
    time_pr_standard_8 = {
        "GraphX": [None, None, 196,113,61],
        "PowerGraph": [149, 108.6, 66.1, 63.7, 73.6],
        "Flash": [99, 112, 147, 145, 144],
        "Grape": [13, 10, 8, 3, 2.4],
        "Pregel+": [127, 83, 63, 23, 22]
    }
    time_pr_diameter_8 = {
        "GraphX": [None, None, 204, 133, 66],
        "PowerGraph": [154, 113.8, 64.7, 63.4, 66.7],
        "Flash": [102, 116, 151, 150, 146],
        "Grape": [15, 10, 8, 3, 2.5],
        "Pregel+": [129, 83, 62, 23, 18]
    }
    time_pr_density_8 = {
        "GraphX": [None, None, 185, 75, 48],
        "PowerGraph": [93.9, 57.5, 44.4, 41.7, 59.2],
        "Flash": [61, 59, 86, 105, 123],
        "Grape": [13, 4.8, 2.8, 1.4, 1.1],
        "Pregel+": [104, 55, 35, 17, 10]
    }
    marker = ['o', 'd', '^', 'p', 's']
    ms = [14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-']

    ymin = 0.3
    ymax = 2000

    fig = plt.figure(figsize=(18, 5.5))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_pr_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_pr_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)
    plt.xlabel("#machines", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_pr_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("pr_horizontal_scalability_9.pdf")
    plt.show()


def sssp_horizontal_scalability_9():
    # machines = 1 2 4 8 16
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+"]
    time_sssp_standard_8 = {
        "GraphX": [None, None, 315, 176, 169],
        "PowerGraph": [32.2, 19.4, 14.1, 12, 18.5],
        "Flash": [62, 50, 58, 54, 60],
        "Grape": [10.7, 10.4, 8.0, 6.9, 6.1],
        "Pregel+": [28.1, 31.6, 11.5, 12.7, 18.6]
    }
    time_sssp_diameter_8 = {
        "GraphX": [None, None, ],
        "PowerGraph": [75, 50.9, 53.4, 92.8, 151.5],
        "Flash": [995, 692, 598, 477, 474],
        "Grape": [23.7, 66.7, 63.5, 54.9, 47.4],
        "Pregel+": [58.5, 25.6, 20.3, 14.4, 20.0]
    }
    time_sssp_density_8 = {
        "GraphX": [None, None, 236,219, 107],
        "PowerGraph": [20.7, 11.5, 9, 7.1, 16.2],
        "Flash": [32, 24, 25, 25, 30],
        "Grape": [6.7, 4.9, 3.6, 2.6, 2.0],
        "Pregel+": [23.9, 16.4, 8.2, 7.7, 14.3]
    }
    marker = ['o', 'd', '^', 'p', 's']
    ms = [14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-']

    ymin = 0.9
    ymax = 2000

    fig = plt.figure(figsize=(18, 5.5))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_sssp_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_sssp_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)
    plt.xlabel("#machines", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_sssp_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("sssp_horizontal_scalability_9.pdf")
    plt.show()


def tc_horizontal_scalability_9():
    # machines = 1 2 4 8 16
    systems = ["GraphX", "PowerGraph", "Flash", "Grape", "Pregel+"]
    time_tc_standard_8 = {
        "GraphX": [None, None, ],
        "PowerGraph": [],
        "Flash": [111, 72, 65, 47, 33],
        "Grape": [44, 29, 20, 15, 13],
        "Pregel+": [161, 42, 20, 11, 5]
    }
    time_tc_diameter_8 = {
        "GraphX": [None, None, ],
        "PowerGraph": [],
        "Flash": [165, 75, 66, 50, 34],
        "Grape": [54, 30, 20, 15, 13],
        "Pregel+": [199, 44, 21, 12, 5]
    }
    time_tc_density_8 = {
        "GraphX": [None, None, ],
        "PowerGraph": [],
        "Flash": [161, 105, 95, 81, 61],
        "Grape": [51, 29, 20, 14, 12],
        "Pregel+": [215, 60, 34, 33, 34]
    }
    marker = ['o', 'd', '^', 'p', 's']
    ms = [14, 14, 14, 14, 14]
    mfc = ['none', 'none', 'none', 'none', 'none']
    linestyle = ['-', '-', '-', '-', '-']

    ymin = 0.5
    ymax = 1800

    fig = plt.figure(figsize=(18, 5.5))
    plt.subplot(1, 3, 1)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_tc_standard_8[system], color='black', marker=marker[i], ms=ms[i], linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Std", fontsize=fontsize)
    plt.ylabel("Running Time (s)", fontsize=fontsize)
    plt.yscale("log")
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    plt.subplot(1, 3, 2)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_tc_density_8[system], color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Dense", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)
    plt.xlabel("#machines", fontsize=fontsize)

    plt.subplot(1, 3, 3)
    for i in range(len(systems)):
        system = systems[i]
        plt.plot(time_tc_diameter_8[system], label=system, color='black', marker=marker[i], ms=ms[i],
                 linestyle=linestyle[i], mfc=mfc[i])
    plt.ylim([ymin, ymax])
    plt.title("S9-Diam", fontsize=fontsize)
    plt.yscale("log")
    plt.yticks([], [])
    plt.xticks(range(5), ["1", "2", "4", "8", "16"], fontsize=fontsize-2)

    # fig.legend(loc='center', ncol=6, columnspacing=1, bbox_to_anchor=(0.53, 0.95), frameon=False)
    plt.tight_layout(pad=0.5)
    fig.subplots_adjust(top=0.88)
    plt.savefig("tc_horizontal_scalability_9.pdf")
    plt.show()

def dataset_sensitivity():
    # standard density diameter
    systems = ["GraphX", "PowerG", "Flash", "Grape", "Pregel+", "Ligra"]
    time = {
        "PageRank": {
            "GraphX": [19, 13, 20],
            "PowerG": [22, 15, 22.2],
            "Flash": [11.8, 9.47, 11.82],
            "Grape": [0.79, 0.53, 0.85],
            "Pregel+": [13.3, 9.5, 13.7],
            "Ligra": [9.18, 6.51, 9.62]
        },
        "SSSP": {
            "GraphX": [79, 40, 717],
            "PowerG": [6, 4, 30.5],
            "Flash": [6.63, 3.12, 88.76],
            "Grape": [0.73, 0.42, 1.85],
            "Pregel+": [3.05, 2.26, 10.90],
            "Ligra": [1.02, 0.755, 1.16]
        },
        "Connected\nComponent": {
            "GraphX": [47, 28, 192],
            "PowerG": [17, 12, 171],
            "Flash": [4.09, 2.64, 11.5],
            "Grape": [0.17, 0.14, 0.39],
            "Pregel+": [23, 12, 28],
            "Ligra": [0.462, 0.453, 0.479]
        },
        "Triangle\nCounting": {
            "GraphX": [137, 227, 147],
            "PowerG": [14.4, 30, 12.8],
            "Flash": [8.76, 14.13, 8.92],
            "Grape": [2.72, 4.05, 2.98],
            "Pregel+": [6.3, 9.2, 6.5],
            "Ligra": [26.6, 72.5, 28.5]
        },
        "Betweenness\nCentrality": {
            "GraphX": [99, 41, 1299],
            "PowerG": [15.2, 11.8, 72.5],
            "Flash": [2.07, 0.96, 3.59],
            "Grape": [0.54, 0.25, 0.57],
            "Pregel+": [0, 0, 0],
            "Ligra": [0.06, 0.0196, 0.0611]
        },
        "Label\nPropagation": {
            "GraphX": [974, 2096, 949],
            "PowerG": [199, 185, 133],
            "Flash": [46, 33, 65],
            "Grape": [3.84, 4.36, 2.54],
            "Pregel+": [0, 0, 0],
            "Ligra": [0, 0, 0]
        },
        "Core\nDecomposition": {
            "GraphX": [3600, 5040, 6600],
            "PowerG": [187, 291, 437],
            "Flash": [40, 37, 377],
            "Grape": [1.76, 2.2, 7.2],
            "Pregel+": [0, 0, 0],
            "Ligra": [6.66, 3.87, 7.32]
        },
        "k-Clique": {
            "GraphX": [0, 0, 0],
            "PowerG": [0, 0, 0],
            "Flash": [8.77, 16.12, 22.98],
            "Grape": [4.11, 6.14, 7.48],
            "Pregel+": [0, 0, 0],
            "Ligra": [0, 0, 0]
        }
    }
    color = ['black', 'dimgray', 'silver']
    dataset = ['S8-Std', 'S8-Dense', 'S8-Diam']
    scale = ['log', 'log', 'log', 'log', 'log', 'log', 'log', 'linear']
    save = ['PageRank', 'SSSP', 'Connected Component', 'Triangle Counting', 'Betweenness Centrality', 'Label Propagation', 'Core Decomposition', 'k-Clique']

    index = -1
    for algorithm in ['PageRank', 'SSSP', 'Connected\nComponent', 'Triangle\nCounting', 'Betweenness\nCentrality', 'Label\nPropagation', 'Core\nDecomposition', 'k-Clique']:
    # for algorithm in ['PageRank']:
        index = index + 1
        plt.figure(figsize=(18, 5))
        for i in range(len(systems)):
            system = systems[i]
            plt.bar(range(i * 5, i * 5 + 3), time[algorithm][system],
                    edgecolor='black', color=color, width=1)
        for i in range(3):
            plt.bar(i, time[algorithm]["GraphX"][i], edgecolor='black', color=color[i], label=dataset[i], width=1)

        # plt.title(algorithm, x=1.12, y=0.7, fontsize=36)
        plt.ylabel('Running Time (s)')
        plt.yscale(scale[index])
        # plt.ylim([0.1, 1000])
        plt.xticks(range(1, 27, 5), systems)
        # plt.legend(loc='right', bbox_to_anchor=(1.25, 0.2))
        plt.subplots_adjust(left=0.08, right=0.98, top=0.96)
        plt.savefig("algorithm-sensitivity-" + save[index] + '.pdf')
        plt.show()


def create_legend_image():
    color = ['dimgray', 'silver']
    dataset = ['S8-Diam', 'S9-Diam']

    fig, ax = plt.subplots(figsize=(12, 0.6))  # 你可以调整图像大小
    handles = [plt.Rectangle((0, 0), 1, 1, color=color[i]) for i in range(len(dataset))]
    legend = ax.legend(handles, dataset, loc='center', ncol=len(dataset), frameon=False)

    ax.add_artist(legend)
    ax.axis('off')  # 隐藏轴

    plt.savefig("legend_horizontal.pdf", bbox_inches='tight')
    plt.show()

def std_throughput():
    # standard density diameter
    systems = ["GraphX", "PowerG", "Flash", "Grape", "Pregel+"]
    time = {
        "PageRank": {
            "GraphX": [13636363, 0],
            "PowerG": [3554502, 20380430],
            "Flash": [7903055, 10366990],
            "Grape": [297980289, 624271683],
            "Pregel+": [51644427, 67831293]
        },
        "SSSP": {
            "GraphX": [1948051, 0],
            "PowerG": [8241758, 81081081],
            "Flash": [12711864, 24912805],
            "Grape": [273769088, 245547005],
            "Pregel+": [10888327, 80514398]
        },
        "Triangle\nCounting": {
            "GraphX": [1094890, 0],
            "PowerG": [14851485, 0],
            "Flash": [42134831, 44937088],
            "Grape": [110117459, 110898350],
            "Pregel+": [136915030, 256854850]
        }
    }
    color = ['dimgray', 'silver']
    dataset = ['S8-Std', 'S9-Std']
    scale = ['log', 'log', 'log']
    save = ['PageRank', 'SSSP','Triangle Counting']

    # bar_width = 0.35

    for index, algorithm in enumerate(['PageRank', 'SSSP', 'Triangle\nCounting']):
        plt.figure(figsize=(12, 4))
        for i in range(len(systems)):
            system = systems[i]
            plt.bar(range(i * 4, i * 4 + 2), time[algorithm][system],
                    edgecolor='black', color=color, width=1)
        for i in range(2):
            plt.bar(i, time[algorithm]["GraphX"][i], edgecolor='black', color=color[i], label=dataset[i], width=1)

        plt.ylabel('Throughput (Edges/s)')
        plt.yscale(scale[index])
        plt.xticks(np.arange(0.5, 0.5 + 4 * len(systems), 4), systems)
        plt.subplots_adjust(left=0.1, right=0.98, top=0.94)
        plt.savefig("stan8-throughput-" + save[index] + '.pdf')
        plt.show()

def dia_throughput():
    # standard density diameter
    systems = ["GraphX", "PowerG", "Flash", "Grape", "Pregel+"]
    time = {
        "PageRank": {
            "GraphX": [12500000, 0],
            "PowerG": [3703703, 22488750],
            "Flash": [10438413, 10220072],
            "Grape": [2730996814, 682601197],
            "Pregel+": [21828694, 82041512]
        },
        "SSSP": {
            "GraphX": [32376, 0],
            "PowerG": [488122, 9900990],
            "Flash": [1340602, 3161022],
            "Grape": [156200048, 31625953],
            "Pregel+": [1489122, 74654264]
        },
        "Triangle\nCounting": {
            "GraphX": [1020408, 0],
            "PowerG": [16129032, 0],
            "Flash": [41095890, 42930738],
            "Grape": [103336387, 109183019],
            "Pregel+": [133402346, 266949086]
        }
    }
    color = ['dimgray', 'silver']
    dataset = ['S8-Std', 'S9-Std']
    scale = ['log', 'log', 'log']
    save = ['PageRank', 'SSSP','Triangle Counting']

    # bar_width = 0.35

    for index, algorithm in enumerate(['PageRank', 'SSSP', 'Triangle\nCounting']):
        plt.figure(figsize=(12, 4))
        for i in range(len(systems)):
            system = systems[i]
            plt.bar(range(i * 4, i * 4 + 2), time[algorithm][system],
                    edgecolor='black', color=color, width=1)
        for i in range(2):
            plt.bar(i, time[algorithm]["GraphX"][i], edgecolor='black', color=color[i], label=dataset[i], width=1)

        plt.ylabel('Throughput (Edges/s)')
        plt.yscale(scale[index])
        plt.xticks(np.arange(0.5, 0.5 + 4 * len(systems), 4), systems)
        plt.subplots_adjust(left=0.1, right=0.98, top=0.94)
        plt.savefig("dia-throughput-" + save[index] + '.pdf')
        plt.show()

def den_throughput():
    # standard density diameter
    systems = ["GraphX", "PowerG", "Flash", "Grape", "Pregel+"]
    time = {
        "PageRank": {
            "GraphX": [15000000, 0],
            "PowerG": [4398826, 25337830],
            "Flash": [7755946, 12192148 ],
            "Grape": [771974246, 1288472625],
            "Pregel+": [37874971, 142506901]
        },
        "SSSP": {
            "GraphX": [3409090, 0],
            "PowerG": [11278195, 92592592],
            "Flash": [19455252 , 48859934 ],
            "Grape": [749861275, 736449332],
            "Pregel+": [12997965, 104647668]
        },
        "Triangle\nCounting": {
            "GraphX": [660792, 0],
            "PowerG": [11363636, 0],
            "Flash": [ 24590163, 24553936 ],
            "Grape": [120901441, 120779754],
            "Pregel+": [106006617, 44343163]
        }
    }
    color = ['dimgray', 'silver']
    dataset = ['S8-Std', 'S9-Std']
    scale = ['log', 'log', 'log']
    save = ['PageRank', 'SSSP','Triangle Counting']

    # bar_width = 0.35

    for index, algorithm in enumerate(['PageRank', 'SSSP', 'Triangle\nCounting']):
        plt.figure(figsize=(12, 4))
        for i in range(len(systems)):
            system = systems[i]
            plt.bar(range(i * 4, i * 4 + 2), time[algorithm][system],
                    edgecolor='black', color=color, width=1)
        for i in range(2):
            plt.bar(i, time[algorithm]["GraphX"][i], edgecolor='black', color=color[i], label=dataset[i], width=1)

        plt.ylabel('Throughput (Edges/s)')
        plt.yscale(scale[index])
        plt.xticks(np.arange(0.5, 0.5 + 4 * len(systems), 4), systems)
        plt.subplots_adjust(left=0.1, right=0.98, top=0.94)
        plt.savefig("den-throughput-" + save[index] + '.pdf')
        plt.show()

# create_legend_image()


plt.rcParams["font.size"] = 28
pr_vertical_scalability()
sssp_vertical_scalability()
tc_vertical_scalability()
# pr_horizontal_scalability()
# sssp_horizontal_scalability()
# tc_horizontal_scalability()
pr_horizontal_scalability_9()
sssp_horizontal_scalability_9()
tc_horizontal_scalability_9()

#



plt.rcParams["font.size"] = 26
# dataset_sensitivity()
# std_throughput()
# dia_throughput()
# den_throughput()
# create_legend_image()