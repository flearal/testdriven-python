class Math:

    def faculty(self, x):
        result = 1
        for factor in range (1, x + 1):
            result = result * factor

        return result

    def facultyUser(self):
        x = int(input('Please enter a number: '))
        result = self.faculty(x)
        print('The faculty of {} is {}'. format(x, result))
