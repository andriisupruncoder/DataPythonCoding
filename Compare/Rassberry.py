import pydnp3

# Create a DNP3 master object.
master = pydnp3.Master()

# Connect to the outstation.
master.connect("192.168.1.100", 20000)

# Read the outstation's data.
data = master.read_all()

# Print the data.
print(data)