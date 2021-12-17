import pandas as pd
import ipaddress
import os
import matplotlib.pyplot as plt
import numpy as np

def main():
    df = pd.read_csv('xxx/*.csv')

    df_bool = (df == 'TCP')
    tcp = df_bool.values.sum()

    df_bool = (df == 'UDP')
    udp = df_bool.values.sum()

    vc = df['Protocol'].value_counts()

    f = open('xxx/sample.txt','w')
    f.write('TCP:'+str(tcp)+' '+'UDP:'+str(udp)+' '+'protocal value'+str(vc))
    f.close()

    df = vc.plot(kind='bar')
    plt.yscale('log')
    df.set_xlabel('Protocol')
    df.set_ylabel('Numbers')
    plt.title('Figure1 Numbers of Protocols',c="darkred", size="large",y=-0.65)
    plt.savefig('figure.png')

if __name__ == "__main__":
    main()
    