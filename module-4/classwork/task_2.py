def func(lenght, direction, symbol):
    if direction  == "horizontal":
        print(symbol * lenght)
    if direction == "vertical":
        for lenght in range(lenght):
            print(symbol)

func(6, 'horizontal', '#')
func(4, 'vertical', '&')