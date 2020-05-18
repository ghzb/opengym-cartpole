import os, sys
def get(agent, env):
    return getattr(__import__('.'.join(['agents', agent]), fromlist=['.'.join([agent, agent])]), agent)(env)
