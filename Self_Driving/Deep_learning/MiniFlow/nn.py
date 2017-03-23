# nn.py

"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""

from miniflow import *

# declare x and y to be input neurons
x, y = Input(), Input()
f = Add(x, y)

feed_dict = {x: 10, y: 5}

sorted_neurons = topological_sort(feed_dict)
output = forward_pass(f, sorted_neurons)

print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))

# bonus quiz
node_output = Input()
f2 = Add(node_output, y)
feed_dict2 = {node_output: output, y: 5}
sorted_neurons = topological_sort(feed_dict2)
output2 = forward_pass(f2, sorted_neurons)
print("({} + {}) + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[y], output2))
