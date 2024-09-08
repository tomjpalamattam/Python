import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
from copy import deepcopy

# Define the DQN model
class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, action_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Define the DQN agent
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)  # Replay buffer
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        
        # Q-Network
        self.model = DQN(state_size, action_size)
        
        # Target Network
        self.target_model = DQN(state_size, action_size)
        self.update_target_model()  # Initialize target network with the same weights
        
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()

    # Method to synchronize the target network with the Q-network
    def update_target_model(self):
        self.target_model.load_state_dict(self.model.state_dict())

    # Store experiences in the replay buffer
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    # Select action using epsilon-greedy policy
    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = torch.FloatTensor(state).unsqueeze(0)
        act_values = self.model(state)
        return torch.argmax(act_values[0]).item()

    # Train the model using experiences from the replay buffer
def replay(self, batch_size):
    minibatch = random.sample(self.memory, batch_size)
    for state, action, reward, next_state, done in minibatch:
        state = torch.FloatTensor(state).unsqueeze(0)
        next_state = torch.FloatTensor(next_state).unsqueeze(0)
        
        # Compute the target Q-value
        target = reward
        if not done:
            # Use the target network to calculate the target Q-value
            target = reward + self.gamma * torch.max(self.target_model(next_state)[0]).item()

        # Predicted Q-values from the Q-network
        target_f = self.model(state)
        target_f[0][action] = target  # Set the target for the selected action
        
        # Train the Q-network
        self.optimizer.zero_grad()
        loss = self.criterion(target_f, self.model(state))
        loss.backward()
        self.optimizer.step()
    
    # Decay epsilon for exploration
    if self.epsilon > self.epsilon_min:
        self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_state_dict(torch.load(name))

    def save(self, name):
        torch.save(self.model.state_dict(), name)

# Environment class for UI adaptation
class UIEnvironment:
    def __init__(self, initial_state, adaptations, oracle):
        self.initial_state = initial_state
        self.adaptations = adaptations
        self.oracle = oracle
        self.current_state = initial_state

    def reset(self):
        self.current_state = deepcopy(self.initial_state)
        return self.state_to_vector(self.current_state)

    def step(self, action):
        adaptation = self.adaptations[action]
        next_state = self.apply_adaptation(self.current_state, adaptation)
        reward = self.oracle.get_individual_rewards(next_state.ui_elements_grid_state, self.current_state.ui_elements_grid_state, next_state.freqdist)[0]
        done = self.is_terminal(next_state)
        self.current_state = next_state
        return self.state_to_vector(next_state), sum(reward), done, {}

    def state_to_vector(self, state):
        return state.ui_elements_grid_state.flatten()

    def apply_adaptation(self, state, adaptation):
        grid, history = state.ui_elements_grid_state, state.indexed_history
        new_grid = self.adaptations.apply_bbox_swap_adaptation_mcts(adaptation)
        freqdist, new_history = update_hist(history, new_grid)
        self.utilities.ui_elements_grid, self.utilities.indexed_history, self.utilities.freqdist = deepcopy(new_grid), deepcopy(new_history), deepcopy(freqdist)

        previous_seen_state = State(
            indexed_history=state.indexed_history.copy(),
            freqdist=state.freqdist.copy(),
            ui_elements_grid=state.ui_elements_grid_state.copy(),
            association_matrix=state.association_matrix.copy() if state.association_matrix is not None else None,
            depth=state.depth,
            previous_seen_state=None,
            exposed=state.exposed
        )
        new_state = deepcopy(state)
        new_state.previous_seen_state = previous_seen_state
        new_state.ui_elements_grid_state = deepcopy(new_grid)
        new_state.indexed_history = deepcopy(new_history)
        new_state.freqdist = deepcopy(freqdist)
        new_state.association_matrix = deepcopy(self.utilities.get_association_matrix())
        new_state.depth += 1

        self.adaptations.menustate.grid = deepcopy(new_grid)
        activations = self.utilities.get_activations(new_history, session_interval=50, duration_between_clicks=30)
        self.oracle.activations = deepcopy(activations)
        return new_state

    def is_terminal(self, state):
        return state.depth >= self.oracle.maxdepth

# Training the DQN agent
env = UIEnvironment(initial_state, adaptations, oracle)
state_size = env.state_to_vector(initial_state).shape[0]
action_size = len(adaptations)

agent = DQNAgent(state_size, action_size)

# Training the DQN agent
episodes = 1000
target_update_frequency = 10  # Update the target network every 10 episodes

for e in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    total_reward = 0
    for time in range(10):  # Adjust the number of steps as needed
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        if done:
            break
    
    # Train the Q-network
    if len(agent.memory) > 32:
        agent.replay(32)
    
    # Update the target network every 'target_update_frequency' episodes
    if e % target_update_frequency == 0:
        agent.update_target_model()
    
    print(f"episode: {e}/{episodes}, total reward: {total_reward}, e: {agent.epsilon:.2f}")
    
    

# Extracting the best sequence of adaptations
def get_best_sequence(env, agent, initial_state, sequence_length=10):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    best_sequence = []
    for _ in range(sequence_length):
        action = agent.act(state)
        best_sequence.append(action)
        next_state, reward, done,

```python
# Extracting the best sequence of adaptations
def get_best_sequence(env, agent, initial_state, sequence_length=10):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    best_sequence = []
    for _ in range(sequence_length):
        action = agent.act(state)
        best_sequence.append(action)
        next_state, reward, done, _ = env.step(action)
        state = np.reshape(next_state, [1, state_size])
        if done:
            break
    return best_sequence

best_sequence = get_best_sequence(env, agent, initial_state)
print("Best sequence of adaptations:", best_sequence)
