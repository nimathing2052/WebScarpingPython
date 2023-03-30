import csv

class FileWriter:
    def __init__(self, filename, names, labels):
        self.filename = filename
        self.names = names
        self.labels = labels
        
    def write_file(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Name', 'Label'])
            for name, label in zip(self.names, self.labels):
                writer.writerow([name, label])