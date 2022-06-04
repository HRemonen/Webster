import queue

def validate_mode(mode: str) -> str:
    """
    Validates the passed mode type
    
    Parameters
    ----------
    mode : str
        Given mode. Valid modes are: "manual".    

    Raises
    ------
    TypeError
        If mode is not a valid mode.
    
    Returns
    -------
    string
        mode provided as argument is returned as valid mode.
        
    """
    valid_modes = ["manual"]
    if mode in valid_modes:
        return mode
    else: raise TypeError(f"mode type {mode} not understood")

def validate_queue(userQueue: object) -> object:
    """
    Validates the passed queue
    
    Parameters
    ----------
    userQueue : object
        Given queue. 

    Raises
    ------
    TypeError
        If queue is not a valid object.
    
    Returns
    -------
    object
        queue provided as argument is returned as valid queue.
        
    """
    if isinstance(userQueue, queue):
        return userQueue
    else: raise TypeError(f"mode type {userQueue} not understood")