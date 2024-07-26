import one

print("two.py TOP level")
one.func()

if __name__=='__main__':
    print("two.py run directly")
else:
    print("two.py has beed imported")