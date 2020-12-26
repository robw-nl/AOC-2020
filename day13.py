# Day 13: Shuttle Search: What is the ID of the earliest bus you can take to the
# airport multiplied by the number of minutes # you'll need to wait for that bus?

timestamp = int(open("day13.txt").read().strip().split()[0])
busses = open("day13.txt").read().strip().split()[1].split(',')
departures = {}

# part 1
for bus in (bus for bus in busses if bus != 'x'):
    bus_id = int(bus)
    # calculate closest departure to your time for each bus
    departing = (bus_id  * (timestamp // bus_id)) + bus_id
    departures[departing] = bus_id

# calculate the wait for the earliest (min) departing bus
wait = min(departures) - timestamp
print(f'Part 1: {wait * departures[min(departures)]}')

# part 2
timestamp, step = 0, 1

# get all bus id's and time offset
bus_ids = [(int(i), j) for j, i in enumerate(busses) if i != 'x']

# iterate through busses
for bus_id, mins in bus_ids:
    # check to see if bus is departing at current time
    while (timestamp + mins) % bus_id != 0:
        timestamp += step
    # increase step multiple to fmem next min for next bus
    step *= bus_id

print(f'Part 2: {timestamp}')
