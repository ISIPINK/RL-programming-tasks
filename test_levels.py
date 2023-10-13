import gym
# trivial case with no holes: expected rew should approach 1


def envrandom():
    return gym.make("FrozenLake8x8-v1", desc=None, map_name=None, is_slippery=True)


def trivial():
    return gym.make("FrozenLake8x8-v1", desc=[
        "SFFFFFFF",
        "FFFHFFFF",
        "FFHFFFFF",
        "FFFFFFFF",
        "FFFFFFFF",
        "FFFFFFFF",
        "FFFFFFFF",
        "FFFFFFFG",
    ], map_name=None, is_slippery=True)


def time_level():
    return gym.make("FrozenLake8x8-v1", desc=[
        "SFFFFFFH",
        "FFHHHFHF",
        "FHFFFFFF",
        "FHFFFFFF",
        "FHFFHFFF",
        "FHFFHFFF",
        "FHFFHFFF",
        "FFFFHFFG",
    ], map_name=None, is_slippery=True)
