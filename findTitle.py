def findTitle(title_str, titles = corrMat.columns, where = 'middle'):
    '''
    To look at the top 15 for a specific show, the show name must be inputted 
    correctly. This may be difficult because the names are Romanized versions 
    of the Japanese name. If one know part of a show name, this function will
    give all titles that contain that part so users can find the exact title
    name.
    
    titles is a list of all the titles of interest
    
    title_str is a string argument that is part of the title that is trying to
              be searched
    
    where is where in the title the string is located.
          The inputs for where are 'start', 'middle', or 'end'.
          Default is 'start'
    '''
    import re
    if where == 'start':
        reg_exp_str = r'^' + title_str + '.*$'
        pattern = re.compile(reg_exp_str)
        matches = [x for x in titles if pattern.match(x)]
    elif where == 'middle':
        reg_exp_str = r'^.*' + title_str + '.*$'
        pattern = re.compile(reg_exp_str)
        matches = [x for x in titles if pattern.match(x)]
    elif where == 'end':
        reg_exp_str = r'^.*' + title_str + '$'
        pattern = re.compile(reg_exp_str)
        matches = [x for x in titles if pattern.match(x)]
    return matches
