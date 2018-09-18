import numpy as np
import pandas as pd
import time

np.random.seed(2) #reproductin

#global vari
N_States = 6
ACTIONS = ['left', 'right']
EPDILON = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13
FRESH_TIME = 0.3

def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),
        columns = actions,
    )
    #print(table)
    return table
#build_q_table(N_States, ACTIONS)

def choose_action(state, q_table):
    state_action = q_table.iloc[state, :]
    if (np.random.uniform() > EPDILON) or (state_action.all() == 0):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_action.argmax()
    return action_name

def get_env_feedback(S, A):

    if A == 'right': # move right
        if S == N_States - 2: #terminate
            S_ = 'terminal'
            R = 1

        else:
            S_ = S + 1
            R = 0
    else: #move left
        R = 0
        if S == 0:
            S_ = S #reach the wall
        else:
            S_ = S - 1
    return S_, R

# def update_env(S, episode, step_counter):
#     env_list = ['-']*[N_States - 1] + ['T']  #'------T' our environment
#     if S == 'terminal':
#         interaction = "Episode %s: total_steps = %s" % (episode + 1, step_counter)
#         #print('\r{}'.format(interaction), end='')
#         print(interaction)
#         time.sleep(2)
#         #print('\r                           ', end='')
#     else:
#         env_list = 'o'
#         interaction = ''.join(env_list)
#         print(interaction)
#         #print('\r'.format(interaction), end='')
#         time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_States, ACTIONS)
    print('start:{0}'.format(q_table))
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated =  False
        print('*'*50)
        print(episode)
        #update_env(S, episode, step_counter)
        while not is_terminated:
            print('-'*30)
            A = choose_action(S,q_table)
            S_, R =get_env_feedback(S, A)
            q_predict = q_table.ix[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.iloc[S_, :].max()
            else:
                q_target  = R
                is_terminated = True
            q_table.ix[S, A] += ALPHA * (q_target - q_predict)
            S = S_
            print('q_target : {0}     q_predict :{1}'.format(q_target, q_predict))
            step_counter += 1
            print('step :{0}   action :{1}   state :{2}\n'.format(step_counter, A, S))
            print(q_table)
            #update_env(S, episode, step_counter)

    return q_table

if __name__ == '__main__':
    print("Let's play the game!")
    q_table = rl()
   # print(q_table)
