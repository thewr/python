"""
Class called NVector that is an N-dimensional vector of real numbers
"""


# Constructor
class NVector:
    def __init__(self, *data):
        new_data = data
        self.data = new_data

    def to_string(self):
            print(self.data)

    def __len__(self):
        vlen = 0
        for key in self.data:
            vlen += 1
        return vlen

    def __getitem__(self, index):
        result = self.data[index]
        return result

    def __setitem__(self, index, value):
        self.data[index] = value

    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

    def __add__(self, other):
        result = []
        if not isinstance(other, int):
            if self.data.__len__() > other.__len__():
                size = other.__len__()
            else:
                size = self.data.__len__()
        else:
            size = self.data.__len__()

        for i in range(0, size):
            if not isinstance(other, int):
                value = self.data[i] + other[i]
            else:
                value = self.data[i] + other

            result.append(value)
        return result

    def __r__add(self):
        return 0







def main():


    "method a"
    """    x1 = NVector(3, 0, 1)
    x2 = NVector(3, 0, 1)
    x3 = NVector(9, 3, 2, 7)
    print(x1.__len__())
    print(x1[2])
    x1[0] = 4
    x1.to_string()
    print(x1 == x2)
    print(x1 != x3)
    x4 = NVector(3,6,8,1) + NVector(3,8,9,2)
    print(x4)"""
    x5 = NVector(3,0,1) + 10
    print(x5)

if __name__ == "__main__":
    main()