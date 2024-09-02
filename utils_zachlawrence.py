''' ITERATION 1

Module: Stellar Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Millennium Group: Delivering Professional Insights For The Financial Markets'


#####################################
# Define a main() function for this module.
#####################################
def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
#####################################
# Define get_byline() function for this module.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
