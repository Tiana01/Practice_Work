import json
import numpy as np
import threading

from bsread.sender import sender

with sender(queue_size=10, port=1500) as stream:
    while True:
        for i in range(0 , 10):
            X = np.array([1, i, 3], dtype=np.int32)
            Y = np.array([4, 1, 2], dtype=np.int32)
            A = np.array([i, 8, 5], dtype=np.int32)
            B = np.array([4, 2, i], dtype=np.int32)

            stream.send(pulse_id=0, data={"CHA_1": X, "CHA_2": Y, "CHA_3": A , "CHA_4": B})

