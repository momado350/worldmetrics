#!pip install worldometer
#pip install worldometer
#https://github.com/matheusfelipeog/worldometer
import worldometer

pop = worldometer.current_world_population()
#{'current_world_population': 7845085923}

twt = worldometer.tweets_sent_today()
#{'tweets_sent_today': 4539558}

com = worldometer.get_metric_of(label='computers_produced_this_year')

#{'computers_produced_this_year': 27760858}

print(pop)
print(twt)
print(com)