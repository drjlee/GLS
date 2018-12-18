def main2(gpf_num, gpm_num, fs_num, ms_num, fc_num, mc_num, sib_num):
    totalNum = gpf_num + fs_num + fc_num + gpm_num + ms_num + mc_num + sib_num
    distanceMatrix = np.eye(totalNum)
    start_num = 0
    item_column_num_dict = {}
    for item in ['gpf_num', 'gpm_num', 'fs_num', 'ms_num', 'fc_num', 'mc_num', 'sib_num']:
        num = eval(item)
        end_num = start_num + num
        item_column_num_dict[item] = range(start_num, end_num)
        start_num = start_num + num
        
    siblings = ['fs_num', 'ms_num', 'sib_num', 'fc_num', 'mc_num']
    for sibling in siblings:
        cols = item_column_num_dict[sibling]
        distanceMatrix[np.ix_(cols,cols)] = .5
        
        distanceMatrix[np.ix_(item_column_num_dict['gpf_num'], 
                    item_column_num_dict['fs_num'])] = .5

    distanceMatrix[np.ix_(item_column_num_dict['gpf_num'],
                   item_column_num_dict['fc_num'])] = .25

    distanceMatrix[np.ix_(item_column_num_dict['gpf_num'],
                   item_column_num_dict['sib_num'])] = .25

    '''mother side grand father'''
    distanceMatrix[np.ix_(item_column_num_dict['gpm_num'], 
                    item_column_num_dict['ms_num'])] = .5

    distanceMatrix[np.ix_(item_column_num_dict['gpm_num'],
                   item_column_num_dict['mc_num'])] = .25

    distanceMatrix[np.ix_(item_column_num_dict['gpm_num'],
                   item_column_num_dict['sib_num'])] = .25

    '''Father siblings'''
    distanceMatrix[np.ix_(item_column_num_dict['fs_num'],
                   item_column_num_dict['fc_num'])] = .5

    distanceMatrix[np.ix_(item_column_num_dict['fs_num'],
                   item_column_num_dict['sib_num'])] = .25

    distanceMatrix[np.ix_(item_column_num_dict['ms_num'],
                   item_column_num_dict['mc_num'])] = .5

    distanceMatrix[np.ix_(item_column_num_dict['ms_num'],
                   item_column_num_dict['sib_num'])] = .25

    '''Father cousins'''
    distanceMatrix[np.ix_(item_column_num_dict['fc_num'],
                   item_column_num_dict['sib_num'])] = .25

    '''Mother cousins'''
    distanceMatrix[np.ix_(item_column_num_dict['mc_num'],
                   item_column_num_dict['sib_num'])] = .25

    '''parent mark'''
    distanceMatrix[np.ix_([item_column_num_dict['fs_num'][-1], 
                           item_column_num_dict['ms_num'][0]],
                   item_column_num_dict['sib_num'])] = .5

    distanceMatrix[range(totalNum),range(totalNum)] = 1

    
    R = np.triu(distanceMatrix) + np.triu(distanceMatrix).T - np.eye(distanceMatrix.shape[0])
    distanceDf = pd.DataFrame(R)
    print(distanceDf)

    V = R * 0.7 
    V[V==0.7] = 1

    print(pd.DataFrame(V))

    print('-------------------------------')
    print('Total family number :', totalNum)
    print('-------------------------------')
    print(gpf_num, gpm_num, fs_num, ms_num, fc_num, mc_num, sib_num)
    print('Grand parents (father side) :', len(item_column_num_dict['gpf_num']))
    print('Grand parents (mother side) :', len(item_column_num_dict['gpm_num']))
    print('Father siblings :', len(item_column_num_dict['fs_num']))
    print('Mother siblings :', len(item_column_num_dict['ms_num']))
    print('Cousins (father side) :', len(item_column_num_dict['fc_num']))
    print('Cousins (mother side) :', len(item_column_num_dict['mc_num']))
    print('Siblings :', len(item_column_num_dict['sib_num'])) #should be 'sib_num'

    L_input = input('L ? :').split(' ')

    L = np.matrix([float(x) for x in L_input]).T
    print(len(L))
    L[L==1] = 2.78
    L[L==0] = -0.08
    print(pd.DataFrame(L))
    
    g =  R * ((np.linalg.inv(V)) * L)
    print(pd.DataFrame(g))
