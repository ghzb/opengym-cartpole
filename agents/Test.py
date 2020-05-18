class Test():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print ("Action size %s" % self.action_size)
        # self.state = env.reset()
        

    def handle_pole(self, state):
        angle = state[2]
        if angle > 0:
            self.action = 1

    def get_action(self, state):
        self.action = 0
        self.handle_pole(state)
        return self.action