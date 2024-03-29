def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    data=[line for line in data]
    return data

def part1(data):
    sum = 0
    for line in data:
        digits = [int(c) for c in line if c.isdigit()]
        if len(digits) != 0:
            sum += digits[0]*10 + digits[-1]
    return sum

def part2(data):
    sum = 0
    spelled_out = { 'one':'1', 'two':'2', 'three':'3',
                    'four':'4','five':'5','six':'6',
                    'seven':'7', 'eight':'8', 'nine':'9'}
    for line in data:
        digits = []
        for idx, c in enumerate(line):
            line = line + 'qqqq'
            if c.isdigit():
                digits.append(int(c))
            else:
                for key in spelled_out.keys():
                    test = line[idx: idx+len(key)]
                    if  test == key:
                        digits.append(int(spelled_out[key]))
                

        print(digits[0]*10 + digits[-1])
        sum += digits[0]*10 + digits[-1]        
    return sum

if __name__ == "__main__":
    data=readAndFormatData('day1.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')