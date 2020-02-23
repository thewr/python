# Problem 3
# contact list
import csv

data = []
data.append(('Zoe', 'Z', 2323829323))
data.append(('Steven', 'S', 2328329535))


def add(name, nickname, phone):
    tup = (name, nickname, phone)
    count = 0
    for t in data:

        if t[0] == name:
            data[count] = tup
            return True
        count += 1
    data.append(tup)
    data.sort()
    return False


def remove(name):
    count = 0
    for t in data:
        tup = data[count]
        if t[0] == name:
            data.remove(tup)
            return True
        count += 1
    data.sort()
    return False


def find(name):
    ''' finds tupple ( t ) in contact list ( data ) '''
    for t in data:
        if (t[0] == name) or (t[1] == name):
            return t
    return None


myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]


def write_csv(filename):
    '''write newline without empty line'''
    obj_write = open(filename, 'w', newline= '')
    with obj_write:
        writer = csv.writer(obj_write)
        writer.writerows(data)

def read_csv(filename):
    obj_read = open(filename,'r')
    with obj_read:
        reader = csv.reader(obj_read)
        for line in reader:
            print(line)


def main():
    import csv
    add('Lodizal', 'Lodi', 2832839923)
    print('Adding "Lodizal":', data)
    add('Kyle', 'Ky', 7982329323)
    print('Adding "Kyle":', data, '\n')

    remove('Steven')
    print('After removing "Steven": ', data)
    print('Find "Steven": ', find('Steven'))
    print('Find "Ky": ', find('Ky'))

    write_csv('contacts.csv')
    read_csv('contacts.csv')



if __name__ == "__main__":
    main()

main()
