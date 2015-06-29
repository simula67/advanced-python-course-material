__author__ = 'antonjoj'

# Create a center function

def print_n_times( char, n):
    print char * n,

def center( content, width, fill):
    right_n_times = (width - len(content)) / 2
    left_n_times = right_n_times
    if width % 2 == 1:
        left_n_times += 1
    print_n_times(fill,left_n_times)
    print content,
    print_n_times(fill,right_n_times)

center('perl', 9, '-')