class SingleRecord:
    def __init__(self, name, value, status, record_date):
        self.name = name
        self.value = value
        self.status = status
        self.record_date = record_date


    def displaySingleRecord(self):
        print('\nname:', self.name,
              '\nvalue:', self.value,
              '\nstatus:', self.status,
              '\nrecord_date:', self.record_date)


