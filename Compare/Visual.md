To visualize the network's configuration, we'll use Python with the libraries `python-nmap` and `networkx`. This will allow us to scan the network and then create a visual representation.

Here's a basic script:

```python
import nmap
import networkx as nx
import matplotlib.pyplot as plt

def scan_network(network_range):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments='-T4 -F')

    network_data = {}

    for host, info in scanner.all_hosts().items():
        if 'hostnames' in info:
            hostname = info['hostnames'][0]['name']
        else:
            hostname = host

        network_data[host] = {
            'hostname': hostname,
            'status': info['status']['state']
        }

    return network_data

def visualize_network(network_data):
    graph = nx.Graph()

    for ip, data in network_data.items():
        label = f"{data['hostname']} ({ip})"
        graph.add_node(ip, label=label, status=data['status'])

    # As this is a basic example, we're only adding nodes without explicit edges.
    # In a real-world scenario, you'd add edges based on actual network topology or communication patterns.

    pos = nx.spring_layout(graph)
    labels = nx.get_node_attributes(graph, 'label')
    colors = ['green' if data['status'] == 'up' else 'red' for _, data in network_data.items()]

    nx.draw(graph, pos, labels=labels, with_labels=True, node_color=colors)
    plt.show()

if __name__ == "__main__":
    network_range = "192.168.1.0/24"  # Adjust this as per your network
    network_data = scan_network(network_range)
    visualize_network(network_data)
```

To run the script:

1. Install necessary libraries:

```bash
pip install python-nmap networkx matplotlib
```

2. Execute the Python script.

Note: This is a simple visualization and might not represent the actual configuration/topology of the network. It just shows active hosts. Advanced features like identifying specific devices, links, or inter-device communication patterns would require more detailed scanning and potentially additional tools. Always ensure you have appropriate permissions before scanning any network.
