class Country:
    def __init__(self, name: str, cases: list):
        self.name = name
        self.cases = cases

    def get_cases_day(self, day: int):
        return int(self.cases[day - 1])

    def get_weekly_case_velocity(self):
        first_derivatives = []
        for day in range(1, len(self.cases)):
            first_derivatives.append(int(self.cases[day]) - int(self.cases[day - 1]))
        first_derivatives_weekly = []
        counter = 0
        sum = 0
        for item in first_derivatives:
            sum = sum + item
            counter = counter + 1
            if counter == 7:
                first_derivatives_weekly.append(sum / 7)
                sum = 0
                counter = 0
        return first_derivatives_weekly

    def get_weekly_case_acceleration(self):
        first_derivatives_weekly = self.get_weekly_case_velocity()
        second_derivatives = []
        for day in range(1, len(first_derivatives_weekly)):
            second_derivatives.append(first_derivatives_weekly[day] - first_derivatives_weekly[day - 1])
        return second_derivatives

    def merge(self, data: list):
        for index in range(0, len(data)):
            self.cases[index] = str(int(self.cases[index]) + int(data[index]))