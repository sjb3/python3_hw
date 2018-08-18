# Sung Byun
# Take Home excercises: Slope

# After prompting for inputs by users, this program will calculate the slope and display

def get_prompt(prompt):
    """
        set prompting function separately to embrace the fx decompositioning
        Return: after prompting, numeric value in float will be returned
    """
    data = input(prompt)
    return float(data)

def get_inputs():
    """
        Adopting the function above for prompting,
        Returning, 2 sets of x- and y- coordinates
    """
    x_first = get_prompt('Please Enter the first x coordinate: ')
    y_first = get_prompt('Please Enter the first y coordinate: ')
    x_second = get_prompt('Please Enter the second x coordinate: ')
    y_second = get_prompt('Please Enter the second y coordinate: ')

    return (x_first, y_first,x_second, y_second)

def slope(x_first, x_second, y_first, y_second):
    """
        From the given inputs, slope will be calculated with slope function
        Return:
            the calculated value of slope
    """
    x_diff = (x_second - x_first)
    y_diff = (y_second - y_first)

    calc_slope = y_diff/x_diff
    return calc_slope

def final_report(x_first, x_second, y_first, y_second, calc_slope):
    """
        Solmne purpose for final report to end user
        Return:
            printed value of the results
    """
    print('Given points:', (x_first, y_first), 'and', (x_second, y_second))
    print('Slope = ', '{:,.1f}'.format(calc_slope))

def main():
    """
        aggregate above functions along with final reports for end users
    """
    x_first, y_first, x_second, y_second = get_inputs()
    calc_slope = slope(x_first, x_second, y_first, y_second)
    final_report(x_first, x_second, y_first, y_second, calc_slope)

if __name__ == '__main__':
    main()
