#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# I was supposed to change something in the code to make is faster but do not have much time for that :)
import pandas as pd
import time
import numpy as np
#import the libraries

city_data = { 'chicago': 'chicago.csv',
              'newyork': 'newyork.csv',
              'washington': 'washington.csv' }

#  asks user to specify a city, month, and day to analyze
def get_filters(city, month, day):
    print('Hello! Let\'s explore some US bikeshare data!')

# gets user input  for a city
    print('Pick up a city you\'d like to see data from: Chicago, NewYork, Washington. Type \'q\' if you want to quit')
    cities = ['chicago', 'newyork', 'washington']
    city = ''
    while city != 'q':
        city = str(input('Enter a city: ').lower())
        if city in cities:
            print('Chosen city is: ', city.title())
            break
        elif city == 'q':
            print("Thank you.")
        else:
            print("Please enter a proper name.")
    print('-'*40)

# gets user input for a month
    print('Pick up a month you\'d like to see data from: all, january, february, ..., december. Type \'q\' if you want to quit')
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    month = ''
    while month != 'q':
        month = str(input('Enter a month: ').lower())
        if month in months:
            print('Chosen month is: ', month.title())
            break
        elif month == 'q':
            print("Thank you.")
        else:
            print("Please enter a proper name.")
    print('-'*40)


# gets user input for day of a week
    print('Pick up a day you\'d like to see data from: all, monday, tuesday, ..., sunday. Type \'q\' if you want to quit')
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day != 'q':
        day = str(input('Enter a day: ').lower())
        if day in days:
            print('Chosen day is: ', day.title())
            break
        elif day == 'q':
            print("Thank you.")
        else:
            print("Please enter a proper name.")
    print('-'*40)

    return city, month, day

# loads data for the specified city and filters by month and day if applicable
def load_data(city, month, day):
    if city !='q':
        if month !='q':
            if day !='q':
                months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                          'october', 'november', 'december']
                df = pd.read_csv(city_data[city])
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['month'] = df['Start Time'].dt.month
                df['day_of_week'] = df['Start Time'].dt.weekday_name
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['month'] = df['Start Time'].dt.month
                df['day_of_week'] = df['Start Time'].dt.weekday_name

                # filter by month if applicable
                if month != 'all':
                    # use the index of the months list to get the corresponding int
                    month = months.index(month)
                    # filter by month to create the new dataframe
                    df = df[df['month'] == month]
                # filter by day of week if applicable
                if day != 'all':
                # filter by day of week to create the new dataframe
                    df = df[df['day_of_week'] == day.title()]

                return df
            else:
                df = pd.DataFrame()
                print('No filters were applied to calculate the statistics')
                return df
        else:
                df = pd.DataFrame()
                print('No filters were applied to calculate the statistics')
                return df
    else:
        df = pd.DataFrame()
        print('No filters were applied to calculate the statistics')
        return df

    # displays statistics on the most frequent times of travel.
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]

    print('The most common month is: ', popular_month)
    print('The most common day is: ', popular_day)
    print('The most common hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# displays statistics on the most popular stations and trip.
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Start_end_station'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end_station = df['Start_end_station'].mode()[0]
    print('The most common combination of start and end station is: ', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# displays statistics on the total and average trip duration
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()/360
    print('Total travel time is: ', total_travel_time, ' hours')


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mode()[0]/60
    print('Mean travel time is: ', mean_travel_time, ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# displays statistics on bikeshare users
def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('There is no data to present gender diversity')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birthmin = df['Birth Year'].min()
        birthmax = df['Birth Year'].max()
        birthmode = df['Birth Year'].mode()
        print('Most earliest, most recent and most common year of birth are: ',birthmin, ' ',birthmax, ' ', birthmode)
    else:
        print('There is no data to present statistics about age')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('Do you want to see raw data? Write yes')
    display = ''
    n = 0
    print(display)
    while True:
        display = str(input('Enter a value: ').lower())
        if display == 'yes':
            print('all good')
            print(df.iloc[n:n+5])
            n = n + 5
        else:
            print('Thank you, no more data will be shown')
            break

def main():
    while True:
        city =''
        month = ''

        day = ''
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        if df.empty != True:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)
        else:
            print('Data frame is empty')


        df.head()
        restart = input('\nWould you like to restart? Enter yes to restart or anything to stop.\n')

        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:
