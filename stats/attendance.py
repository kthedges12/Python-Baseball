import pandas as pd
import matplotlib.pyplot as plt

from data import games

# attendance = games.reindex((games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3'])
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['years','multi3']]

attendance.columns = ['years','attendance']

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])
print(attendance)

attendance.plot(x='years', y='attendance', figsize=(15,7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), linestyle='dashed', color='green', label='All Star Attendance')
plt.show()
