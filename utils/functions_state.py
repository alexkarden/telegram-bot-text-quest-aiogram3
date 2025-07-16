import json


# ✅ State cache in memory
state_cache = {}

# ✅ Get state from cache or create a new state
def get_state(user_id):
    if user_id not in state_cache:
        # print(f"⚠️ State for user {user_id} not found — creating a new state.")
        reset_state(user_id)
    return state_cache[user_id]

def reset_state(user_id):
    """Полностью сбрасывает состояние пользователя к начальному"""
    state_cache[user_id] = {
        'gamepath':'',
        'chapter':''
    }
    return state_cache[user_id]

def set_state(user_id, gamepath, chapter):
    state_cache[user_id] ={
        'gamepath': gamepath,
        'chapter':chapter
    }
