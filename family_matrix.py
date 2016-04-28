import numpy as np
import pandas as pd
import sys
np.set_printoptions(suppress=True)
np.set_printoptions(precision=4)
pd.set_option('max_rows', 5000)
pd.set_option('max_columns', 5000)

def main2(gpf_num, gpm_num, fs_num, ms_num, fc_num, mc_num, sib_num):

    '''
    1. level marking
    - make a identity matrix
    - mark which level they are into
        - m_level 2 ~ 3
        - f_level 2 ~ 3
        - level 1 

    '''
    totalNum = gpf_num + fs_num + fc_num + gpm_num + ms_num + mc_num + sib_num
    distanceMatrix = np.eye(totalNum)
    #distanceMatrix = np.array(totalNum*totalNum*[1]).reshape(totalNum,totalNum)

    
    start_num = 0
    item_column_num_dict = {}
    for item in [ 'gpf_num', 'gpm_num', 'fs_num', 'ms_num', 'fc_num', 'mc_num', 'sib_num' ]:
        num = eval(item)
        print item, num, 'people'
        end_num = start_num + num
        item_column_num_dict[item] = range(start_num, end_num)
        start_num = start_num + num

    #print item_column_num_dict


    '''
    mark parent
    '''
    #item_column_num_dict['parent'] = [item_column_num_dict['fs_num'][0], item_column_num_dict['ms_num'][0]]



    '''
    2. sibling mark
    '''
    siblings = ['fs_num','ms_num','sib_num', 'fc_num', 'mc_num']
    for sibling in siblings:
        try:
            #cols = [x+1 for x in item_column_num_dict[sibling]]
            cols = item_column_num_dict[sibling]
            #print sibling, cols
            distanceMatrix[np.ix_(cols,cols)] = .5
                    
                    #cols[0]:cols[-1] + 1, 
                           #cols[0]:cols[-1] + 1] = .5
        except:
            pass


    '''
    3. children mark
    # father side grand father
    '''
    try:
        distanceMatrix[np.ix_(item_column_num_dict['gpf_num'], 
                        item_column_num_dict['fs_num'])] = .5

        distanceMatrix[np.ix_(item_column_num_dict['gpf_num'],
                       item_column_num_dict['fc_num'])] = .25

        distanceMatrix[np.ix_(item_column_num_dict['gpf_num'],
                       item_column_num_dict['sib_num'])] = .25
    except:
        pass
        print 'error'

    '''
    # mother side grand father
    '''
    try:
        distanceMatrix[np.ix_(item_column_num_dict['gpm_num'], 
                        item_column_num_dict['ms_num'])] = .5

        distanceMatrix[np.ix_(item_column_num_dict['gpm_num'],
                       item_column_num_dict['mc_num'])] = .25

        distanceMatrix[np.ix_(item_column_num_dict['gpm_num'],
                       item_column_num_dict['sib_num'])] = .25
    except:
        pass
        print 'error'


    '''## Father siblings'''
    try:
        distanceMatrix[np.ix_(item_column_num_dict['fs_num'],
                       item_column_num_dict['fc_num'])] = .5

        distanceMatrix[np.ix_(item_column_num_dict['fs_num'],
                       item_column_num_dict['sib_num'])] = .25
    except:
        pass
        print 'error'

    '''## Mother siblings'''
    try:
        distanceMatrix[np.ix_(item_column_num_dict['ms_num'],
                       item_column_num_dict['mc_num'])] = .5

        distanceMatrix[np.ix_(item_column_num_dict['ms_num'],
                       item_column_num_dict['sib_num'])] = .25
    except:
        pass


    # Father cousins
    try:
        distanceMatrix[np.ix_(item_column_num_dict['fc_num'],
                       item_column_num_dict['sib_num'])] = .25
    except:
        pass

    # Mother cousins
    try:
        distanceMatrix[np.ix_(item_column_num_dict['mc_num'],
                       item_column_num_dict['sib_num'])] = .25
    except:
        pass

    '''
    parent mark
    '''
    try:
        distanceMatrix[np.ix_([item_column_num_dict['fs_num'][-1], 
                               item_column_num_dict['ms_num'][0]],
                       item_column_num_dict['sib_num'])] = .5
        #distanceMatrix[np.ix_([4, 
                               #14],
                       #item_column_num_dict['sib_num'])] = .5
    except:
        pass

    #'''
    #different side
    #'''
    ## Father and mother side
    #try:
        #distance[item_column_num_dict['fs_num'],
                 #item_column_num_dict['ms_num']] = 0
    #except:
        #pass

    ## Father side cousins and mother side cousins
    #try:
        #distance[item_column_num_dict['fc_num'],
                 #item_column_num_dict['mc_num']] = 0
    #except:
        #pass




    distanceMatrix[range(totalNum),range(totalNum)] = 1

    
    R = np.triu(distanceMatrix) + np.triu(distanceMatrix).T - np.eye(distanceMatrix.shape[0])
    distanceDf = pd.DataFrame(R)
    print distanceDf

    V = R * 0.7 
    V[V==0.7] = 1

    print pd.DataFrame(V)

    L_input = raw_input('L ? :').split(' ')
    L = np.matrix([float(x) for x in L_input]).T
    L[L==1] = 2.78
    L[L==0] = -0.08
    print pd.DataFrame(L)
    
    g =  R * ((np.linalg.inv(V)) * L)
    #g =  R * (np.linalg.inv(V)) * L
    print pd.DataFrame(g)

    # create family degree matrix
    



if __name__=='__main__':
    #main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    main2(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))

