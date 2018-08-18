def get_prompt(prompt):
    data = input(prompt)
    return int(data)

# width = (get_input('Enter the width: '))
# height = (get_input('Enter the height: '))

def get_inputs():

    width = get_prompt('Enter the width: ')
    height = get_prompt('Enter the height: ')
    # 
    # width = int(input('Enter the width: '))
    # height = int(input('Enter the height: '))

    return(width, height)

def rectArea(width, height):
    area = width * height
    return area
# area = rectArea(width, height)


def rectPerimeter(width, height):
    perimeter = 2*(width + height)
    return perimeter
# perimeter = rectPerimeter(width, height)
def final_report(width, height, area, perimeter):
    print('A rectangle with dimension: width ', width, 'ft', ', height ', height, 'ft' )
    print('Has perimeter = ', perimeter, 'ft', ' and area ', area, 'sq ft' )

def main():
    # answer_area = rectArea(width, height)
    #
    # answer_peri = rectPerimeter(width, height)

    width, height = get_inputs()
    area = rectArea(width, height)
    perimeter = rectPerimeter(width, height)

    final_report(width, height, area, perimeter)
    # if __main__ == '__main__':
main()
