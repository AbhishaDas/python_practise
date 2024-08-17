class TwoDArray:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[0 for _ in range(cols)] for _ in range(rows)]

    def getArray(self):
        print("Enter the array values:")
        for i in range(self.rows):
            row_values = input().split()
            for j in range(self.cols):
                self.array[i][j] = int(row_values[j])

    def displayArray(self):
        print("Array elements are:")
        for row in self.array:
            print("\t".join(map(str, row)))

def main():
    size = int(input("Enter the size of array: "))
    arr = TwoDArray(size, size)
    arr.getArray()
    arr.displayArray()

if __name__ == "__main__":
    main()