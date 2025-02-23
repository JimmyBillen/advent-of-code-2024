from utils import get_input

def isStable(report: list) -> bool:
    """Checks if conditions for stability are met: 
    monotonically increasing / decreasing and differences of adjacent spots at least one and at most three.
    """
    difference_incr = (0 < v2 - v1 <= 3 for v1, v2 in zip(report[:-1], report[1:]))

    reversed_report = report.copy()
    reversed_report.reverse()
    difference_decr = (0 < v2 - v1 <= 3 for v1, v2 in zip(reversed_report[:-1], reversed_report[1:]))
    return all(difference_incr) or all(difference_decr)


def aoc1():
    reports = (list(map(int, line.split())) for line in get_input(day=2))
    safe_reports = sum([isStable(report) for report in reports])

    return safe_reports 


def aoc2():
    reports = (list(map(int, line.split())) for line in get_input(day=2))

    safe_reports = 0
    for report in reports:
        # if it is stable at full length, it will also be stable when one value removed
        for i in range(len(report)):
            
            report_tolerate = report.copy()
            del report_tolerate[i]

            if isStable(report_tolerate):
                safe_reports += 1
                break

    return safe_reports

if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
