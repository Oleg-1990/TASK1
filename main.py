import csv


def group_csv(file):
    d = dict()
    with open(file, 'r', encoding='utf-8') as file_csv:
        rows = csv.reader(file_csv)
        next(rows)
        for row in rows:
            if row[0] in d:
                d[row[0]]['people'].append(row[1])
                d[row[0]]['count'] = len(d[row[0]]['people'])
            else:
                d[row[0]] = {'people': [], 'count': 0}
                d[row[0]]['people'].append(row[1])

        for key, value in d.items():
            print(f'"{key}": {value}')


if __name__ == '__main__':
    group_csv('data.csv')
