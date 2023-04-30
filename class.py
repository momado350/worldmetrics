from worldometer import Worldometer
w = Worldometer()

w.what_is_here()
#{'categories': 8, 'labels': 63, 'metrics': 63}

w.categories()
# [   
#     'world_population',
#     'government_and_economics',
#     'society_and_media',
#     ...  # compressed
# ]

w.metrics_labels()
# [   
#     'current_world_population',
#     'births_this_year',
#     'births_today',
#     'deaths_this_year',
#     'deaths_today',
#     'net_population_growth_this_year',
#     ...  # compressed
# ]

w.metrics()
# [   
#     7845087963,
#     15741371,
#     5676,
#     6608605,
#     2383,
#     9132766,
#     ...  # compressed
# ]

labels = w.metrics_with_labels()
print(labels)
# {   
#     'abortions_this_year': 4785492,
#     'bicycles_produced_this_year': 17070566,
#     'births_this_year': 15741371,
#     'births_today': 5676,
#     'blog_posts_written_today': 110171,
#     'cars_produced_this_year': 8999185,
#     'cellular_phones_sold_today': 98846,
#     ...: ...  # compressed
# }