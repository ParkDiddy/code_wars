# takes seconds and returns hh:mm::ss format to make readable
def make_readable(seconds):
    return f"{seconds // 3600 :02d}:{seconds // 60 % 60 :02d}:{seconds % 60 :02d}"

print(make_readable(3661))