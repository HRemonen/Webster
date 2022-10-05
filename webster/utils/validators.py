import re

def ModeValidator(mode: str) -> bool:
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
    boolean
        True if mode of accepted type.
        
    """
    
    valid_modes = ["auto", "manual"]
    
    if mode in valid_modes:
        return True
    else: raise TypeError(
                    "Expected Mode type of string, instead got: "
                    , type(mode))

def URLValidator(url: list) -> bool:
    """
    Validates the URL or list of URLs
    
    Parameters
    ----------
    url : str | list
        Given URL or list of URLs

    Raises
    ------
    TypeError
        If URL is not of accepted form or not an valid URL.
    
    Returns
    -------
    bool
        True if URL of accepted form and False if it was not.
    """
    
    def _validate(input: str) -> bool:
        if not isinstance(input, str):
            raise TypeError(
                "Check input list content! Expected URL type of string, instead got: "
                , type(input))
            
        return bool(re.match(
            r"(https?|ftp)://"          # protocol
            r"(\w+(\-\w+)*\.)?"         # host (optional)
            r"((\w+(\-\w+)*)\.(\w+))"   # domain
            r"(\.\w+)*"                 # top-level domain (optional, can have > 1)
            r"([\w\-\._\~/]*)*(?<!\.)"  # path, params, anchors, etc. (optional)
        , input))
        
    if not isinstance(url, str):
        if not isinstance(url, list):
            raise TypeError(
                    "Expected URL type of list or string, instead got: "
                    , type(url))
        else:
            check = all([_validate(x) for x in url])       
    else: check = _validate(url)       
    if check:
        return check
    else:
        raise ValueError(
            "URL not of accepted form, please check form: ", url)  
