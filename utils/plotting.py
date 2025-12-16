import matplotlib.pyplot as plt

def plot_learining_curve(rewards, window=50):
    if len(rewards) >= window:
        rewards = rewards[-window]

    plt.plot(rewards)
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.show()
