import matplotlib
import matplotlib.pyplot as plt
import time
timestr = time.strftime("%Y%m%d-%H%M")

episode_rewards = []
loss_history = []

def plot_reward(reward):
    plt.figure('Reward graph [FlappyBird A3C]')
    plt.clf()
    episode_rewards.append(reward)
    plt.title('Mean Reward')
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.plot(episode_rewards)
    plt.legend(loc='upper left')
    plt.pause(0.001)  # pause a bit so that plots are updated
    plt.savefig('plots/reward/reward_graph@' + timestr)

def plot_loss(loss):
    plt.figure('Loss graph [FlappyBird A3C]')
    plt.clf()
    loss_history.append(loss)
    plt.title('Mean Loss')
    plt.xlabel('Episode')
    plt.ylabel('Loss')
    plt.plot(loss_history, color= 'red')
    plt.legend(loc='upper left')
    plt.pause(0.001)  # pause a bit so that plots are updated
    plt.savefig('plots/loss/loss_graph@' + timestr)
